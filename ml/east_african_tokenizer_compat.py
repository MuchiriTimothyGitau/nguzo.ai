"""
Import shim for `east-african-tokenizer-config.py`.

The original file uses dashes in its filename, which Python cannot import
directly.  This module loads it with `importlib.util.spec_from_file_location`
and re-exports the public names so the rest of the codebase can use a normal
`from ml.east_african_tokenizer_compat import get_tokenizer_config` import.
"""

from __future__ import annotations

import importlib.util
from pathlib import Path

_HERE = Path(__file__).resolve().parent
_TARGET = _HERE / "east-african-tokenizer-config.py"

if not _TARGET.exists():
    raise ImportError(f"Tokenizer config file not found: {_TARGET}")

_spec = importlib.util.spec_from_file_location("east_african_tokenizer_config", _TARGET)
_mod = importlib.util.module_from_spec(_spec)
assert _spec.loader is not None
_spec.loader.exec_module(_mod)

# Re-export the public surface
LanguageTokenizerConfig = _mod.LanguageTokenizerConfig
TOKENIZER_CONFIGS = _mod.TOKENIZER_CONFIGS
get_tokenizer_config = _mod.get_tokenizer_config
list_available_configs = _mod.list_available_configs
get_family_configs = _mod.get_family_configs
get_tier_1_configs = _mod.get_tier_1_configs
get_tier_2_configs = _mod.get_tier_2_configs
print_config_summary = _mod.print_config_summary
create_tokenizer_training_config = _mod.create_tokenizer_training_config

# Individual configs (handy for one-off scripts)
SWAHILI_CONFIG = _mod.SWAHILI_CONFIG
KIKUYU_CONFIG = _mod.KIKUYU_CONFIG
LUGANDA_CONFIG = _mod.LUGANDA_CONFIG
KINYARWANDA_CONFIG = _mod.KINYARWANDA_CONFIG

__all__ = [
    "LanguageTokenizerConfig",
    "TOKENIZER_CONFIGS",
    "get_tokenizer_config",
    "list_available_configs",
    "get_family_configs",
    "get_tier_1_configs",
    "get_tier_2_configs",
    "print_config_summary",
    "create_tokenizer_training_config",
    "SWAHILI_CONFIG",
    "KIKUYU_CONFIG",
    "LUGANDA_CONFIG",
    "KINYARWANDA_CONFIG",
]
