"""
Smoke test for the full benchmark pipeline.

Trains a tiny vanilla BPE and a tiny linguistically-informed BPE on the
built-in fallback corpus and verifies that:
  1. Both tokenizers train successfully
  2. Both produce a non-empty vocabulary
  3. The metrics are computable and the comparison report is well-formed
  4. The atomic-chunk prior actually changes the coverage (this is the
     whole point of the experiment)
"""

import json
import sys
from pathlib import Path

import pytest

from ml.benchmark_tokenizer import (
    SWAHILI_ATOMIC_CHUNKS,
    train_bpe,
    build_vanilla_pre_tokenizer,
    build_swahili_pre_tokenizer,
    render_markdown,
)
from ml.metrics import compute_stats, chunk_coverage, compare
from ml.data_acquisition import acquire


# Ensure SWAHILI_ATOMIC_CHUNKS is non-empty
def test_atomic_chunks_non_empty():
    assert len(SWAHILI_ATOMIC_CHUNKS) >= 5


# Train a very small tokenizer end-to-end on the built-in corpus
@pytest.fixture(scope="module")
def benchmark_pair(tmp_path_factory):
    corpus = tmp_path_factory.mktemp("corpus") / "sw.txt"
    acquire(corpus, max_chars=10_000)

    # Tiny prior block so the test runs in < 1 second
    tiny_prior = " ".join(SWAHILI_ATOMIC_CHUNKS * 5)
    random_block = " ".join(["lorem", "ipsum", "dolor", "sit", "amet"] * 5)
    text = corpus.read_text(encoding="utf-8")

    vanilla = train_bpe(text + "\n\n" + random_block, vocab_size=200,
                        pre_tokenizer=build_vanilla_pre_tokenizer())
    informed = train_bpe(text + "\n\n" + tiny_prior, vocab_size=200,
                          pre_tokenizer=build_swahili_pre_tokenizer())
    return vanilla, informed, text


def test_both_tokenizers_train(benchmark_pair):
    vanilla, informed, _ = benchmark_pair
    assert vanilla.get_vocab_size() > 0
    assert informed.get_vocab_size() > 0


def test_metrics_computable(benchmark_pair):
    vanilla, informed, text = benchmark_pair
    a = compute_stats(text, vanilla)
    b = compute_stats(text, informed)
    assert a.tokens > 0
    assert b.tokens > 0
    assert 0.0 <= a.fertility <= 5.0
    assert 0.0 <= b.fertility <= 5.0


def test_atomic_chunks_differentially_covered(benchmark_pair):
    """The whole point of the experiment: the linguistically-informed
    tokenizer should have higher coverage of the targeted atomic chunks."""
    vanilla, informed, _ = benchmark_pair
    cov_v = chunk_coverage(vanilla, SWAHILI_ATOMIC_CHUNKS)
    cov_i = chunk_coverage(informed, SWAHILI_ATOMIC_CHUNKS)
    assert cov_i["coverage_rate"] > cov_v["coverage_rate"], (
        f"linguistically-informed coverage {cov_i['coverage_rate']:.0%} "
        f"is not greater than vanilla {cov_v['coverage_rate']:.0%}"
    )


def test_compare_report_well_formed(benchmark_pair):
    vanilla, informed, text = benchmark_pair
    a = compute_stats(text, vanilla)
    b = compute_stats(text, informed)
    cmp = compare(a, b, label_a="A", label_b="B")
    assert "a" in cmp and "b" in cmp
    assert "improvement_b_over_a" in cmp
    for key in ("fertility_pct", "characters_per_token_pct",
                "continued_words_pct", "unknown_rate_pct"):
        assert key in cmp["improvement_b_over_a"]


def test_render_markdown_contains_headline_numbers(benchmark_pair):
    vanilla, informed, text = benchmark_pair
    a = compute_stats(text, vanilla)
    b = compute_stats(text, informed)
    cov_v = chunk_coverage(vanilla, SWAHILI_ATOMIC_CHUNKS)
    cov_i = chunk_coverage(informed, SWAHILI_ATOMIC_CHUNKS)
    cmp = compare(a, b, label_a="v", label_b="i")
    report = {
        "config": {
            "corpus": "x", "vocab_size": 200, "seed": 42, "train_fraction": 0.9,
            "train_sentences": 10, "test_sentences": 2, "train_chars": 1000,
            "test_chars": 200, "atomic_chunks_used": SWAHILI_ATOMIC_CHUNKS,
            "atomic_chunks_from_config": SWAHILI_ATOMIC_CHUNKS,
        },
        "vanilla_bpe": {**a.to_dict(), "train_seconds": 0.0,
                          "actual_vocab_size": 100, "atomic_chunk_coverage": cov_v},
        "linguistically_informed_bpe": {**b.to_dict(), "train_seconds": 0.0,
                                          "actual_vocab_size": 100,
                                          "atomic_chunk_coverage": cov_i},
        "improvement_b_over_a": cmp["improvement_b_over_a"],
    }
    md = render_markdown(report)
    assert "Tokenizer Benchmark" in md
    assert "Fertility" in md
    assert "Vanilla BPE" in md
    assert "Linguistically-Informed BPE" in md
    assert "ng'" in md or "ng" in md
