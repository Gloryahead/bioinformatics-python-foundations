"""Simple notes utility.

This module appends a user-provided note to a file and then prints
all notes with line numbers. Paths default to a file named
"file.txt" in the user's home directory.
"""

from pathlib import Path

# Default file used to store notes (~/file.txt). Change as needed.
FILE_PATH = Path.home() / "file.txt"


def add_note(file_path: Path) -> None:
    """Prompt the user for a note and append it to ``file_path``.

    The function appends a newline after the note so each entry is on
    its own line. I/O errors are caught and reported to the user.
    """

    # Read a single line of input from the user.
    note = input("Enter a note to append: ")
    note_new_line = note + "\n"

    try:
        # Open the target file in append mode and write the note.
        with open(file_path, "a", encoding="utf-8") as file:
            file.write(note_new_line)

        # Confirm success to the user with the actual path used.
        print(f"Note was successfully appended to '{file_path}'")

    except IOError as e:
        # Report common file I/O errors (permission issues, disk full, etc.).
        print(f"An error has occurred: {e}")


def read_notes(file_path: Path) -> None:
    """Read and print all notes from ``file_path`` with line numbers.

    Handles the case where the file does not exist and reports other
    unexpected errors.
    """

    try:
        # Open the file for reading and enumerate each line for numbering.
        with open(file_path, "r", encoding="utf-8") as file:
            for number, line in enumerate(file, start=1):
                # rstrip removes the trailing newline for clean printing.
                print(f"{number}. {line.rstrip()}")
    except FileNotFoundError:
        # Informative message when the file hasn't been created yet.
        print(f"Error: The file '{file_path}' was not found!")
    except Exception as e:
        # Catch-all for other unexpected exceptions during read.
        print(f"An error has occurred: {e}")


def main() -> None:
    """Main entry point: append a note, then display all notes."""

    # First, prompt the user to add a note; then display the file contents.
    add_note(FILE_PATH)
    read_notes(FILE_PATH)


if __name__ == "__main__":
    main()
