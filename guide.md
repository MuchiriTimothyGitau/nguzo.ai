# African Native Oral LLM - Complete Guide

## Table of Contents
1. [Quick Start](#quick-start)
2. [Understanding the Challenge](#understanding-the-challenge)
3. [Data Collection Phase](#data-collection-phase)
4. [Processing Phase](#processing-phase)
5. [Training Phase](#training-phase)
6. [Google Colab Instructions](#google-colab-instructions)

---

## Quick Start

### For Beginners: Use Google Colab (Free GPU)

1. **Open Notebook 01** in Google Colab:
   - Go to [Google Colab](https://colab.research.google.com/)
   - File → Upload notebook → Select `notebooks/01-data-collection.ipynb`
   - Or click the "Open in Colab" badge in any notebook

2. **Connect to GPU** (for training):
   - Runtime → Change runtime type → Select "GPU"

3. **Mount Google Drive**:
   ```python
   from google.colab import drive
   drive.mount('/content/drive')
   ```

4. **Follow notebook steps** in order

---

## East African Bantu Languages - Quick Integration

For East African Bantu languages with **existing data resources**, you can use the data integration script to quickly bootstrap your corpus:

### List Available Languages

```bash
python src/data-integration.py --list
```

### Download Data for Specific Languages

```bash
# Download all available data for Swahili, Kikuyu, and Luganda
python src/data-integration.py --language swa kik lug

# Or download all Tier 1 languages (extensive data)
python src/data-integration.py --tier 1

# Output goes to ./data/<language_code>/
```

### Tier 1 Languages (Ready for Immediate Training)

| Language | Command | Est. Tokens |
|----------|---------|-------------|
| Swahili | `--language swa` | 500M+ |
| Luganda | `--language lug` | 50M+ |
| Kinyarwanda | `--language kin` | 30M+ |
| Kikuyu | `--language kik` | 5M+ |

### Data Sources Integrated

- **NLLB**: Parallel corpora (Meta AI)
- **CC100**: Web-crawled monolingual text
- **KenCorpus**: Maseno University (Swahili, Dholuo, Luhya)
- **Building African Voices**: Speech+text (Dholuo, Suba)
- **Common Voice**: Mozilla speech
- **Masakhane**: Community MT datasets
- **Khaya AI**: Translation models

**Full details**: See [docs/east-african-bantu-languages.md](docs/east-african-bantu-languages.md)

---

## Understanding the Challenge

### Why Current AI Fails African Languages

| Aspect | English-Centric AI | African-Native AI |
|--------|-------------------|-------------------|
| **Tone** | Ignored | Core feature |
| **Proverbs** | Literal translation | Layered meaning |
| **Context** | Individual sentences | Community narrative |
| **Script** | Latin only | Mandombe + others |
| **Data** | Billions of tokens | Thousands (growing) |

### The Solution Framework

```
┌─────────────────────────────────────────────────────────────┐
│              AFRICAN NATIVE ORAL LLM PIPELINE               │
├─────────────────────────────────────────────────────────────┤
│                                                             │
│  1. DATA COLLECTION                                         │
│     ├── Community consent (Notebook 01)                     │
│     ├── Ethical protocols (docs/ethical_guidelines.md)      │
│     └── Structured metadata                               │
│                                                             │
│  2. AUDIO PROCESSING                                        │
│     ├── Tonal feature extraction (Notebook 02)            │
│     ├── Speech segmentation                               │
│     └── Pitch contour analysis                            │
│                                                             │
│  3. TEXT PREPARATION                                        │
│     ├── Transcription workflows (Notebook 03)             │
│     ├── Mandombe script support                           │
│     └── Corpus building                                   │
│                                                             │
│  4. TOKENIZER TRAINING                                      │
│     ├── Custom BPE/SentencePiece (Notebook 04)            │
│     ├── African phonology optimization                    │
│     └── Mandombe Unicode handling                         │
│                                                             │
│  5. MODEL PRE-TRAINING                                      │
│     ├── From-scratch training (Notebook 05)             │
│     ├── Transformer architecture                          │
│     └── African language corpus                           │
│                                                             │
│  6. FINE-TUNING                                             │
│     ├── Oral tradition focus (Notebook 06)                │
│     ├── Proverb understanding                             │
│     └── Narrative generation                              │
│                                                             │
│  7. EVALUATION                                              │
│     ├── Community validation (Notebook 07)                │
│     ├── Cultural accuracy                                 │
│     └── Performance metrics                               │
│                                                             │
└─────────────────────────────────────────────────────────────┘
```

---

## Data Collection Phase

### Using Notebook 01: `01_data_collection.ipynb`

#### Step-by-Step

1. **Setup** (Cell 1-2):
   ```python
   # This installs required packages
   # and mounts your Google Drive
   ```

2. **Initialize Consent System** (Cell 3-4):
   ```python
   # Register each contributor with explicit consent
   contributor = consent_manager.record_consent(
       contributor_id="unique-id",
       contributor_name="Elder Name",
       consent_level="community_control",
       language_community="Kikongo"
   )
   ```

3. **Record or Upload Audio** (Cell 5):
   - Use the Gradio interface
   - Fill in metadata form
   - Audio automatically saved with structured metadata

4. **Validate Quality** (Cell 6-7):
   ```python
   # Check audio meets training standards
   validator.validate_audio('/path/to/recording.wav')
   ```

5. **Generate Summary** (Cell 8):
   ```python
   # View dataset statistics
   summary = generate_dataset_summary()
   ```

### Key Files Created
- `metadata/{recording_id}.json` - Full metadata
- `raw_audio/{recording_id}.wav` - Audio file
- `metadata/consent_records.json` - Consent tracking

---

## Processing Phase

### Using Notebook 02: `02_audio_processing.ipynb`

This notebook extracts tonal features essential for tonal languages.

#### Key Features Extracted

| Feature | Description | Used For |
|---------|-------------|----------|
| F0 (pitch) | Fundamental frequency | Tone recognition |
| Formants | Vowel resonance | Phoneme identification |
| Intensity | Loudness contour | Stress patterns |
| VAD | Voice activity | Segmentation |

#### Running Processing

```python
# Initialize
preprocessor = AudioPreprocessor('/path/to/output')

# Process single file
result = preprocessor.process_recording(
    audio_path='path/to/audio.wav',
    metadata_path='path/to/metadata.json'
)

# Process entire dataset
results = preprocessor.process_dataset(
    metadata_dir='path/to/metadata',
    audio_dir='path/to/raw_audio'
)
```

---

## Training Phase

### Using Notebook 05: `05_model_pretraining.ipynb`

#### Model Sizes Available

| Size | Params | VRAM | Use Case |
|------|--------|------|----------|
| Tiny | 5M | 4GB | Testing/Prototyping |
| Small | 40M | 8GB | Initial training |
| Base | 125M | 16GB | Production model |
| Large | 350M | 24GB | High quality |

#### Training Steps

1. **Configure model**:
   ```python
   config = CONFIGS['base']  # or 'small', 'large'
   ```

2. **Initialize**:
   ```python
   model_config = config.to_gpt2_config()
   model = GPT2LMHeadModel(model_config)
   ```

3. **Train**:
   ```python
   trainer = Trainer(
       model=model,
       args=training_args,
       train_dataset=train_dataset,
       eval_dataset=eval_dataset
   )
   trainer.train()
   ```

---

## Google Colab Instructions

### Free GPU Access

Google Colab provides free GPU time (typically 12 hours per session):

1. **Enable GPU**:
   - Runtime → Change runtime type
   - Hardware accelerator → GPU
   - Save

2. **Check GPU**:
   ```python
   import torch
   print(torch.cuda.get_device_name(0))
   ```

3. **Memory Management**:
   ```python
   # Monitor GPU memory
   !nvidia-smi
   
   # Clear cache if needed
   torch.cuda.empty_cache()
   ```

### Best Practices for Colab

1. **Save to Drive frequently**:
   ```python
   # Mount drive at start
   from google.colab import drive
   drive.mount('/content/drive')
   
   # Save models to drive (persists after session)
   model.save_pretrained('/content/drive/MyDrive/model')
   ```

2. **Resume interrupted training**:
   ```python
   # Load checkpoint
   model = GPT2LMHeadModel.from_pretrained('/content/drive/MyDrive/model/checkpoint-1000')
   ```

3. **Use gradient checkpointing** for larger models:
   ```python
   model.gradient_checkpointing_enable()
   ```

### Alternative: Kaggle Notebooks

Kaggle also provides free GPU:
- 30 hours/week of GPU
- P100 or T4 GPUs
- Direct dataset integration

---

## Project Files Reference

### Notebooks

| Notebook | Purpose | GPU Needed | Notes |
|----------|---------|------------|-------|
| `01-data-collection.ipynb` | Record and organize audio | No | Start here |
| `02-audio-processing.ipynb` | Extract tonal features | Optional | - |
| `03-text-preprocessing.ipynb` | Text Preprocessing | No | ⚠️ Broken, use `src/text-preprocessing.py` |
| `04-tokenizer-training.ipynb` | Train custom tokenizer | No | - |
| `05-model-pretraining.ipynb` | Train base model | Yes | Use Colab |
| `06-finetuning-oral-traditions.ipynb` | Fine-tune on oral traditions | Yes | Use Colab |
| `07-evaluation.ipynb` | Evaluate model | Yes | Use Colab |

### Documentation

- `docs/ethical_guidelines.md` - Ethical framework
- `docs/language_specific/` - Language-specific guides
- `docs/community_protocols/` - Community engagement

---

## Cost Estimates

### Google Colab (Free Tier)
- Data collection: $0
- Preprocessing: $0
- Training (Base model): $0 (limited by session time)

### Google Colab Pro ($10/month)
- Faster GPUs
- Longer sessions
- More memory

### Cloud Training (AWS/GCP)
| Task | Instance | Cost |
|------|----------|------|
| Base model (125M) | V100 (16GB) | ~$25 |
| Large model (350M) | A100 (40GB) | ~$50 |
| Full dataset prep | CPU instance | ~$10 |

---

## Next Steps

1. **Start with Notebook 01** - Set up data collection
2. **Read ethical guidelines** - Essential before any collection
3. **Join community** - Connect with other researchers
4. **Contribute data** - Help grow the corpus
5. **Train models** - Build African-native AI

## Support

- Issues: GitHub Issues
- Discussions: GitHub Discussions
- Email: project@african-native-oral-llm.org

---

*Built for African communities, by African communities, with respect for African knowledge systems.*
