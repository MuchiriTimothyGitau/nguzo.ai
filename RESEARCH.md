# Nguzo.ai: Research Framing and Preliminary Findings

**Author:** Muchiri Timothy Gitau
**Repository:** <https://github.com/MuchiriTimothyGitau/nguzo.ai>
**Date:** 2025-06
**Status:** Preliminary, scope-1 of a larger research programme

---

## Abstract

Nguzo.ai is a research programme that investigates whether low-resource African
languages can be served better by language models that incorporate explicit
linguistic priors during tokenizer training, rather than by scale alone.  This
document describes **Scope 1** of the programme: a controlled experiment that
measures whether a BPE tokenizer trained with Swahili-specific atomic chunks
(prenasalized consonants, digraphs) achieves measurably better tokenization
efficiency and vocabulary coverage than a vanilla BPE with the same data and
vocabulary size.  The atomic chunks are derived from the published
`LanguageTokenizerConfig` registry in `ml/east-african-tokenizer-config.py`.

**Headline result:** on a 10,677-character Swahili text sample, the
linguistically-informed BPE achieves **93% coverage** of the targeted atomic
chunks in its vocabulary, versus **50%** for a vanilla BPE trained on the
same data.  Tokenization fertility improves by **+0.89%** and characters per
token by **+0.90%**.  The fertility improvement is small on this tiny corpus;
the chunk-coverage improvement is large and directly demonstrates the
linguistic prior is doing what it claims to do.  Larger-corpus replications
are queued for Scope 2.

---

## 1. Research question

> Does a BPE tokenizer trained with explicit Swahili-specific atomic-chunk
> priors produce a measurably more efficient tokenizer (in the Rust-et-al.
> 2021 sense) and a vocabulary that better preserves the language's
> phonological inventory, compared to a vanilla BPE trained on the same
> data with the same vocabulary size?

### 1.1 Why this matters

Modern multilingual and African-language language models typically inherit
their tokenizers from large, English-centric pretraining corpora.  This
creates a documented "tokenizer tax" on low-resource and morphologically rich
languages: a Swahili word that would be a single token to a Swahili-aware
tokenizer is split into 2-4 sub-pieces by a vanilla BPE, multiplying the
effective sequence length and reducing sample efficiency (Ahia et al. 2021;
Rust et al. 2021).

The Bantu languages of East Africa, including Swahili, have a well-documented
set of phonological features that BPE merging is unlikely to recover from a
small corpus in a reasonable number of training steps:

- **Prenasalized consonants**: `mb, nd, ng, nj, nz` are single phonemes in
  Bantu phonology.  A vanilla BPE sees them as a nasal + obstruent and may
  split them.
- **Digraphs imported from Arabic and other languages**: `ch, sh, th, dh,
  gh, kh, ny, ng'`.
- **Nasal + glide clusters**: `mw, my, ny, nw`.

The pre-existing `ml/east-african-tokenizer-config.py` module encodes these
chunks as language-specific tokens for 15 East African Bantu languages.  The
research question is whether activating that prior at training time produces
a tokenizer that is provably better than a vanilla BPE, controlling for
training data, vocabulary size, and algorithm.

### 1.2 What "better" means here

We adopt the standard tokenization-efficiency metrics from Rust et al. 2021:

- **Fertility** = tokens / words.  Lower is better.
- **Characters per token** = characters / tokens.  Higher is better.
- **Proportion of continued words** = fraction of words that split into
  >= 2 tokens.  Lower is better.
- **Unknown rate** = fraction of words mapped to `[UNK]`.  Should be ~0 for
  a well-trained BPE on its training language.
- **Atomic-chunk vocabulary coverage** = fraction of the targeted Swahili
  chunks that appear as standalone entries in the trained vocabulary.
  Higher is better; this is the most direct test of the linguistic-prior
  hypothesis.

---

## 2. Related work

- **Rust, P., Pfeiffer, J., Vulić, I., Ruder, S., & Gurevych, I. (2021).**
  *How Good is Your Tokenizer? On the Monolingual vs Cross-Lingual Trade-off.*
  ACL.  Introduces fertility, characters-per-token, and proportion-of-continued-words
  as the standard efficiency metrics for tokenizers; this paper's methodology
  follows theirs.
- **Ahia, O., Kumar, S., Gonen, H., Kasai, J., Mortazavi, N., & Smith, N. A.
  (2021).** *Do All Languages Cost the Same? Tokenization in the Era of
  Multilingual Language Models.*  Empirically shows the tokenizer tax on
  low-resource languages; motivates linguistically-aware tokenization.
- **Ács, J. (2019).** *Exploring BERT's Vocabulary.*  Tokenizer-overlap
  methodology that informs our atomic-chunk coverage metric.
- **Bender, E. M., Gebru, T., McMillan-Major, A., & Shmitchell, S. (2021).**
  *On the Dangers of Stochastic Parrots: Can Language Models Be Too Big?*
  FAccT.  The ethical framing in §6 of this document follows their data-sheet
  and ethical-consent recommendations.
- **Emezue, O. C., & Dossou, F. (2020, 2021).** Masakhane community
  publications on community-driven MT data collection for African languages;
  informs our consent-aware design in `docs/ethical-guidelines.md`.
- **NLLB Team (Costa-jussà et al. 2022).** *No Language Left Behind.*  The
  data-integration script in `ml/data-integration.py` targets the same
  NLLB-derived parallel corpora for Bantu languages.

---

## 3. Method

### 3.1 Data

A Swahili text corpus of **10,677 characters** across **144 sentences**, drawn
either from a public-domain source (unfoldingWord Open Bible Stories, Swahili)
or, when the network is unavailable, from a built-in fallback sample of
public-domain Swahili proverbs and biblical text embedded in
`ml/data_acquisition.py` (the corpus sha256 is recorded in the manifest).

**Why so small?**  This is a Scope-1 controlled experiment.  The point is to
isolate the *effect of the linguistic prior*, not to produce a state-of-the-art
model.  A small corpus keeps the training step under 1 second, the test set
honestly held out, and the entire experiment reproducible on a laptop in
under 5 seconds.  Scope 2 (below) scales the same experiment to >= 100 MB of
Swahili text.

**Train / test split:** 90% / 10%, sentence-stratified, seed 42.  The test
set is held out from both tokenizers' training data and is never augmented
with the atomic-chunk prior block.

### 3.2 Atomic-chunk list

The 14 atomic chunks used in this experiment are taken directly from the
`SWAHILI_CONFIG` dataclass in `ml/east-african-tokenizer-config.py` (built by
`ml/benchmark_tokenizer.py` via `ml/east_african_tokenizer_compat.py`):

```
["ng'", "my", "th", "gh", "ch", "ny", "nd", "nz", "sh", "kh", "ng", "mw", "mb", "dh"]
```

This list is the union of `SWAHILI_CONFIG.special_tokens` (Arabic-influenced
digraphs and `ng'`) and `SWAHILI_CONFIG.prenasalized` (the Bantu prenasalized
consonants `mb, nd, ng, nj, nz`).

### 3.3 Tokenizers

We train **two** BPE tokenizers with the HuggingFace `tokenizers` library
(v0.21.1), holding the following constant:

- BPE algorithm
- Vocabulary size: 8,000
- Training data: identical 129-sentence Swahili training split, plus a
  same-volume *filler* block (~ 600 tokens of Latin text in the vanilla
  case, vs. the same volume of the 14 atomic chunks repeated in the
  linguistically-informed case)
- Special tokens: `[UNK], [PAD], [CLS], [SEP], [MASK]`
- Pre-tokenization: `Whitespace` (i.e. plain word boundaries)
- Random seed: 42

The **only** difference between the two tokenizers is the content of the
filler block added after the training split.  In the vanilla case the filler
is random Latin words, so the total training data volume is matched but no
Swahili-specific prior is present.  In the linguistically-informed case the
filler is the 14 atomic chunks, repeated 50 times, so the BPE trainer sees
each chunk as a frequent standalone pre-token and is biased to keep them
intact in the final vocabulary.

We control for **total data volume** because BPE performance scales with
training data; only the *content* of the prior is the experimental lever.

### 3.4 Metrics

We compute the standard tokenization-efficiency metrics (Rust et al. 2021)
on the held-out test split, plus the atomic-chunk coverage metric
introduced here.  All metrics are implemented in pure Python in
`ml/metrics.py` and unit-tested in `tests/test_metrics.py`.

### 3.5 Reproducibility

- **Code:** this repository, commit hash recorded in `results/`.
- **Data:** `data/swahili_corpus.txt` is checked into the repository, with
  its SHA-256 in the benchmark manifest.
- **Random seed:** 42.
- **Dependencies:** `requirements-lock.txt` pins exact versions of
  `tokenizers==0.21.1`, `numpy==2.2.5`, `pytest==9.0.2`, etc., tested on
  Python 3.13.1.
- **Single-command reproduction:**
  ```
  pip install -r requirements-lock.txt
  python -m pytest tests/         # 35 tests, should all pass
  python ml/benchmark_tokenizer.py
  ```
- **One-click Colab reproduction:** open `colab_runner.ipynb` in Google
  Colab and run all cells.

---

## 4. Results

### 4.1 Headline numbers

| Metric                                  | Vanilla BPE | Linguistically-Informed BPE | Change       |
|-----------------------------------------|------------:|----------------------------:|--------------|
| Vocabulary size (actual)                | 938         | 886                         | -5.5%        |
| Tokens on test (176 words)              | 225         | 223                         | -0.9%        |
| **Fertility** (tokens/word, ↓ better)   | 1.2784      | 1.2670                      | **+0.89%**   |
| **Chars per token** (↑ better)           | 4.94        | 4.98                        | **+0.90%**   |
| Continued-words fraction (↓ better)     | 0.2102      | 0.2102                      | +0.00%       |
| Unknown rate                            | 0.0000      | 0.0000                      | n/a          |
| **Atomic-chunk coverage** (↑ better)    | **50%**     | **93%**                     | **+43 pp**   |

The machine-readable JSON and a Markdown report are saved to
`results/tokenizer_benchmark.json` and `results/tokenizer_benchmark.md`.

### 4.2 Interpretation

**Atomic-chunk coverage is the clearest signal.**  The linguistically-informed
tokenizer ends up with 13 of the 14 targeted Swahili chunks as standalone
vocabulary entries, versus 7 for the vanilla tokenizer.  The chunk it
"misses" (`ng'`) is a corner case: the apostrophe character has separate
status in the BPE byte-level encoding, and on this small corpus the trainer
chose to keep `ng` and `'` as separate tokens rather than merge them.  This
is a known limitation of the byte-level fallback used by HuggingFace BPE and
would be resolved by switching to a pre-tokenizer that handles `ng'` as a
single unit (left as future work).

**Fertility improves marginally** (0.89%) because on a tiny test set most
Swahili words are already in the vocabulary of *both* tokenizers (the actual
vocabularies are 938 and 886 tokens, but the test set only contains 176
words, of which 139 are singletons).  The fertility improvement is therefore
a lower bound: with a larger test set, the gap is expected to widen.  Scope 2
tests this hypothesis on >= 1M characters of held-out text.

**The continued-words fraction is identical** for both tokenizers, because
the test set is too small to register the difference; this metric is a
near-term target for Scope 2.

### 4.3 What the numbers do and do not show

**The numbers DO show:**
- The atomic-chunk prior is doing what the design intends: it shapes the
  vocabulary toward the phonological inventory the linguist specified.
- With matched training data volume, the prior produces a smaller, more
  focused vocabulary (886 vs 938 tokens) and a slightly more efficient
  tokenization on the test set.
- The pipeline (acquire -> split -> train -> score -> report) is
  reproducible end-to-end in < 5 seconds and is fully tested.

**The numbers DO NOT show:**
- That the efficiency improvement generalizes to a larger corpus.  Scope 2
  tests this.
- That a downstream language model trained on the informed tokenizer's
  output converges faster or achieves lower perplexity.  That is Scope 3.
- That the same approach works for the other 14 languages in the registry.
  The methodology transfers, but each language needs its own atomic-chunk
  list and its own replication.

---

## 5. Threats to validity

1. **Corpus size.**  10,677 characters is far below the threshold at which
   tokenization metrics stabilize.  All quantitative claims should be
   considered preliminary until re-run on >= 1M characters of held-out text.
2. **One language only.**  Swahili is the test case.  Results may not
   transfer to lower-resource Bantu languages (e.g. RunyaNkore, Tooro) that
   have less training data to begin with and may benefit more from the prior.
3. **The prior is delivered via corpus augmentation, not pre-tokenization.**
   We tried (and documented) a custom atomic-chunk pre-tokenizer, but the
   HuggingFace `tokenizers` library's `PreTokenizer` API does not support
   pure-Python subclassing in 0.21.  We therefore delivered the prior as a
   repeated block in the training corpus.  This is a controlled
   methodological choice, not a result, and we re-introduce the
   pre-tokenization path in Scope 2 by either (a) implementing it via a Rust
   extension or (b) using a different tokenizer library (SentencePiece) that
   supports custom pre-tokenizers.
4. **The byte-level decoder splits `ng'`.**  This is a known limitation of
   the current setup; Scope 2 either uses `Metaspace` decoding or a
   pre-tokenizer that handles apostrophe-containing clusters.
5. **No human evaluation.**  This is a tokenizer-level study; we do not
   evaluate downstream generation quality, which is a separate question.

---

## 6. Ethics and data sovereignty

This research follows the ethical framework laid out in
[`docs/ethical-guidelines.md`](docs/ethical-guidelines.md).  Key points:

- The fallback corpus embedded in `ml/data_acquisition.py` is public-domain
  Swahili text (catechism, biblical paraphrases, proverbs) assembled for
  testing purposes only; it is *not* the corpus we expect Scope 2 to use.
- The unfoldingWord Open Bible Stories used as the primary acquisition target
  is distributed under CC-BY-SA, with explicit permission for derivative
  works.  Attribution is recorded in the benchmark manifest.
- The NLLB and CC100 corpora targeted by `ml/data-integration.py` are
  accessed only after their respective licenses and access conditions are
  verified (NLLB: CC-BY-SA 4.0; CC100: research-use; KenCorpus: requires
  written request to Maseno University).
- The atomic-chunk prior is derived from the published
  `LanguageTokenizerConfig` registry, which is a curated, language-expert
  resource; no community data is incorporated without consent.
- **Community-led evaluation is the long-term goal.**  Tokenization
  efficiency is a necessary but not sufficient condition for serving a
  language community well.  We commit to community-validated evaluation
  (per Bender et al. 2021) before any production deployment.

---

## 7. Scope 2: planned next steps

The next iteration of this research programme (Scope 2) will:

1. **Scale the corpus** to >= 100 MB of Swahili text (NLLB + CC100 + Open
   Bible Stories + African Storybook Initiative), with the same 90/10
   train/test split and identical metrics.
2. **Add a real pre-tokenizer.**  Switch to SentencePiece or implement a
   Rust `PreTokenizer` extension to deliver the atomic-chunk prior as a
   true pre-tokenization step rather than corpus augmentation.  This
   removes a methodological confound.
3. **Add three languages** from the registry: Luganda (tonal Bantu),
   Kinyarwanda (tonal Bantu, Rwanda-Rundi), and Kikuyu (Thagicu Bantu) to
   test generalizability.
4. **Train a small downstream LM** (5M-40M parameters) on each tokenizer's
   output and report held-out perplexity.  This is the Scope-3 measurement
   and the missing link to "is this useful in practice."
5. **Add tone-preservation metrics** for tonal languages (Luganda,
   Kinyarwanda): does the linguistically-informed tokenizer keep tone
   marks attached to their base vowel more often than the vanilla BPE?

---

## 8. How to reproduce this work

### 8.1 On a laptop (CPU only, < 30 seconds)

```
git clone https://github.com/MuchiriTimothyGitau/nguzo.ai.git
cd nguzo.ai
pip install -r requirements-lock.txt
python -m pytest tests/                      # 35 tests
python ml/data_acquisition.py                # writes data/swahili_corpus.txt
python ml/benchmark_tokenizer.py             # writes results/tokenizer_benchmark.{json,md}
```

### 8.2 On Google Colab (one click)

Open `colab_runner.ipynb` in Colab and run all cells.  Steps 1-3 (install,
test, benchmark) take ~3-5 minutes on the free tier.  Step 4 (full
training pipeline) is commented out by default; uncomment it to run
notebooks 01-05 on a GPU runtime.

### 8.3 Expected outputs

- `results/tokenizer_benchmark.json` - machine-readable benchmark report
- `results/tokenizer_benchmark.md` - human-readable summary
- `data/swahili_corpus.txt` - the corpus used (10,677 characters)
- A passing test suite (`35 passed`)

---

## 9. Citation

```bibtex
@software{nguzo_ai_scope1_2025,
  title={Nguzo.ai Scope 1: A controlled experiment on linguistically-informed BPE for Swahili},
  author={Muchiri, Tim},
  year={2025},
  url={https://github.com/MuchiriTimothyGitau/nguzo.ai},
  note={Preliminary findings.  See RESEARCH.md.}
}
```

---

## 10. Acknowledgements

- The Bantu-language atomic-chunk lists are derived from standard reference
  phonologies (Bastin, Coupez, & Mann 1999; Nurse & Philippson 2003).
- The fallback Swahili corpus in `ml/data_acquisition.py` is in the public
  domain.
- The tokenization-efficiency metrics follow Rust et al. 2021.

---

*This document describes preliminary research.  Numerical results in
§4 are valid as of the commit hash recorded in `results/` and may be
superseded by Scope 2.*
