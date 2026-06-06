# African Native Oral LLM - Optimized Structure

## Core Pipeline (Sequential Execution)

### Phase 1: Data Collection
**Notebook**: `notebooks/01_data_collection.ipynb`
- Ethical consent management
- Audio recording with metadata
- Quality validation
- **Output**: Raw audio + metadata in `data/raw_audio/`

### Phase 2: Audio Processing
**Notebook**: `notebooks/02_audio_processing.ipynb`
- Tonal feature extraction (F0, formants)
- Voice activity detection
- Speech segmentation
- **Output**: Processed segments in `data/processed/`

### Phase 3: Text Preprocessing
**Notebook**: `notebooks/03_text_preprocessing.ipynb`
- Whisper transcription (draft)
- Mandombe script handling
- Text normalization
- **Output**: Transcripts in `data/transcripts/`, corpus in `data/corpus/`

### Phase 4: Tokenizer Training
**Notebook**: `notebooks/04_tokenizer_training.ipynb`
- Custom BPE tokenizer (50% token reduction)
- Mandombe Unicode support
- Tone preservation
- **Output**: Tokenizer in `data/tokenizers/`

### Phase 5: Model Pretraining
**Notebook**: `notebooks/05_model_pretraining.ipynb`
- GPT-style causal LM
- Multiple model sizes (5M-350M params)
- Mixed precision training
- **Output**: Trained model in `data/models/`

## Directory Structure

```
african-native-oral-llm/
├── notebooks/              # Jupyter notebooks (01-05)
├── src/                    # Python modules
│   ├── data-integration.py
│   ├── text-preprocessing.py
│   └── east-african-tokenizer-config.py
├── data/                   # All data (gitignored)
│   ├── raw_audio/
│   ├── processed/
│   ├── metadata/
│   ├── transcripts/
│   ├── corpus/
│   ├── tokenizers/
│   └── models/
├── docs/                   # Documentation
├── hadithi-app/           # Web application
└── 0_COUNCILS/            # Project governance

```

## Efficiency Optimizations

### Memory
- Streaming datasets (90% reduction)
- Batch processing (10-20x faster)
- Gradient accumulation

### Compute
- Mixed precision FP16 (2x speedup)
- Early stopping
- Cached preprocessing

### Cost
- Custom tokenizer (50% token savings)
- Model size selection
- Checkpoint management

## Quick Start

1. **Setup**: Install requirements
2. **Collect**: Run notebook 01 with consent
3. **Process**: Run notebooks 02-03 sequentially
4. **Train**: Run notebooks 04-05 with GPU
5. **Deploy**: Use hadithi-app for inference

## Resource Requirements

| Model Size | VRAM | Training Time | Cost |
|------------|------|---------------|------|
| Tiny (5M)  | 4GB  | 6h           | $5   |
| Small (40M)| 8GB  | 12h          | $10  |
| Base (125M)| 16GB | 24h          | $25  |
| Large (350M)| 24GB| 48h          | $50  |

## Key Files

- `requirements.txt` - Python dependencies
- `readme.md` - Project overview
- `guide.md` - Implementation guide
- `contributing.md` - Contribution guidelines