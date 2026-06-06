"""
Tests for the tokenization-efficiency metrics.

Pure-Python, no external dependencies beyond the standard library + tokenizers.
"""

import pytest
from tokenizers import Tokenizer
from tokenizers.models import BPE
from tokenizers.pre_tokenizers import Whitespace
from tokenizers.trainers import BpeTrainer

from ml.metrics import (
    TokenizationStats,
    compute_stats,
    aggregate_stats,
    compare,
    chunk_coverage,
    tokenize_words,
)


# Fixture: a tiny BPE trained on a tiny English corpus.  We reuse this for
# metric tests because it is fast and deterministic.
@pytest.fixture(scope="module")
def tiny_tokenizer():
    tok = Tokenizer(BPE(unk_token="[UNK]"))
    tok.pre_tokenizer = Whitespace()
    trainer = BpeTrainer(vocab_size=200, special_tokens=["[UNK]", "[PAD]"], show_progress=False)
    corpus = (
        "the quick brown fox jumps over the lazy dog "
        "the cat sat on the mat "
        "she sells sea shells by the sea shore "
        "the tortoise and the hare ran a race"
    )
    tok.train_from_iterator([corpus], trainer=trainer)
    return tok


def test_stats_dataclass_properties():
    s = TokenizationStats(characters=100, words=20, tokens=25, unknown_tokens=1, continued_words=5)
    assert s.fertility == pytest.approx(1.25)
    assert s.characters_per_token == pytest.approx(4.0)
    assert s.proportion_continued_words == pytest.approx(0.25)
    assert s.unknown_rate == pytest.approx(0.05)


def test_stats_zero_words_safe():
    s = TokenizationStats(characters=0, words=0, tokens=0, unknown_tokens=0, continued_words=0)
    assert s.fertility == 0.0
    assert s.characters_per_token == 0.0
    assert s.proportion_continued_words == 0.0
    assert s.unknown_rate == 0.0


def test_compute_stats_runs(tiny_tokenizer):
    stats = compute_stats("the quick brown fox", tiny_tokenizer)
    assert stats.words == 4
    assert stats.tokens > 0
    assert stats.tokens <= stats.words * 5  # sanity bound
    assert 0.0 <= stats.proportion_continued_words <= 1.0


def test_tokenize_words_returns_list_per_word(tiny_tokenizer):
    out = tokenize_words(tiny_tokenizer, "the fox")
    assert len(out) == 2
    for toks in out:
        assert isinstance(toks, list)
        assert all(isinstance(t, str) for t in toks)
        assert len(toks) >= 1


def test_aggregate_stats_sums_correctly():
    s1 = TokenizationStats(characters=100, words=20, tokens=25, unknown_tokens=1, continued_words=5)
    s2 = TokenizationStats(characters=50, words=10, tokens=12, unknown_tokens=0, continued_words=2)
    total = aggregate_stats([s1, s2])
    assert total.characters == 150
    assert total.words == 30
    assert total.tokens == 37
    assert total.unknown_tokens == 1
    assert total.continued_words == 7


def test_compare_relative_improvement_signs():
    """When B is strictly better on fertility (lower) and CPT (higher),
    compare() should report POSITIVE percentages (positive = B is better)."""
    a = TokenizationStats(characters=100, words=20, tokens=30, unknown_tokens=0, continued_words=10)
    b = TokenizationStats(characters=100, words=20, tokens=24, unknown_tokens=0, continued_words=8)
    c = compare(a, b, label_a="A", label_b="B")
    assert c["improvement_b_over_a"]["fertility_pct"] > 0
    assert c["improvement_b_over_a"]["characters_per_token_pct"] > 0
    assert c["improvement_b_over_a"]["continued_words_pct"] > 0


def test_chunk_coverage_basic(tiny_tokenizer):
    """The chunk coverage helper should classify chunks as covered/as-sub/missing."""
    vocab = tiny_tokenizer.get_vocab()
    # Pick a chunk we know is in vocab
    known = next(iter(vocab.keys()))
    cov = chunk_coverage(tiny_tokenizer, [known, "zzzzzzz_definitely_missing"])
    assert cov["total"] == 2
    assert known in cov["covered"]
    assert "zzzzzzz_definitely_missing" in cov["missing"]
    assert cov["coverage_rate"] == pytest.approx(0.5)


def test_chunk_coverage_empty_list(tiny_tokenizer):
    cov = chunk_coverage(tiny_tokenizer, [])
    assert cov["total"] == 0
    assert cov["coverage_rate"] == 0.0
