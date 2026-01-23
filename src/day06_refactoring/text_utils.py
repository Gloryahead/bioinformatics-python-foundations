"""Text utilities for reading and analyzing plain text files.

Provides functions to:
- read text from a file
- count lines
- compute word frequencies (case-insensitive, punctuation trimmed)
- find the most common word
"""

from __future__ import annotations

from pathlib import Path
from string import punctuation


def read_text(file_path: Path) -> str:
    """Read the content of a text file and return it as a string.

    Raises:
        FileNotFoundError, PermissionError, OSError: if reading fails.
    """
    return file_path.read_text(encoding="utf-8")


def count_lines(text: str) -> int:
    """Count lines in the given text."""
    return len(text.splitlines())


def word_frequencies(text: str) -> dict[str, int]:
    """Return a frequency dictionary of normalized words in the text."""
    freq: dict[str, int] = {}
    for token in text.split():
        w = token.strip(punctuation).lower()
        if not w:
            continue
        freq[w] = freq.get(w, 0) + 1
    return freq


def count_words(text: str) -> int:
    """Count words in the text after normalization."""
    freq = word_frequencies(text)
    return sum(freq.values())


def most_common_word(text: str) -> str:
    """Return the most common word in the text, or empty string if none."""
    freq = word_frequencies(text)
    if not freq:
        return ""
    return max(freq, key=freq.get)
