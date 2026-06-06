# Tokenizer Benchmark: Linguistically-Informed BPE vs Vanilla BPE

- **Corpus**: `data\swahili_corpus.txt`
- **Train sentences / chars**: 129 / 9,691
- **Test sentences / chars**:  15 / 1,111
- **Vocabulary size**: 8,000
- **Atomic chunks targeted**: ["ng'", 'my', 'th', 'gh', 'ch', 'ny', 'nd', 'nz', 'sh', 'kh', 'ng', 'mw', 'mb', 'dh']

## Results

| Metric | Vanilla BPE | Linguistically-Informed BPE |
|---|---:|---:|
| Vocabulary size | 938 | 886 |
| Tokens on test | 225 | 223 |
| Words on test  | 176 | 176 |
| Fertility (tokens/word, lower is better) | 1.2784 | 1.2670 |
| Characters per token (higher is better)  | 4.9378 | 4.9821 |
| Continued-words fraction (lower is better) | 0.2102 | 0.2102 |
| Unknown rate (lower is better) | 0.0000 | 0.0000 |
| Training time (s) | 0.0 | 0.0 |

## Atomic-chunk vocabulary coverage

Does the tokenizer actually have the Swahili-specific atomic chunks as
standalone vocabulary entries?

| Tokenizer | Covered | As-substring | Missing | Coverage |
|---|---:|---:|---:|---:|
| Vanilla BPE | 7/14 | 4 | 3 | 50% |
| Linguistically-Informed BPE | 13/14 | 0 | 1 | 93% |

## Improvement of linguistically-informed BPE over vanilla BPE

Positive percentage = the linguistically-informed tokenizer is better
on this metric.  For metrics where *lower is better* (fertility, continued-words,
unknown-rate) a positive number means B's value is lower; for *higher is better*
(characters-per-token) a positive number means B's value is higher.

- **Fertility**: +0.89% (positive = B is more token-efficient)
- **Characters per token**: +0.90% (positive = B carries more meaning per token)
- **Continued-words fraction**: -0.00% (positive = B splits fewer words)
- **Unknown rate**: +0.00% (positive = B has lower OOV)

## Interpretation

These are the two primary efficiency signals from Rust et al. 2021,
*How Good is Your Tokenizer?* on a held-out test split.

The atomic-chunk coverage column is the most direct test of the
linguistic-prior hypothesis: it asks whether the targeted chunks end up
as single base tokens in the vocabulary.  Higher coverage means the
linguistic prior actually shaped the vocabulary the way the design
intended.
