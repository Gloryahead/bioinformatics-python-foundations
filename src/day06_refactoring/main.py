"""
Main script for text analysis.
Prompts user for a file path and displays text statistics.
"""

from pathlib import Path
from text_utils import read_text, count_lines, count_words, most_common_word


def main() -> None:
    """Interactive entry point: prompt for a path and print metrics."""
    file_path = Path(input("Enter the path to the text file: ").strip())

    if not file_path.exists():
        print(f"Error: The path '{file_path}' does not exist.")
        return
    if not file_path.is_file():
        print(f"Error: The path '{file_path}' is not a file.")
        return

    try:
        text = read_text(file_path)
    except PermissionError:
        print(f"Error: Permission denied when trying to read '{file_path}'.")
        return
    except OSError as e:
        print(f"Error: Could not read '{file_path}': {e}")
        return

    print(f"Lines: {count_lines(text)}")
    print(f"Words: {count_words(text)}")

    common = most_common_word(text)
    print(f"Most common word: {common if common else '(none)'}")


if __name__ == "__main__":
    main()
