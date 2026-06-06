"""
Tokenization efficiency metrics
================================

Implements the standard metrics used to compare tokenizers on a target language:

- **Tokens** (count of token IDs the tokenizer produces for a given text)
- **Words** (whitespace-split tokens of the input)
- **Characters** (raw input length)
- **Fertility**  = tokens / words
        Average number of subword pieces per word. Lower is better. The
        canonical "fertility" metric from Rust et al. 2021 ("How Good is Your
        Tokenizer?") is `tokens / words`.
- **Characters per token (CPT)** = characters / tokens
        Inverse density. Higher is better (each token carries more meaning).
- **Proportion of continued words**  = (#words that split into >= 2 tokens) / #words
        Lower is better. High values mean the tokenizer is splitting common
        words into many pieces.
- **Unknown / OOV rate**  = (#words mapped to [UNK]) / #words
        Should be ~0 for a well-trained BPE on its training language.

All metrics are pure functions on a sequence of (words, tokens) pairs.
"""

from __future__ import annotations

from dataclasses import dataclass, asdict
from typing import Iterable, List, Sequence


@dataclass
class TokenizationStats:
    """Aggregate metrics for a tokenizer over a corpus."""
    characters: int
    words: int
    tokens: int
    unknown_tokens: int
    continued_words: int

    @property
    def fertility(self) -> float:
        """Average tokens per word. Lower is better (Rust et al. 2021)."""
        return self.tokens / self.words if self.words else 0.0

    @property
    def characters_per_token(self) -> float:
        """Inverse density. Higher is better."""
        return self.characters / self.tokens if self.tokens else 0.0

    @property
    def proportion_continued_words(self) -> float:
        """Fraction of words split into >= 2 tokens. Lower is better."""
        return self.continued_words / self.words if self.words else 0.0

    @property
    def unknown_rate(self) -> float:
        """Fraction of words mapped to [UNK]. Should be near zero."""
        return self.unknown_tokens / self.words if self.words else 0.0

    def to_dict(self) -> dict:
        d = asdict(self)
        d["fertility"] = self.fertility
        d["characters_per_token"] = self.characters_per_token
        d["proportion_continued_words"] = self.proportion_continued_words
        d["unknown_rate"] = self.unknown_rate
        return d


def chunk_coverage(tokenizer, atomic_chunks) -> dict:
    """
    For a list of "linguistically atomic" chunks, return:
      - total: how many chunks we asked about
      - covered: how many appear as a single token in the vocabulary
      - as_substring: how many appear as a substring of some vocabulary token
                      (i.e. the chunk is a piece of a longer atomic unit)
      - missing: how many are not present at all
      - coverage_rate: covered / total
    """
    vocab = tokenizer.get_vocab()  # dict[str, int]
    covered, as_sub, missing = [], [], []
    for chunk in atomic_chunks:
        if chunk in vocab:
            covered.append(chunk)
        elif any(chunk in tok for tok in vocab):
            as_sub.append(chunk)
        else:
            missing.append(chunk)
    return {
        "total": len(atomic_chunks),
        "covered": covered,
        "as_substring": as_sub,
        "missing": missing,
        "coverage_rate": len(covered) / len(atomic_chunks) if atomic_chunks else 0.0,
    }


def tokenize_words(tokenizer, text: str) -> List[List[str]]:
    """
    Tokenize each whitespace-delimited word individually and return the list of
    subword token strings for each word.

    Using per-word tokenization (rather than `tokenizer.encode(text)`) lets us
    detect which words got split into multiple pieces (continued words) and
    which words were mapped to a single [UNK].

    Works with the HuggingFace `tokenizers` library (v0.20+).
    """
    out: List[List[str]] = []
    for word in text.split():
        enc = tokenizer.encode(word)
        toks = enc.tokens
        if not toks:
            toks = ["[UNK]"]
        out.append(toks)
    return out


def compute_stats(text: str, tokenizer) -> TokenizationStats:
    """Compute aggregate tokenization stats for `text` under `tokenizer`."""
    words = text.split()
    characters = len(text)
    per_word = tokenize_words(tokenizer, text)

    # The HF tokenizers API exposes the UNK token via .tokenizer.unk_token
    # (where .tokenizer is the underlying models.BPE), or via a get_unk_token
    # helper. Fall back to the literal "[UNK]" string.
    try:
        unk_str = tokenizer.tokenizer.unk_token  # type: ignore[attr-defined]
    except AttributeError:
        unk_str = None
    if not unk_str:
        # Try model-level access
        try:
            unk_str = tokenizer.model.unk_token  # type: ignore[attr-defined]
        except AttributeError:
            unk_str = "[UNK]"

    tokens = sum(len(toks) for toks in per_word)
    unknown_tokens = sum(
        1 for toks in per_word
        if len(toks) == 1 and toks[0] == unk_str
    )
    continued_words = sum(1 for toks in per_word if len(toks) >= 2)

    return TokenizationStats(
        characters=characters,
        words=len(words),
        tokens=tokens,
        unknown_tokens=unknown_tokens,
        continued_words=continued_words,
    )


def aggregate_stats(stats_list: Sequence[TokenizationStats]) -> TokenizationStats:
    """Sum per-document stats into a single corpus-level stat."""
    return TokenizationStats(
        characters=sum(s.characters for s in stats_list),
        words=sum(s.words for s in stats_list),
        tokens=sum(s.tokens for s in stats_list),
        unknown_tokens=sum(s.unknown_tokens for s in stats_list),
        continued_words=sum(s.continued_words for s in stats_list),
    )


def compare(stats_a: TokenizationStats, stats_b: TokenizationStats,
            label_a: str = "A", label_b: str = "B") -> dict:
    """
    Return a side-by-side comparison and relative improvement of B over A on
    the two main efficiency metrics: fertility (lower better) and CPT (higher
    better).
    """
    def _rel_pct(a: float, b: float, lower_is_better: bool) -> float:
        """Relative improvement of B over A, as a percentage.

        Positive means B is better than A on this metric.
        For "lower is better" metrics, we flip the sign so that a smaller
        B yields a positive improvement.
        """
        if a == 0:
            return 0.0
        delta = (b - a) / a
        return -delta * 100 if lower_is_better else delta * 100

    return {
        "a": {"label": label_a, **stats_a.to_dict()},
        "b": {"label": label_b, **stats_b.to_dict()},
        "improvement_b_over_a": {
            "fertility_pct": _rel_pct(stats_a.fertility, stats_b.fertility, lower_is_better=True),
            "characters_per_token_pct": _rel_pct(stats_a.characters_per_token,
                                                  stats_b.characters_per_token,
                                                  lower_is_better=False),
            "continued_words_pct": _rel_pct(stats_a.proportion_continued_words,
                                              stats_b.proportion_continued_words,
                                              lower_is_better=True),
            "unknown_rate_pct": _rel_pct(stats_a.unknown_rate, stats_b.unknown_rate,
                                          lower_is_better=True),
        },
    }
