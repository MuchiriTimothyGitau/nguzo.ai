# Nguzo.ai - African Native Oral Language Model

Ethical AI for African oral traditions. Train language models on Kikongo, Yoruba, Swahili, and other African languages with proper tonal representation and Mandombe script support.

## Quick Start

```bash
pip install -r requirements.txt
jupyter notebook notebooks/01_data_collection.ipynb
```

## Pipeline

1. **Data Collection** (`01_data_collection.ipynb`) - Ethical audio recording with consent
2. **Audio Processing** (`02_audio_processing.ipynb`) - Tonal feature extraction
3. **Text Preprocessing** (`03_text_preprocessing.ipynb`) - Transcription & normalization
4. **Tokenizer Training** (`04_tokenizer_training.ipynb`) - Custom BPE (50% token reduction)
5. **Model Pretraining** (`05_model_pretraining.ipynb`) - GPT-style LM training

## Features

- **Tonal Language Support** - Pitch extraction for tone-bearing languages
- **Mandombe Script** - Unicode U+1E800–U+1E8DF support
- **Ethical Framework** - Community consent & data sovereignty
- **Efficient Tokenization** - 50% fewer tokens vs standard BPE
- **Multiple Model Sizes** - 5M to 350M parameters

## Structure

```
nguzo.ai/
├── notebooks/     # 5 Jupyter notebooks (pipeline)
├── src/          # Python modules
├── hadithi-app/  # Web interface
├── docs/         # Documentation
└── data/         # Training data (gitignored)
```

## Requirements

- Python 3.8+
- GPU recommended (Colab free tier works)
- 16GB RAM minimum
- See `requirements.txt` for packages

## Cost Efficiency

| Optimization | Savings |
|--------------|---------|
| Custom tokenizer | 50% tokens |
| Streaming datasets | 90% memory |
| Mixed precision | 2x speed |
| Batch processing | 10-20x faster |

## Model Sizes

| Size | Params | VRAM | Training Time | Cost |
|------|--------|------|---------------|------|
| Tiny | 5M | 4GB | 6h | $5 |
| Small | 40M | 8GB | 12h | $10 |
| Base | 125M | 16GB | 24h | $25 |
| Large | 350M | 24GB | 48h | $50 |

## Ethics

- Informed consent required
- Community data ownership
- Attribution mandatory
- Non-commercial by default
- See `docs/ethical-guidelines.md`

## Languages Supported

- Kikongo (kik) - Mandombe script
- Yoruba (yor) - Tonal
- Swahili (swa)
- Zulu (zul)
- Xhosa (xho)
- Wolof (wol)
- Akan (aka)

## Contributing

See `contributing.md` for guidelines.

## License

MIT License - See LICENSE file

## Citation

```bibtex
@software{nguzo_ai_2026,
  title={Nguzo.ai: African Native Oral Language Model},
  author={Muchiri, Tim},
  year={2026},
  url={https://github.com/muchiriTimdev/nguzo.ai}
}
```

## Contact

- GitHub: [@muchiriTimdev](https://github.com/muchiriTimdev)
- Project: [nguzo.ai](https://nguzo.ai)
