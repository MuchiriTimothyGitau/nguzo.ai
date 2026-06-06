# Nguzo.ai

> A research programme investigating whether low-resource African languages
> are served better by language models that incorporate explicit linguistic
> priors, rather than by scale alone.  This repository is a unified
> combination of the web application, the ML pipeline, and the supporting
> research artifacts.

---

## What's in this repo

| Source | What it is | Where it lives |
|---|---|---|
| `nguzo.ai--Language-Barrier-Bridge-` | AI Studio TypeScript/React web app | root (`src/`, `server.ts`, `vite.config.ts`, ...) |
| `nguzo.ai` (Python side) | ML pipeline + Hadithi web app | `ml/`, `notebooks/`, `hadithi-app/`, `docs/` |
| **Research artifacts (new)** | Scope-1 controlled tokenizer experiment, tests, results | `ml/`, `tests/`, `results/`, `RESEARCH.md` |

**The research artefact is the centerpiece** - see **[`RESEARCH.md`](RESEARCH.md)**
for the research question, method, results, threats to validity, and the
Scope-2 plan.  Headline result: a linguistically-informed BPE tokenizer
trained on Swahili-specific atomic chunks achieves **93% vocabulary coverage
of the targeted chunks** versus **50% for a vanilla BPE** with the same data
and vocabulary size.

---

## Repository layout

```
nguzo.ai/
├── src/                  # Root web app (TypeScript/React)
├── assets/               # Static assets
├── index.html            # Root web app entry
├── package.json          # Root web app deps
├── server.ts             # Express dev server
├── tsconfig.json         # TypeScript config (excludes hadithi-app, ml/)
├── vite.config.ts
├── metadata.json
├── .env.example
│
├── hadithi-app/          # Hadithi Vite/React app
│   ├── src/{components,pages}/
│   ├── index.html
│   ├── tailwind.config.js
│   └── vite.config.ts
│
├── ml/                   # Python ML modules
│   ├── data_acquisition.py            # Fetch small Swahili corpus
│   ├── data-integration.py            # Multi-source East-African data registry
│   ├── east-african-tokenizer-config.py  # Linguistic configs for 15 Bantu langs
│   ├── east_african_tokenizer_compat.py  # Import shim (dashes in filename)
│   ├── text-preprocessing.py          # Whisper + African-text normalization
│   ├── metrics.py                     # Tokenization efficiency metrics
│   ├── benchmark_tokenizer.py         # The Scope-1 experiment
│   └── __init__.py
│
├── notebooks/            # Original 5-stage pipeline (Colab-only, needs torch)
│   ├── 01_data_collection.ipynb
│   ├── 02_audio_processing.ipynb
│   ├── 03_text_preprocessing.ipynb
│   ├── 04_tokenizer_training.ipynb
│   └── 05_model_pretraining.ipynb
│
├── docs/                 # Project documentation
│   ├── east-african-bantu-languages.md
│   └── ethical-guidelines.md
│
├── tests/                # Pytest test suite (35 tests)
│   ├── test_benchmark.py
│   ├── test_data_acquisition.py
│   ├── test_metrics.py
│   └── test_tokenizer_configs.py
│
├── results/              # Generated benchmark outputs
│   ├── tokenizer_benchmark.json
│   └── tokenizer_benchmark.md
│
├── data/                 # Small sample corpora (committed); larger data gitignored
│   └── swahili_corpus.txt
│
├── RESEARCH.md           # The research writeup (READ THIS)
├── colab_runner.ipynb    # One-click Colab reproduction
├── requirements.txt      # Full pipeline deps (torch, whisper, ...)
├── requirements-lock.txt # Pinned research-profile deps
├── guide.md              # Full implementation guide (Colab)
├── PROJECT_STRUCTURE.md  # ML pipeline structure
├── contributing.md
├── readme.md             # (legacy) original repo readme, kept for reference
└── _repo2_readme.md      # (legacy) preserved original readme from nguzo.ai
```

---

## How to run things

### Option A: Reproduce the research artefact (CPU only, < 30 s)

```bash
pip install -r requirements-lock.txt
python -m pytest tests/                  # 35 tests, should all pass
python ml/data_acquisition.py            # writes data/swahili_corpus.txt
python ml/benchmark_tokenizer.py         # writes results/tokenizer_benchmark.{json,md}
```

Then read [`RESEARCH.md`](RESEARCH.md) and inspect
`results/tokenizer_benchmark.md`.

### Option B: Run the root web app (Node)

```bash
npm install
copy .env.example .env.local             # set GEMINI_API_KEY
npm run dev                              # http://localhost:5173 (via Express in server.ts)
```

### Option C: Run the Hadithi web app (Node)

```bash
cd hadithi-app
npm install
npm run dev                              # http://localhost:3000
```

### Option D: Full ML pipeline (Google Colab, GPU)

Open `colab_runner.ipynb` in Colab with a GPU runtime.  Uncomment the
"step 4" cell to execute notebooks 01-05 in sequence.  This is the
6-48-hour path; see `guide.md` for details.

---

## What's "ready to be displayed as research work"?

- **Yes:** the controlled experiment in `ml/benchmark_tokenizer.py`, the
  test suite in `tests/`, the data-acquisition pipeline, the pinned
  dependency set, the `RESEARCH.md` writeup, and the `colab_runner.ipynb`
  one-click reproduction.  These constitute a reproducible, honest
  preliminary finding.
- **Not yet:** Scope 2 (larger corpus, more languages, downstream LM
  perplexity) and Scope 3 (community-validated evaluation).  The roadmap is
  in `RESEARCH.md` §7.

---

## Languages supported (current registry)

From `ml/east-african-tokenizer-config.py`:

| Code | Language        | Family                | Tier |
|------|-----------------|-----------------------|------|
| swa  | Swahili         | Northeast Coast Bantu | 1    |
| kik  | Kikuyu          | Thagicu Bantu         | 1    |
| lug  | Luganda         | Luganda Bantu         | 1    |
| kin  | Kinyarwanda     | Rwanda-Rundi Bantu    | 1    |
| kam  | Kamba           | Central Bantu         | 2    |
| mer  | Meru            | Thagicu Bantu         | 2    |
| bxk  | Lubukusu        | Luhya Bantu           | 2    |
| luo  | Dholuo          | Nilotic               | 2    |
| suk  | Sukuma          | Sukuma-Nyamwezi Bantu | 2    |
| nym  | Nyamwezi        | Sukuma-Nyamwezi Bantu | 3    |
| nyn  | Runyankore      | Luganda Bantu         | 2    |
| ttj  | Tooro           | Luganda Bantu         | 3    |
| run  | Kirundi         | Rwanda-Rundi Bantu    | 2    |
| emb  | Embu            | Thagicu Bantu         | 3    |
| haya | Haya            | Haya-Jita Bantu       | 3    |

---

## Documentation map

- **[`RESEARCH.md`](RESEARCH.md)** - the research writeup (start here)
- `guide.md` - step-by-step Colab walkthrough
- `docs/ethical-guidelines.md` - the ethical framework
- `docs/east-african-bantu-languages.md` - per-language data sources
- `PROJECT_STRUCTURE.md` - the original 5-stage pipeline diagram
- `contributing.md` - how to contribute

---

## Ethics

See `docs/ethical-guidelines.md` for the full framework.  Key commitments:
informed consent before any community-data collection, community data
sovereignty, mandatory attribution, non-commercial use by default, and
community-validated evaluation before any production deployment.

---

## License

MIT

---

## Citation

```bibtex
@software{nguzo_ai_scope1_2025,
  title={Nguzo.ai Scope 1: A controlled experiment on linguistically-informed BPE for Swahili},
  author={Muchiri, Tim},
  year={2025},
  url={https://github.com/MuchiriTimothyGitau/nguzo.ai}
}
```
