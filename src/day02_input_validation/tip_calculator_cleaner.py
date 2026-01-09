"""Small calculator to split a bill with tip among people.

Prompts the user for a bill amount, tip percentage, and number of people,
then prints how much each person should pay. Includes input validation and
separates pure computation from I/O.
"""

from __future__ import annotations


def prompt_float(prompt: str, *, min_value: float) -> float:
    """Prompt for a float until the user enters a valid number >= min_value."""
    while True:
        raw = input(prompt).strip()
        try:
            value = float(raw)
        except ValueError:
            print("Error: Please enter a valid number.")
            continue

        if value < min_value:
            print(f"Error: Value must be at least {min_value}.")
            continue

        return value


def prompt_int(prompt: str, *, min_value: int) -> int:
    """Prompt for an int until the user enters a valid integer >= min_value."""
    while True:
        raw = input(prompt).strip()
        try:
            value = int(raw)
        except ValueError:
            print("Error: Please enter a whole number.")
            continue

        if value < min_value:
            print(f"Error: Value must be at least {min_value}.")
            continue

        return value


def compute_per_person(bill: float, tip_percent: float, people: int) -> float:
    """Compute how much each person should pay."""
    tip_amount = bill * (tip_percent / 100.0)
    total = bill + tip_amount
    return total / people


def main() -> None:
    bill = prompt_float("What is the total bill? $", min_value=0.01)
    tip_percent = prompt_float("What percentage would you like to tip? ", min_value=0.0)
    people = prompt_int("How many people to split the bill? ", min_value=1)

    per_person = compute_per_person(bill, tip_percent, people)
    print(f"Each person should pay: ${per_person:.2f}")


if __name__ == "__main__":
    main()

