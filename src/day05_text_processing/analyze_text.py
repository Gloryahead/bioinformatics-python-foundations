"""Simple text analysis utilities.

This module provides functions to read a text file, count lines and
words, and determine the most common word. Functions are defensive
about missing files and handle punctuation/casing so results are
more useful for natural-language text.
"""

from pathlib import Path
from string import punctuation
from collections import Counter
from typing import Union


def read_text(file_path: Union[str, Path]) -> str:
    """Read and return the contents of ``file_path`` as a string.

    If the file does not exist, a message is printed and an empty
    string is returned. Accepts either a string path or a ``Path``.
    """
    try:
        path = Path(file_path)
        if not path.exists():
            raise FileNotFoundError(f"The file {path} does not exist.")
        with path.open("r", encoding="utf-8") as file:
            return file.read()
    except FileNotFoundError as e:
        # Inform the caller but return a safe empty string to keep
        # downstream functions simple (they can handle empty text).
        print(e)
        return ""


def count_lines(text: str) -> int:
    """Return the number of lines in ``text``.

    Uses ``str.splitlines()`` which correctly handles various newline
    conventions (\n, \r\n, etc.).
    """
    return len(text.splitlines())


def count_words(text: str) -> int:
    """Return the total count of words in ``text``.

    Splits on whitespace, strips surrounding punctuation from each token,
    and lowercases tokens so that "Word" and "word" are counted as one.
    """
    frequency = {}
    words = text.split()
    for word in words:
        # Remove leading/trailing punctuation and normalize case.
        cleaned = word.strip(punctuation).lower()
        if cleaned:
            frequency[cleaned] = frequency.get(
                cleaned, 0) + 1
    # Sum of frequencies equals the number of recognized words.
    return sum(frequency.values())


def most_common_word(text: str) -> str:
    """Return the most common word in ``text`` or an empty string.

    Cleans tokens similarly to ``count_words`` and uses
    ``collections.Counter`` to find the most frequent token. Returns
    an empty string when no words are present.
    """
    words = text.split()
    cleaned_words = [word.strip(punctuation).lower()
                     for word in words if word.strip(punctuation)]
    if not cleaned_words:
        return ""
    word_counts = Counter(cleaned_words)
    most_common = word_counts.most_common(1)[0][0]
    return most_common


def main() -> None:
    """Interactive entry point: prompt for a path and print metrics."""

    # Prompt the user for a path and accept either a string or Path.
    file_path = Path(input("Enter the path to the text file: "))
    text = read_text(file_path)

    # Print simple textual statistics; helper functions handle empty text.
    print(f"Lines: {count_lines(text)}")
    print(f"Words: {count_words(text)}")
    print(f"Most common word: {most_common_word(text)}")


if __name__ == "__main__":
    main()
