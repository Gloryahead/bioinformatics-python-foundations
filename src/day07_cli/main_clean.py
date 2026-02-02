import argparse
from pathlib import Path
from text_utils import read_text, count_lines, count_words, most_common_word


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Analyze a text file and display statistics.")
    parser.add_argument(
        "--file", "-f",
        dest="file_path",
        type=Path,
        required=True,
        help="Path to the text file to analyze.",
    )
    parser.add_argument("--lines", action="store_true", help="Print number of lines.")
    parser.add_argument("--words", action="store_true", help="Print number of words.")
    parser.add_argument("--common", action="store_true", help="Print most common word.")

    args = parser.parse_args()

    if not args.file_path.exists():
        parser.error(f"File not found: {args.file_path}")
    if not args.file_path.is_file():
        parser.error(f"Not a file: {args.file_path}")

    return args


def main() -> None:
    args = parse_args()

    want_lines = args.lines
    want_words = args.words
    want_common = args.common
    if not (want_lines or want_words or want_common):
        want_lines = want_words = want_common = True

    try:
        text = read_text(args.file_path)
    except PermissionError:
        print(f"Error: Permission denied when trying to read '{args.file_path}'.")
        return
    except OSError as e:
        print(f"Error: Could not read '{args.file_path}': {e}")
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

