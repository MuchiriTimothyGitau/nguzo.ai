"""
East African Bantu Language Tokenizer Configuration
====================================================

Specialized tokenizer configurations for East African Bantu languages,
optimized for their phonological and morphological features.

Features handled:
- Prenasalized consonants (mb, nd, ng, nj, nz)
- Common affixes (nominal and verbal prefixes)
- Tone marks (for tonal languages like Luganda, Kinyarwanda)
- Digraphs and trigraphs
- Language-specific sound combinations

Usage:
    from east_african_tokenizer_config import get_tokenizer_config
    
    config = get_tokenizer_config('lug')  # Luganda
    tokenizer = train_tokenizer(config)
"""

from typing import Dict, List, Optional
from dataclasses import dataclass, field


@dataclass
class LanguageTokenizerConfig:
    """Configuration for training a language-specific tokenizer."""
    
    language_code: str
    language_name: str
    family: str
    
    # Special tokens to include in initial vocabulary
    special_tokens: List[str] = field(default_factory=list)
    
    # Common prefixes/suffixes for better tokenization
    prefixes: List[str] = field(default_factory=list)
    suffixes: List[str] = field(default_factory=list)
    
    # Prenasalized consonants (treat as single units)
    prenasalized: List[str] = field(default_factory=list)
    
    # Tone marks (for tonal languages)
    tone_marks: List[str] = field(default_factory=list)
    tone_aware: bool = False
    
    # Character sets
    vowels: str = "aeiou"
    consonants: str = "bcdfghjklmnpqrstvwxyz"
    
    # Special characters beyond basic Latin
    special_characters: List[str] = field(default_factory=list)
    
    # BPE training parameters
    vocab_size: int = 32000
    min_frequency: int = 2
    
    # Pre-tokenization pattern (regex)
    pre_tokenization_pattern: Optional[str] = None
    
    # Normalization rules
    normalize_unicode: bool = True
    lowercase: bool = False  # Most African languages preserve case
    
    def to_dict(self) -> Dict:
        """Convert configuration to dictionary."""
        return {
            'language_code': self.language_code,
            'language_name': self.language_name,
            'family': self.family,
            'special_tokens': self.special_tokens,
            'prefixes': self.prefixes,
            'suffixes': self.suffixes,
            'prenasalized': self.prenasalized,
            'tone_aware': self.tone_aware,
            'tone_marks': self.tone_marks if self.tone_aware else [],
            'vocab_size': self.vocab_size,
            'vowel_inventory': self.vowels,
            'consonant_inventory': self.consonants,
            'special_characters': self.special_characters,
        }


# ============================================
# THAGICU LANGUAGES (Kenya - Central/Eastern)
# ============================================

KIKUYU_CONFIG = LanguageTokenizerConfig(
    language_code='kik',
    language_name='Kikuyu/Gikuyu',
    family='Thagicu Bantu',
    
    special_tokens=[
        # Prenasalized consonants
        'mb', 'nd', 'ng', 'nj', 'nz', 'nv', 'mv',
        # Common consonant clusters
        'ng\'', 'ny', 'th',
        # Implosives (if using special notation)
        'ɓ', 'ɗ',
    ],
    
    prefixes=[
        # Nominal prefixes
        'mu', 'wa', 'mi', 'ma', 'ki', 'vi', 'i', 'u',
        # Verbal prefixes
        'n', 'u', 'a', 'tu', 'mu', 'wa',
        # Locative
        'ga', 'gw',
    ],
    
    suffixes=[
        # Verb extensions
        'a', 'ia', 'ea', 'ana', 'aana',
        # Final vowels
        'a', 'e', 'i', 'o', 'u',
    ],
    
    prenasalized=['mb', 'nd', 'ng', 'nj', 'nz', 'nv', 'mv'],
    
    tone_aware=True,
    tone_marks=['\u0301', '\u0300', '\u0302'],  # acute, grave, circumflex
    
    vowels='aeiou',
    consonants='bcdfghjklmnpqrstvwxyzɓɗ',
    
    vocab_size=32000,
    min_frequency=2,
)

KAMBA_CONFIG = LanguageTokenizerConfig(
    language_code='kam',
    language_name='Kamba',
    family='Central Bantu',
    
    special_tokens=[
        'mb', 'nd', 'ng', 'nj', 'nz',
        'ng\'', 'ny', 'th', 'sy', 'zy',
    ],
    
    prefixes=[
        'mu', 'wa', 'mi', 'ma', 'ki', 'i', 'u',
        'n', 'u', 'a', 'tu', 'mu', 'wa',
    ],
    
    suffixes=[
        'a', 'ia', 'ea', 'ana', 'wa', 'ya',
    ],
    
    prenasalized=['mb', 'nd', 'ng', 'nj', 'nz'],
    tone_aware=True,
    tone_marks=['\u0301', '\u0300'],
    vocab_size=28000,
)

MERU_CONFIG = LanguageTokenizerConfig(
    language_code='mer',
    language_name='Meru',
    family='Thagicu Bantu',
    
    special_tokens=[
        'mb', 'nd', 'ng', 'nj',
        'ng\'', 'ny', 'th',
    ],
    
    prefixes=[
        'mu', 'wa', 'mi', 'ma', 'ki', 'i', 'u',
        'n', 'u', 'a', 'tu', 'mu', 'wa',
    ],
    
    prenasalized=['mb', 'nd', 'ng', 'nj'],
    tone_aware=True,
    vocab_size=24000,
)

EMBU_CONFIG = LanguageTokenizerConfig(
    language_code='emb',
    language_name='Embu',
    family='Thagicu Bantu',
    
    special_tokens=[
        'mb', 'nd', 'ng', 'nj',
        'ng\'', 'ny',
    ],
    
    prefixes=[
        'mu', 'wa', 'mi', 'ma', 'ki', 'i', 'u',
    ],
    
    prenasalized=['mb', 'nd', 'ng', 'nj'],
    tone_aware=True,
    vocab_size=20000,
)


# ============================================
# LUGANDA & RELATED (Uganda - Central)
# ============================================

LUGANDA_CONFIG = LanguageTokenizerConfig(
    language_code='lug',
    language_name='Luganda',
    family='Luganda Bantu',
    
    special_tokens=[
        # Prenasalized
        'mb', 'nd', 'ng', 'nj', 'nz', 'nv',
        # Palatalized
        'gy', 'ky', 'ny', 'by', 'py',
        # Other clusters
        'ng\'', 'nny', 'ly', 'ry',
    ],
    
    prefixes=[
        # Noun class prefixes
        'mu', 'ba',       # Class 1/2 (person)
        'lu', 'n',        # Class 11/10 (long things)
        'gu', 'ga',       # Class 5/6 (liquids)
        'bu', 'ma',       # Class 14/6 (abstract)
        'ku', 'tu',       # Class 15/13 (infinitive)
        'ki', 'bi',       # Class 7/8 (things)
        'li', 'ma',       # Class 5/6 (fruits)
        'ka', 'tu',       # Class 12/13 (diminutive)
        # Verbal
        'n', 'o', 'a', 'tu', 'mu', 'ba',
        # Object markers
        'mu', 'gu', 'ki', 'bi', 'n',
    ],
    
    suffixes=[
        # Verb extensions
        'a', 'e', 'i', 'o', 'u',
        'wa', 'ya', 'kye', 'bye',
        # TAM markers
        'a', 'e', 'i', 'o',
    ],
    
    prenasalized=['mb', 'nd', 'ng', 'nj', 'nz', 'nv'],
    
    tone_aware=True,
    tone_marks=['\u0301', '\u0300', '\u0302', '\u0304'],  # acute, grave, circumflex, macron
    
    vowels='aeiou',
    consonants='bcdfghjklmnpqrstvwxyz',
    
    # Vowel length matters
    special_characters=['\u0304'],  # macron for long vowels
    
    vocab_size=32000,
)

RUNYANKORE_CONFIG = LanguageTokenizerConfig(
    language_code='nyn',
    language_name='Runyankore-Rukiga',
    family='Luganda Bantu',
    
    special_tokens=[
        'mb', 'nd', 'ng', 'nj',
        'gy', 'ky', 'ny',
        'ng\'',
    ],
    
    prefixes=[
        'mu', 'ba', 'ru', 'ma',
        'bu', 'ku', 'tu',
        'n', 'o', 'a', 'tu', 'mu', 'ba',
    ],
    
    prenasalized=['mb', 'nd', 'ng', 'nj'],
    tone_aware=True,
    tone_marks=['\u0301', '\u0300'],
    vocab_size=28000,
)

TOORO_CONFIG = LanguageTokenizerConfig(
    language_code='ttj',
    language_name='Tooro',
    family='Luganda Bantu',
    
    special_tokens=[
        'mb', 'nd', 'ng', 'nj',
        'gy', 'ky', 'ny',
    ],
    
    prefixes=[
        'mu', 'ba', 'ru', 'ma',
        'bu', 'ku', 'tu',
    ],
    
    prenasalized=['mb', 'nd', 'ng', 'nj'],
    tone_aware=True,
    vocab_size=20000,
)


# ============================================
# RWANDA-RUNDI (Rwanda, Burundi, DRC)
# ============================================

KINYARWANDA_CONFIG = LanguageTokenizerConfig(
    language_code='kin',
    language_name='Kinyarwanda',
    family='Rwanda-Rundi Bantu',
    
    special_tokens=[
        'mb', 'nd', 'ng', 'nj', 'nz',
        'pf', 'tf', 'kv', 'tsv',
        'rw', 'tw', 'kw', 'sw',
        'ng\'', 'ny', 'shy', 'shy',
    ],
    
    prefixes=[
        # Noun classes
        'umu', 'aba',      # 1/2
        'umu', 'imi',      # 3/4
        'iki', 'ibi',      # 7/8
        'i', 'ama',        # 5/6
        'aka', 'utu',      # 12/13
        'obu', 'ama',      # 14/6
        'a', 'ama',        # 16/6
        'uru', 'ama',      # 11/6
        'ku', 'ma',        # 15/6
        'ho', 'mu',        # 17/18
        # Verbal
        'n', 'u', 'a', 'tu', 'mu', 'ba',
        # Object markers
        'mu', 'ku', 'i', 'ri', 'wa',
    ],
    
    suffixes=[
        'a', 'e', 'i', 'o', 'u',
        'wa', 'we', 'ye',
    ],
    
    prenasalized=['mb', 'nd', 'ng', 'nj', 'nz'],
    
    tone_aware=True,
    tone_marks=['\u0301', '\u0300', '\u0302'],
    
    vowels='aeiou',
    consonants='bcdfghjklmnpqrstvwxyz',
    
    vocab_size=32000,
)

KIRUNDI_CONFIG = LanguageTokenizerConfig(
    language_code='run',
    language_name='Kirundi',
    family='Rwanda-Rundi Bantu',
    
    special_tokens=[
        'mb', 'nd', 'ng', 'nj', 'nz',
        'pf', 'tf', 'kv',
        'rw', 'ng\'', 'ny',
    ],
    
    prefixes=[
        'umu', 'aba', 'umu', 'imi',
        'iki', 'ibi', 'i', 'ama',
        'n', 'u', 'a', 'tu', 'mu', 'ba',
    ],
    
    prenasalized=['mb', 'nd', 'ng', 'nj', 'nz'],
    tone_aware=True,
    vocab_size=28000,
)


# ============================================
# SWAHILI & COASTAL LANGUAGES
# ============================================

SWAHILI_CONFIG = LanguageTokenizerConfig(
    language_code='swa',
    language_name='Swahili',
    family='Northeast Coast Bantu',
    
    special_tokens=[
        # Digraphs
        'ch', 'dh', 'gh', 'kh', 'ng\'', 'ny', 'sh', 'th',
        # Common in Arabic loans
        'mb', 'nd', 'ng', 'nz',
        # Glides
        'mw', 'my', 'ny',
    ],
    
    prefixes=[
        # Noun classes
        'm', 'wa',         # 1/2 (mwanafunzi/wanafunzi)
        'm', 'mi',         # 3/4 (mti/miti)
        'ki', 'vi',        # 7/8 (kitu/vitu)
        'i', 'ma',         # 5/6 (jicho/macho)
        'zi', 'ma',        # With augment
        'u', 'nya',        # 11/10 (ubao/nyao)
        'ku', 'ma',        # 15 (infinitive)
        'pa', 'ku', 'mu',  # 16/17/18 (locative)
        # Verbal
        'ni', 'u', 'a', 'tu', 'm', 'wa',
        'si', 'hu', 'ha',  # Negatives
        # Object markers
        'ni', 'ku', 'm', 'wa', 'ki', 'vi', 'i', 'zi',
    ],
    
    suffixes=[
        # Final vowels
        'a', 'i', 'e',
        # Extensions
        'wa', 'ka', 'sha', 'ana', 'wa', 'kwa',
        # Tense/aspect
        'li', 'na', 'ta', 'me', 'ngali',
    ],
    
    prenasalized=['mb', 'nd', 'ng', 'nz'],
    
    tone_aware=False,  # Swahili tone is not written
    
    vowels='aeiou',
    consonants='bcdfghjklmnpqrstvwxyz',
    
    # Arabic influence
    special_characters=['],
    
    vocab_size=48000,  # Larger due to more data
)


# ============================================
# LUYHA LANGUAGES (Western Kenya)
# ============================================

LUBUKUSU_CONFIG = LanguageTokenizerConfig(
    language_code='bxk',
    language_name='Lubukusu',
    family='Luhya Bantu',
    
    special_tokens=[
        'mb', 'nd', 'ng', 'nj', 'nz',
        'ng\'', 'ny', 'sy', 'zy',
        'bw', 'lw', 'mw', 'nyw',
    ],
    
    prefixes=[
        'umu', 'aba', 'esi', 'e',
        'li', 'ama', 'si', 'tsi',
        'lu', 'ma', 'ku', 'bu',
        'a', 'ba',
    ],
    
    prenasalized=['mb', 'nd', 'ng', 'nj', 'nz'],
    tone_aware=True,
    vocab_size=24000,
)

LUO_CONFIG = LanguageTokenizerConfig(
    language_code='luo',
    language_name='Dholuo',
    family='Nilotic (non-Bantu)',
    
    special_tokens=[
        'nd', 'ng', 'ny', 'nw', 'nyw',
        'th', 'dh',
        'kw', 'gw', 'jw',
    ],
    
    prefixes=[
        'ja', 'gi', 'ni', 'chi',
        'o', 'i', 'wa',
    ],
    
    prenasalized=['nd', 'ng', 'ny'],
    tone_aware=True,
    tone_marks=['\u0301', '\u0300', '\u0302'],
    vocab_size=24000,
)


# ============================================
# TANZANIAN LANGUAGES
# ============================================

SUKUMA_CONFIG = LanguageTokenizerConfig(
    language_code='suk',
    language_name='Sukuma',
    family='Sukuma-Nyamwezi Bantu',
    
    special_tokens=[
        'mb', 'nd', 'ng', 'nj', 'nz',
        'bw', 'dw', 'gw', 'jw', 'kw', 'lw', 'mw', 'nw', 'pw', 'sw', 'tw', 'vw', 'zw',
        'ng\'', 'ny',
    ],
    
    prefixes=[
        'mu', 'ba', 'mu', 'mi',
        'ma', 'ga', 'ka', 'tu',
        'lu', 'ma', 'bu', 'ku',
        'n', 'u', 'a', 'tu', 'mu', 'ba',
    ],
    
    prenasalized=['mb', 'nd', 'ng', 'nj', 'nz'],
    tone_aware=True,
    vocab_size=24000,
)

NYAMWEZI_CONFIG = LanguageTokenizerConfig(
    language_code='nym',
    language_name='Nyamwezi',
    family='Sukuma-Nyamwezi Bantu',
    
    special_tokens=[
        'mb', 'nd', 'ng', 'nj',
        'bw', 'dw', 'gw', 'kw', 'lw', 'mw', 'sw', 'tw',
        'ng\'', 'ny',
    ],
    
    prefixes=[
        'mu', 'ba', 'mu', 'mi',
        'ma', 'li', 'ka', 'tu',
        'n', 'u', 'a', 'tu', 'mu', 'ba',
    ],
    
    prenasalized=['mb', 'nd', 'ng', 'nj'],
    tone_aware=True,
    vocab_size=20000,
)

HAYA_CONFIG = LanguageTokenizerConfig(
    language_code='haya',
    language_name='Haya',
    family='Haya-Jita Bantu',
    
    special_tokens=[
        'mb', 'nd', 'ng', 'nj',
        'gy', 'ky', 'ny',
        'bw', 'gw', 'kw', 'mw', 'nw', 'nyw',
    ],
    
    prefixes=[
        'omu', 'aba', 'omu', 'emi',
        'eki', 'ebi', 'eri', 'ama',
        'n', 'o', 'a', 'tu', 'mu', 'ba',
    ],
    
    prenasalized=['mb', 'nd', 'ng', 'nj'],
    tone_aware=True,
    tone_marks=['\u0301', '\u0300', '\u0302', '\u0304'],
    vocab_size=20000,
)


# ============================================
# CONFIGURATION REGISTRY
# ============================================

TOKENIZER_CONFIGS = {
    # Thagicu (Kenya Central)
    'kik': KIKUYU_CONFIG,
    'kam': KAMBA_CONFIG,
    'mer': MERU_CONFIG,
    'emb': EMBU_CONFIG,
    
    # Luganda group (Uganda)
    'lug': LUGANDA_CONFIG,
    'nyn': RUNYANKORE_CONFIG,
    'ttj': TOORO_CONFIG,
    
    # Rwanda-Rundi
    'kin': KINYARWANDA_CONFIG,
    'run': KIRUNDI_CONFIG,
    
    # Swahili
    'swa': SWAHILI_CONFIG,
    
    # Luhya (Kenya Western)
    'bxk': LUBUKUSU_CONFIG,
    'luo': LUO_CONFIG,  # Nilotic but included
    
    # Tanzanian
    'suk': SUKUMA_CONFIG,
    'nym': NYAMWEZI_CONFIG,
    'haya': HAYA_CONFIG,
}


def get_tokenizer_config(language_code: str) -> LanguageTokenizerConfig:
    """
    Get tokenizer configuration for a language.
    
    Args:
        language_code: ISO 639-3 code
        
    Returns:
        LanguageTokenizerConfig object
        
    Raises:
        KeyError if language not in registry
    """
    if language_code not in TOKENIZER_CONFIGS:
        available = list(TOKENIZER_CONFIGS.keys())
        raise KeyError(
            f"No tokenizer config for '{language_code}'. "
            f"Available: {available}"
        )
    
    return TOKENIZER_CONFIGS[language_code]


def list_available_configs() -> Dict[str, str]:
    """List all available tokenizer configurations."""
    return {
        code: config.language_name 
        for code, config in TOKENIZER_CONFIGS.items()
    }


def create_tokenizer_training_config(
    language_code: str,
    output_dir: str,
    additional_special_tokens: Optional[List[str]] = None
) -> Dict:
    """
    Create a complete configuration dict for tokenizer training.
    
    Args:
        language_code: ISO 639-3 code
        output_dir: Where to save the tokenizer
        additional_special_tokens: Extra tokens to include
        
    Returns:
        Dictionary with all training parameters
    """
    config = get_tokenizer_config(language_code)
    
    training_config = {
        'language': config.to_dict(),
        'output_dir': output_dir,
        'vocab_size': config.vocab_size,
        'min_frequency': config.min_frequency,
        'special_tokens': {
            'pad_token': '[PAD]',
            'unk_token': '[UNK]',
            'cls_token': '[CLS]',
            'sep_token': '[SEP]',
            'mask_token': '[MASK]',
            'bos_token': '[BOS]',
            'eos_token': '[EOS]',
        },
        'language_specific_tokens': (
            config.special_tokens + 
            config.prenasalized +
            (additional_special_tokens or [])
        ),
        'pre_tokenization': {
            'split_on_prenasalized': True,
            'preserve_tone_marks': config.tone_aware,
        },
        'normalization': {
            'unicode_normalize': config.normalize_unicode,
            'lowercase': config.lowercase,
        }
    }
    
    return training_config


# ============================================
# UTILITY FUNCTIONS
# ============================================

def get_family_configs(family: str) -> List[LanguageTokenizerConfig]:
    """
    Get all tokenizer configs for a language family.
    
    Args:
        family: Family name (e.g., 'Thagicu Bantu', 'Luganda Bantu')
        
    Returns:
        List of configurations
    """
    return [
        config for config in TOKENIZER_CONFIGS.values()
        if config.family == family
    ]


def get_tier_1_configs() -> List[LanguageTokenizerConfig]:
    """Get configs for Tier 1 languages (extensive data)."""
    tier_1_codes = ['swa', 'lug', 'kin', 'kik']
    return [TOKENIZER_CONFIGS[code] for code in tier_1_codes if code in TOKENIZER_CONFIGS]


def get_tier_2_configs() -> List[LanguageTokenizerConfig]:
    """Get configs for Tier 2 languages (moderate data)."""
    tier_2_codes = ['kam', 'mer', 'bxk', 'luo', 'suk']
    return [TOKENIZER_CONFIGS[code] for code in tier_2_codes if code in TOKENIZER_CONFIGS]


def print_config_summary(config: LanguageTokenizerConfig):
    """Print a readable summary of a tokenizer configuration."""
    print(f"\n{'='*60}")
    print(f"Tokenizer Config: {config.language_name} ({config.language_code})")
    print(f"{'='*60}")
    print(f"Family: {config.family}")
    print(f"Vocabulary Size: {config.vocab_size:,}")
    print(f"Tone Aware: {config.tone_aware}")
    print(f"\nSpecial Tokens ({len(config.special_tokens)}):")
    for i, token in enumerate(config.special_tokens[:20]):
        print(f"  - '{token}'")
    if len(config.special_tokens) > 20:
        print(f"  ... and {len(config.special_tokens) - 20} more")
    
    print(f"\nPrenasalized Consonants ({len(config.prenasalized)}):")
    print(f"  {', '.join(config.prenasalized)}")
    
    print(f"\nCommon Prefixes ({len(config.prefixes)}):")
    print(f"  {', '.join(config.prefixes[:10])}")
    
    print(f"\nTone Marks:")
    if config.tone_aware:
        for mark in config.tone_marks:
            print(f"  - U+{ord(mark):04X}: {mark}")
    else:
        print("  (Not tone-aware)")


if __name__ == "__main__":
    # Demo: print all configs
    print("\n" + "="*60)
    print("East African Bantu Tokenizer Configurations")
    print("="*60)
    
    for code, config in TOKENIZER_CONFIGS.items():
        print_config_summary(config)
    
    print("\n" + "="*60)
    print(f"Total configurations: {len(TOKENIZER_CONFIGS)}")
    print("="*60)
