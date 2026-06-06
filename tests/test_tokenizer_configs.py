"""
Tests for the East-African tokenizer config registry.

These tests do NOT need torch / datasets / whisper - they are pure logic over
the dataclass definitions.  Run with `pytest tests/`.
"""

import pytest

from ml.east_african_tokenizer_compat import (
    TOKENIZER_CONFIGS,
    get_tokenizer_config,
    list_available_configs,
    get_tier_1_configs,
    get_tier_2_configs,
    get_family_configs,
    LanguageTokenizerConfig,
    SWAHILI_CONFIG,
    KIKUYU_CONFIG,
    LUGANDA_CONFIG,
)


def test_registry_has_expected_minimum_languages():
    """We should have at least 10 languages in the registry."""
    assert len(TOKENIZER_CONFIGS) >= 10, f"Only {len(TOKENIZER_CONFIGS)} languages registered"


def test_swahili_in_registry():
    assert "swa" in TOKENIZER_CONFIGS
    assert TOKENIZER_CONFIGS["swa"] is SWAHILI_CONFIG


def test_get_tokenizer_config_returns_dataclass():
    cfg = get_tokenizer_config("swa")
    assert isinstance(cfg, LanguageTokenizerConfig)
    assert cfg.language_code == "swa"
    assert cfg.language_name == "Swahili"


def test_get_tokenizer_config_unknown_raises():
    with pytest.raises(KeyError):
        get_tokenizer_config("zzz")


def test_list_available_configs():
    listing = list_available_configs()
    assert isinstance(listing, dict)
    assert "swa" in listing
    assert listing["swa"] == "Swahili"


def test_tier_1_languages_are_present():
    tier_1 = get_tier_1_configs()
    codes = {c.language_code for c in tier_1}
    # Swahili must be in tier 1
    assert "swa" in codes


def test_tier_2_languages_are_present():
    tier_2 = get_tier_2_configs()
    codes = {c.language_code for c in tier_2}
    assert len(codes) >= 1


def test_family_configs_lookup():
    """All Bantu configs should be retrievable by family."""
    thagicu = get_family_configs("Thagicu Bantu")
    assert any(c.language_code == "kik" for c in thagicu)


def test_swahili_has_prenasalized_consonants():
    """Swahili is a Bantu language; prenasalized consonants are part of phonology."""
    assert len(SWAHILI_CONFIG.prenasalized) >= 3
    assert "mb" in SWAHILI_CONFIG.prenasalized
    assert "nd" in SWAHILI_CONFIG.prenasalized


def test_luganda_tone_aware():
    """Luganda is tone-marked in standard orthography."""
    assert LUGANDA_CONFIG.tone_aware is True
    assert len(LUGANDA_CONFIG.tone_marks) > 0


def test_kikuyu_has_prefixes():
    """Bantu languages are agglutinative with rich nominal prefix systems."""
    assert len(KIKUYU_CONFIG.prefixes) >= 3


def test_vocab_sizes_are_positive():
    for code, cfg in TOKENIZER_CONFIGS.items():
        assert cfg.vocab_size > 0, f"{code} has non-positive vocab_size"


def test_all_configs_have_required_fields():
    """Smoke-test every config has the required fields populated."""
    for code, cfg in TOKENIZER_CONFIGS.items():
        assert cfg.language_code == code
        assert isinstance(cfg.language_name, str) and len(cfg.language_name) > 0
        assert isinstance(cfg.family, str) and len(cfg.family) > 0
        assert isinstance(cfg.vowels, str) and len(cfg.vowels) > 0
        assert isinstance(cfg.consonants, str) and len(cfg.consonants) > 0


def test_create_tokenizer_training_config():
    from ml.east_african_tokenizer_compat import create_tokenizer_training_config
    cfg = create_tokenizer_training_config("swa", output_dir="/tmp/tokenizer")
    assert cfg["language"]["language_code"] == "swa"
    assert cfg["vocab_size"] == SWAHILI_CONFIG.vocab_size
    assert "language_specific_tokens" in cfg
    # Should include the prenasalized consonants
    assert "mb" in cfg["language_specific_tokens"]
    assert "nd" in cfg["language_specific_tokens"]


def test_to_dict_round_trip():
    d = SWAHILI_CONFIG.to_dict()
    assert d["language_code"] == "swa"
    assert d["vocab_size"] == SWAHILI_CONFIG.vocab_size
    assert "tone_aware" in d
    assert d["tone_aware"] == SWAHILI_CONFIG.tone_aware
