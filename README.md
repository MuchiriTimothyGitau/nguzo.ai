# Nguzo.ai

> Bridging the language barrier for African languages - end-to-end platform combining an AI-powered web app with an ethical ML training pipeline.

This repository is a unified merge of two complementary projects under the Nguzo.ai umbrella:

| Source | Description |
|---|---|
| `nguzo.ai--Language-Barrier-Bridge-` | AI Studio web app (TypeScript / React / Vite) |
| `nguzo.ai` | Python ML pipeline + Hadithi web app + documentation |

---

## Repository layout

```
nguzo.ai/
├── src/                  # Root web app (TypeScript/React) - from Language-Barrier-Bridge
├── assets/               # Static assets for the root web app
├── index.html            # Root web app entry
├── package.json          # Root web app dependencies
├── server.ts             # Express + tsx dev server
├── tsconfig.json
├── vite.config.ts
├── metadata.json
├── .env.example
│
├── hadithi-app/          # Hadithi web app (Vite + React) - from nguzo.ai
│   ├── src/
│   │   ├── components/   # Layout, LughaMojaKnowledgeMap
│   │   └── pages/        # Home, Languages, Stories, Record, About
│   ├── index.html
│   ├── tailwind.config.js
│   └── vite.config.ts
│
├── ml/                   # Python ML modules (renamed from src/ to avoid path conflict)
│   ├── data-integration.py
│   ├── east-african-tokenizer-config.py
│   └── text-preprocessing.py
│
├── notebooks/            # Jupyter notebooks - ML training pipeline
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
├── contributing.md       # Contribution guidelines
├── guide.md              # Full implementation guide
├── PROJECT_STRUCTURE.md  # ML pipeline structure overview
├── requirements.txt      # Python dependencies
└── README.md             # This file
```

---

## 1. Root web app (Language Barrier Bridge)

A Vite + React + TypeScript app originally generated from Google AI Studio, with an Express server and Gemini API integration.

### Run locally

**Prerequisites:** Node.js

```bash
npm install
cp .env.example .env.local   # then set your GEMINI_API_KEY
npm run dev                  # starts the Express + Vite dev server
```

### Build & start (production)

```bash
npm run build
npm start
```

### Stack

- React 19 + Vite 6
- Tailwind CSS 4 (via `@tailwindcss/vite`)
- `@google/genai` for Gemini API access
- Express + `tsx` for the dev/prod server
- `motion` for animations, `lucide-react` for icons

---

## 2. Hadithi web app

A second, content-focused Vite + React + Tailwind app with pages for Home, Languages, Stories, Recording, and About, plus a knowledge-map component.

### Run locally

```bash
cd hadithi-app
npm install
npm run dev
```

See `hadithi-app/README.md` for details.

---

## 3. Python ML pipeline

A 5-stage Jupyter pipeline for collecting, processing, and training language models on African oral-language data with proper tonal representation, Mandombe script support, and ethical consent.

### Quick start

**Prerequisites:** Python 3.8+, GPU recommended (Google Colab free tier works)

```bash
pip install -r requirements.txt
jupyter notebook notebooks/01_data_collection.ipynb
```

### Pipeline stages

1. **Data Collection** (`01_data_collection.ipynb`) - Ethical audio recording with consent
2. **Audio Processing** (`02_audio_processing.ipynb`) - Tonal feature extraction (F0, formants, VAD)
3. **Text Preprocessing** (`03_text_preprocessing.ipynb`) - Transcription & normalization (Mandombe + Latin scripts)
4. **Tokenizer Training** (`04_tokenizer_training.ipynb`) - Custom BPE, ~50% token reduction
5. **Model Pretraining** (`05_model_pretraining.ipynb`) - GPT-style LM training (5M-350M params)

### Standalone Python modules (`ml/`)

```bash
# List available East African Bantu languages
python ml/data-integration.py --list

# Download data for specific languages
python ml/data-integration.py --language swa kik lug
```

### Key features

- **Tonal language support** - Pitch extraction for tone-bearing languages (Yoruba, Kikongo, etc.)
- **Mandombe script** - Unicode U+1E800-U+1E8DF support
- **Ethical framework** - Community consent, data sovereignty, attribution
- **Efficient tokenization** - 50% fewer tokens vs standard BPE
- **Multiple model sizes** - 5M / 40M / 125M / 350M parameters

### Resource requirements

| Model Size | Params | VRAM  | Training Time | Est. Cost |
|------------|--------|-------|---------------|-----------|
| Tiny       | 5M     | 4 GB  | 6 h           | $5        |
| Small      | 40M    | 8 GB  | 12 h          | $10       |
| Base       | 125M   | 16 GB | 24 h          | $25       |
| Large      | 350M   | 24 GB | 48 h          | $50       |

---

## Languages supported

- **Kikongo** (kik) - Mandombe script
- **Yoruba** (yor) - Tonal
- **Swahili** (swa)
- **Zulu** (zul)
- **Xhosa** (xho)
- **Wolof** (wol)
- **Akan** (aka)
- **Luganda** (lug)
- **Kinyarwanda** (kin)
- **Kikuyu** (kik)

See `docs/east-african-bantu-languages.md` for the full data-source map.

---

## Ethics

- Informed consent is **required** before any data collection
- Communities retain **data ownership** and sovereignty
- **Attribution** to contributors is mandatory
- Use is **non-commercial by default**
- See `docs/ethical-guidelines.md` for the full framework

---

## Documentation

- `guide.md` - Step-by-step implementation guide (incl. Google Colab setup)
- `PROJECT_STRUCTURE.md` - ML pipeline structure and phases
- `docs/ethical-guidelines.md` - Ethical framework
- `docs/east-african-bantu-languages.md` - East African Bantu data sources
- `contributing.md` - How to contribute
- `hadithi-app/README.md` - Hadithi app specifics

---

## Contributing

See `contributing.md` for contribution guidelines, and `docs/ethical-guidelines.md` before any data-related work.

---

## License

MIT License

---

## Citation

```bibtex
@software{nguzo_ai_2026,
  title={Nguzo.ai: African Native Oral Language Model & Language Barrier Bridge},
  author={Muchiri, Tim},
  year={2026},
  url={https://github.com/MuchiriTimothyGitau/nguzo.ai}
}
```

---

## Contact

- GitHub: [@MuchiriTimothyGitau](https://github.com/MuchiriTimothyGitau)
- Project: [nguzo.ai](https://nguzo.ai)

---

*Built for African communities, by African communities, with respect for African knowledge systems.*
