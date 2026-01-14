from pathlib import Path
from string import punctuation
from collections import Counter


def read_text(file_path: Path) -> str:
    """Read and return file contents as text."""
    with file_path.open("r", encoding="utf-8") as f:
        return f.read()


def normalize_words(text: str) -> list[str]:
    """Split text into lowercase words with punctuation removed."""
    words = []
    for token in text.split():
        w = token.strip(punctuation).lower()
        if w:
            words.append(w)
    return words


def count_lines(text: str) -> int:
    """Count lines in text."""
    return len(text.splitlines())


def count_words(text: str) -> int:
    """Count words (case-insensitive, punctuation ignored)."""
    return len(normalize_words(text))


def most_common_word(text: str) -> str:
    """Return most common normalized word, or empty string if none."""
    words = normalize_words(text)
    if not words:
        return ""
    return Counter(words).most_common(1)[0][0]


def main() -> None:
    file_path = Path(input("Enter the path to the text file: ").strip())

    if not file_path.exists():
        print(f"Error: file not found: {file_path}")
        return

    text = read_text(file_path)

    print(f"Lines: {count_lines(text)}")
    print(f"Words: {count_words(text)}")

    common = most_common_word(text)
    print(f"Most common word: {common if common else '(none)'}")


if __name__ == "__main__":
    main()

