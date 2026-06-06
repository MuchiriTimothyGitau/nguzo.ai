"""
03: Text Preprocessing and Corpus Building
==========================================

Prepare text data for training: transcription workflows, Mandombe script handling, 
and corpus construction.

Objectives:
- Transcribe audio to text
- Handle Mandombe script encoding
- Normalize and clean text
- Build training corpus

For Google Colab usage, copy relevant cells into a notebook.
"""

# Setup
# !pip install -q openai-whisper regex unidecode pandas

import os
import re
import json
import unicodedata
from pathlib import Path
from typing import List, Dict, Optional

import pandas as pd

try:
    import whisper
    WHISPER_AVAILABLE = True
except ImportError:
    WHISPER_AVAILABLE = False
    print("Whisper not available. Install with: pip install openai-whisper")

# Paths configuration (modify for your setup)
# For Google Colab:
# from google.colab import drive
# drive.mount('/content/drive')
# DATA_ROOT = Path('/content/drive/MyDrive/african_oral_llm_data')

# For local:
DATA_ROOT = Path('./data')
PROCESSED_DIR = DATA_ROOT / 'processed'
TRANSCRIPTS_DIR = DATA_ROOT / 'transcripts'
CORPUS_DIR = DATA_ROOT / 'corpus'

for d in [TRANSCRIPTS_DIR, CORPUS_DIR]:
    d.mkdir(parents=True, exist_ok=True)


# =============================================================================
# 2. Automatic Transcription with Whisper
# =============================================================================

class WhisperTranscriber:
    """Transcribe audio using Whisper (for initial draft)."""
    
    def __init__(self, model_size='base'):
        if not WHISPER_AVAILABLE:
            raise ImportError("Whisper not installed. Run: pip install openai-whisper")
        print(f"Loading Whisper {model_size} model...")
        self.model = whisper.load_model(model_size)
    
    def transcribe(self, audio_path: str, language: Optional[str] = None) -> Dict:
        """
        Transcribe audio file.
        
        Args:
            audio_path: Path to audio file
            language: ISO 639-1 code (e.g., 'sw' for Swahili)
        """
        result = self.model.transcribe(
            audio_path,
            language=language,
            task='transcribe',
            verbose=False
        )
        
        return {
            'text': result['text'],
            'segments': result['segments'],
            'language': result.get('language', 'unknown')
        }
    
    def batch_transcribe(self, audio_paths: List[str], language: Optional[str] = None) -> List[Dict]:
        """Transcribe multiple files."""
        results = []
        for path in audio_paths:
            try:
                result = self.transcribe(path, language)
                results.append({'path': path, 'status': 'success', **result})
            except Exception as e:
                results.append({'path': path, 'status': 'error', 'error': str(e)})
        return results


# =============================================================================
# 3. Manual Transcription Workflow
# =============================================================================

class TranscriptionWorkflow:
    """Semi-automated transcription with manual review."""
    
    def __init__(self, transcripts_dir: Path):
        self.transcripts_dir = Path(transcripts_dir)
        self.pending = []
        self.current_index = 0
    
    def load_segments(self, processed_json_path: str) -> List[Dict]:
        """Load audio segments needing transcription."""
        with open(processed_json_path, 'r', encoding='utf-8') as f:
            data = json.load(f)
        
        # Filter segments without transcripts
        for seg in data['segments']:
            transcript_path = self.transcripts_dir / f"{seg['segment_id']}.txt"
            if not transcript_path.exists():
                self.pending.append(seg)
        
        print(f"Loaded {len(self.pending)} segments pending transcription")
        return self.pending
    
    def save_transcription(self, segment_id: str, text: str, 
                          tone_marks: Optional[List] = None, notes: str = "") -> Path:
        """Save transcription with metadata."""
        transcript_data = {
            'segment_id': segment_id,
            'transcription': text,
            'tone_marks': tone_marks or [],
            'transcriber_notes': notes,
            'timestamp': pd.Timestamp.now().isoformat(),
            'reviewed': False
        }
        
        output_path = self.transcripts_dir / f"{segment_id}.json"
        with open(output_path, 'w', encoding='utf-8') as f:
            json.dump(transcript_data, f, indent=2, ensure_ascii=False)
        
        # Also save plain text
        text_path = self.transcripts_dir / f"{segment_id}.txt"
        with open(text_path, 'w', encoding='utf-8') as f:
            f.write(text)
        
        return output_path


# =============================================================================
# 4. Text Normalization for African Languages
# =============================================================================

class AfricanTextNormalizer:
    """
    Normalize text for African languages.
    Handles diacritics, tone marks, and special characters.
    """
    
    # Tone combining characters
    TONE_MARKS = {
        '\u0301': 'HIGH',      # combining acute
        '\u0300': 'LOW',       # combining grave
        '\u0302': 'FALLING',   # combining circumflex
        '\u030c': 'RISING',    # combining caron
        '\u0304': 'MID',       # combining macron
        '\u0307': 'HIGH_DOT',  # combining dot above
    }
    
    # Nasalization marks
    NASAL_MARKS = ['\u0303', '̃']  # combining tilde
    
    @classmethod
    def normalize(cls, text: str, language_code: str = 'kik') -> str:
        """
        Normalize text while preserving linguistic features.
        
        Args:
            text: Input text
            language_code: ISO 639-3 code
        """
        # NFC normalization (compose characters)
        text = unicodedata.normalize('NFC', text)
        
        # Language-specific normalization
        if language_code == 'kik':
            text = cls._normalize_kikongo(text)
        elif language_code == 'yor':
            text = cls._normalize_yoruba(text)
        elif language_code == 'swa':
            text = cls._normalize_swahili(text)
        
        # Common cleaning
        text = cls._common_cleaning(text)
        
        return text
    
    @staticmethod
    def _normalize_kikongo(text: str) -> str:
        """Kikongo-specific normalization."""
        # Handle prenasalized consonants
        text = re.sub(r'mb', 'mb', text, flags=re.IGNORECASE)
        text = re.sub(r'nd', 'nd', text, flags=re.IGNORECASE)
        text = re.sub(r'ng', 'ng', text, flags=re.IGNORECASE)
        text = re.sub(r'nv', 'nv', text, flags=re.IGNORECASE)
        
        # Ensure consistent vowel representation
        text = text.replace('ɛ', 'ε').replace('ɔ', 'o̩')
        
        return text
    
    @staticmethod
    def _normalize_yoruba(text: str) -> str:
        """Yoruba-specific normalization."""
        # Tone mark consistency
        return text
    
    @staticmethod
    def _normalize_swahili(text: str) -> str:
        """Swahili-specific normalization."""
        text = re.sub(r'ch', 'ch', text, flags=re.IGNORECASE)
        text = re.sub(r'sh', 'sh', text, flags=re.IGNORECASE)
        return text
    
    @staticmethod
    def _common_cleaning(text: str) -> str:
        """Common text cleaning."""
        text = re.sub(r'\s+', ' ', text)
        text = re.sub(r'\s+([.,!?;:])', r'\1', text)
        text = re.sub(r'[\x00-\x08\x0b-\x0c\x0e-\x1f\x7f]', '', text)
        return text.strip()
    
    @classmethod
    def extract_tone_pattern(cls, text: str) -> List[str]:
        """Extract tone pattern from text with combining marks."""
        tones = []
        for char in text:
            if char in cls.TONE_MARKS:
                tones.append(cls.TONE_MARKS[char])
        return tones


# =============================================================================
# 5. Corpus Builder
# =============================================================================

class CorpusBuilder:
    """Build training corpus from transcribed segments."""
    
    def __init__(self, output_dir: Path):
        self.output_dir = Path(output_dir)
        self.documents = []
    
    def add_document(self, text: str, metadata: Optional[Dict] = None):
        """Add a document to the corpus."""
        self.documents.append({
            'text': text,
            'metadata': metadata or {}
        })
    
    def add_from_transcriptions(self, transcripts_dir: Path, processed_dir: Path):
        """Add all transcribed segments."""
        for transcript_file in Path(transcripts_dir).glob('*.json'):
            with open(transcript_file, 'r', encoding='utf-8') as f:
                data = json.load(f)
            
            # Find corresponding processed data
            recording_id = data['segment_id'].split('_seg')[0]
            processed_file = Path(processed_dir) / f"{recording_id}_processed.json"
            
            metadata = {'segment_id': data['segment_id']}
            if processed_file.exists():
                with open(processed_file, 'r', encoding='utf-8') as f:
                    processed = json.load(f)
                    for seg in processed['segments']:
                        if seg['segment_id'] == data['segment_id']:
                            metadata.update({
                                'tone_analysis': seg.get('tone_analysis', {}),
                                'duration': seg.get('duration', 0)
                            })
                            break
            
            self.add_document(data['transcription'], metadata)
        
        print(f"Added {len(self.documents)} documents")
    
    def build_corpus(self, output_filename: str = 'corpus.txt',
                    min_length: int = 10, max_length: int = 10000) -> Dict:
        """
        Build and save the training corpus.
        
        Args:
            min_length: Minimum characters per document
            max_length: Maximum characters per document
        """
        output_path = self.output_dir / output_filename
        
        with open(output_path, 'w', encoding='utf-8') as f:
            for doc in self.documents:
                text = doc['text']
                
                if len(text) < min_length or len(text) > max_length:
                    continue
                
                f.write(text + '\n\n')
        
        total_chars = sum(len(d['text']) for d in self.documents)
        total_docs = len(self.documents)
        
        stats = {
            'total_documents': total_docs,
            'total_characters': total_chars,
            'average_length': total_chars / total_docs if total_docs > 0 else 0,
            'output_file': str(output_path)
        }
        
        stats_path = self.output_dir / 'corpus_stats.json'
        with open(stats_path, 'w', encoding='utf-8') as f:
            json.dump(stats, f, indent=2)
        
        print(f"Corpus built: {output_path}")
        print(f"  Documents: {stats['total_documents']}")
        print(f"  Characters: {stats['total_characters']:,}")
        print(f"  Avg length: {stats['average_length']:.0f} chars")
        
        return stats


# =============================================================================
# 6. Dataset Creation
# =============================================================================

def create_datasets_from_corpus(corpus_path: str, 
                                 train_split: float = 0.9,
                                 val_split: float = 0.05,
                                 test_split: float = 0.05):
    """
    Split corpus into train/val/test sets.
    Returns document lists (can be converted to HuggingFace datasets).
    """
    with open(corpus_path, 'r', encoding='utf-8') as f:
        text = f.read()
    
    documents = [d.strip() for d in text.split('\n\n') if d.strip()]
    
    import random
    random.seed(42)
    random.shuffle(documents)
    
    n = len(documents)
    train_end = int(n * train_split)
    val_end = train_end + int(n * val_split)
    
    train_docs = documents[:train_end]
    val_docs = documents[train_end:val_end]
    test_docs = documents[val_end:]
    
    print(f"Datasets created:")
    print(f"  Train: {len(train_docs)} documents")
    print(f"  Val: {len(val_docs)} documents")
    print(f"  Test: {len(test_docs)} documents")
    
    return train_docs, val_docs, test_docs


# =============================================================================
# Example Usage
# =============================================================================

if __name__ == "__main__":
    # Initialize components
    workflow = TranscriptionWorkflow(TRANSCRIPTS_DIR)
    builder = CorpusBuilder(CORPUS_DIR)
    normalizer = AfricanTextNormalizer()
    
    print("Text preprocessing module ready")
    print("Components:")
    print("  - WhisperTranscriber: Automatic transcription")
    print("  - TranscriptionWorkflow: Manual review workflow")
    print("  - AfricanTextNormalizer: Language-specific normalization")
    print("  - CorpusBuilder: Training corpus construction")
