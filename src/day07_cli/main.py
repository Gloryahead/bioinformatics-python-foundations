"""
Main script for text analysis.
Prompts user for a file path and displays text statistics.
"""

import argparse
from pathlib import Path
from text_utils import read_text, count_lines, count_words, most_common_word


def parse_args() -> argparse.Namespace:
    """Parse command-line arguments for the script.

    Provides flags: --file/-f, --lines, --words, --common. If no stat
    flags are provided the script prints all statistics.
    """
    parser = argparse.ArgumentParser(
        description="Analyze text file and display statistics.")
    parser.add_argument("--file", "-f", dest="file_path", type=Path,
                        required=True, help="Path to the text file to analyze.")
    parser.add_argument("--lines", action="store_true",
                        help="Print number of lines.")
    parser.add_argument("--words", action="store_true",
                        help="Print number of words.")
    parser.add_argument("--common", action="store_true",
                        help="Print most common word.")

    return parser.parse_args()


def main() -> None:
    """Entry point: parse args and print text metrics."""
    args = parse_args()
    file_path = args.file_path
    # If no specific stat flags provided, print all
    want_lines = args.lines
    want_words = args.words
    want_common = args.common
    if not (want_lines or want_words or want_common):
        want_lines = want_words = want_common = True

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

    if want_lines:
        print(f"Lines: {count_lines(text)}")
    if want_words:
        print(f"Words: {count_words(text)}")
    if want_common:
        common = most_common_word(text)
        print(f"Most common word: {common if common else '(none)'}")


if __name__ == "__main__":
    main()
