"""
Tests for the data acquisition script.

The acquisition script has three paths: cache, network, builtin.  We test the
cache and builtin paths (the network path is skipped in CI because the test
runner may not have outbound access).
"""

import json
from pathlib import Path

import pytest

from ml.data_acquisition import acquire, BUILTIN_SWAHILI_SAMPLE, _clean_text


def test_clean_text_strips_markdown():
    raw = """---
title: Test
---

# Heading

This is **bold** and *italic* text with [a link](http://x.com).
```code block```

> blockquote

[1] In the beginning [2] was the Word.
{1:1} Some text.
"""
    cleaned = _clean_text(raw)
    # Frontmatter gone
    assert "title" not in cleaned
    # Headings gone
    assert "Heading" not in cleaned
    # Code blocks gone
    assert "code block" not in cleaned
    # Bracketed verse markers gone
    assert "[1]" not in cleaned
    assert "{1:1}" not in cleaned
    # Link text preserved
    assert "a link" in cleaned
    # Bold/italic markers gone but text remains
    assert "bold" in cleaned
    assert "italic" in cleaned


def test_clean_text_handles_empty_input():
    assert _clean_text("") == ""
    assert _clean_text(None) == ""


def test_builtin_sample_is_swahili():
    """Smoke-test: the fallback corpus contains Swahili vocabulary."""
    sample = BUILTIN_SWAHILI_SAMPLE.lower()
    # A handful of very common Swahili words
    for word in ("na", "wa", "ya", "kwa", "mungu", "bwana", "ni"):
        assert word in sample, f"Expected Swahili word '{word}' in fallback corpus"


def test_acquire_writes_cache(tmp_path: Path):
    """The first call should write the corpus; second call should use the cache."""
    out = tmp_path / "sw.txt"
    manifest = acquire(out, max_chars=50_000)
    assert out.exists()
    assert manifest["characters"] > 1000
    # Re-running with the same path should hit the cache path
    manifest2 = acquire(out, max_chars=50_000)
    # Cache path: source is 'cache', bytes match exactly
    assert manifest2["source"] == "cache"
    assert manifest2["sha256_16"] == manifest["sha256_16"]


def test_acquire_truncates_to_max_chars(tmp_path: Path):
    out = tmp_path / "sw.txt"
    manifest = acquire(out, max_chars=2_000)
    assert manifest["characters"] <= 2_000


def test_acquire_manifest_fields(tmp_path: Path):
    out = tmp_path / "sw.txt"
    manifest = acquire(out, max_chars=50_000)
    # Required keys
    for key in ("path", "source", "characters", "words", "sentence_endings", "sha256_16"):
        assert key in manifest, f"Missing manifest key: {key}"
