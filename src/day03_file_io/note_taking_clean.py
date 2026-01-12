"""A minimal, clean note-taking CLI.

This script stores notes in a file named ``notes.txt`` located in the
same directory as this script. It provides two simple operations:
- add a note (appends a line to the file)
- view notes (prints numbered lines)

The implementation focuses on clarity and robust, user-friendly I/O
and error messages.
"""

from pathlib import Path


# Default storage file: "notes.txt" next to this script.
NOTES_FILE = Path(__file__).with_name("notes.txt")


def add_note(file_path: Path) -> None:
    """Prompt for a single-line note and append it to ``file_path``.

    - Trims surrounding whitespace from the user's input.
    - Skips saving when the user submits an empty note.
    - Ensures the parent directory exists before writing.
    - Catches and reports file system errors (permissions, disk full, etc.).
    """

    # Prompt the user and remove accidental leading/trailing whitespace.
    note = input("Enter a note: ").strip()

    # If the user didn't enter anything, inform and exit early.
    if not note:
        print("No note entered. Nothing saved.")
        return

    try:
        # Create parent directories if they don't exist (no-op otherwise).
        file_path.parent.mkdir(parents=True, exist_ok=True)

        # Open the file in append mode and write the note with a newline.
        with file_path.open("a", encoding="utf-8") as f:
            f.write(note + "\n")

        # Let the user know the write succeeded.
        print("Note saved.")
    except OSError as e:
        # Provide an informative error message for common I/O failures.
        print(f"Error: could not write to {file_path}: {e}")


def view_notes(file_path: Path) -> None:
    """Read and print all notes from ``file_path``, numbered.

    - If the file doesn't exist or is empty, prints a friendly message.
    - Uses ``rstrip('\n')`` to avoid printing extra blank lines.
    - Catches and reports unexpected I/O errors.
    """

    # If there's no file yet, the user has no notes saved.
    if not file_path.exists():
        print("No notes yet.")
        return

    try:
        # Read all lines and strip trailing newlines for neat printing.
        with file_path.open("r", encoding="utf-8") as f:
            lines = [line.rstrip("\n") for line in f]

        # If the file is empty, tell the user rather than printing nothing.
        if not lines:
            print("No notes yet.")
            return

        # Print each saved note preceded by a line number.
        for i, line in enumerate(lines, start=1):
            print(f"{i}. {line}")
    except OSError as e:
        print(f"Error: could not read {file_path}: {e}")


def main() -> None:
    """Interactive command loop for adding and viewing notes.

    Presents a small menu and loops until the user chooses to exit.
    Input is read as strings and validated via explicit comparisons.
    """

    while True:
        # Display the menu options each loop iteration.
        print("\n1. Add a note")
        print("2. View notes")
        print("3. Exit")

        # Read the user's choice and trim whitespace.
        choice = input("Choose an option (1-3): ").strip()

        # Route the chosen command to the corresponding handler.
        if choice == "1":
            add_note(NOTES_FILE)
        elif choice == "2":
            view_notes(NOTES_FILE)
        elif choice == "3":
            print("Goodbye.")
            break
        else:
            # Helpful guidance when input is not recognized.
            print("Invalid choice. Please enter 1, 2, or 3.")


if __name__ == "__main__":
    main()
