import sys
import argparse
from datetime import datetime


def build_message(name: str) -> str:
    """Build and return a multi-line message for the given ``name``.

    The message contains three lines:
    - a friendly greeting using the provided name;
    - the Python interpreter version (first token of ``sys.version``);
    - the current local time formatted as YYYY-MM-DD HH:MM:SS.
    """

    # Create a one-line greeting using the provided name.
    greeting = f"Hello, {name}!"

    # Extract the Python version string (e.g. '3.11.4').
    python_version = f"Python version: {sys.version.split()[0]}"

    # Format the current local time for human readers.
    current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    # Join the parts into a single string with newline separators.
    return "\n".join([greeting, python_version, f"Current time: {current_time}"])


def main(argv=None) -> None:
    """Parse CLI args and print the composed message.

    Args:
        argv: Optional list of arguments for testing (defaults to sys.argv[1:]).
    """

    # Set up a small argument parser with a helpful default for `--name`.
    parser = argparse.ArgumentParser(
        description="Simple greeting CLI",
        formatter_class=argparse.ArgumentDefaultsHelpFormatter,
    )
    parser.add_argument("--name", "-n", default="World", help="Name to greet")

    # Parse the provided arguments (or the real CLI args when None).
    args = parser.parse_args(argv)

    # Build and print the message to stdout.
    print(build_message(args.name))


if __name__ == "__main__":
    main()
