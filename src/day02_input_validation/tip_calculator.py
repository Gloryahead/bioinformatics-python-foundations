"""Small calculator to split a bill with tip among people.

This module prompts the user for a bill amount, tip percentage,
and number of people, then prints how much each person should pay.
The code below adds clear input validation and separates pure
computation from I/O so it's easier to read and test.
"""

from typing import Tuple


def prompt_float(bill: str, tip_percent: str) -> Tuple[float, float]:
    """Prompt for bill and tip percentage and return them as floats.

    This will repeatedly prompt until valid numeric input is provided
    and basic bounds are satisfied (bill > 0, tip_percent >= 0).
    """
    while True:
        try:
            # Prompt for the bill amount and convert to float.
            user_input_bill = input(bill)
            value_bill = float(user_input_bill)

            # Prompt for the tip percentage and convert to float.
            user_input_tip_percent = input(tip_percent)
            value_tip_percent = float(user_input_tip_percent)

            # Validate sensible bounds for bill and tip.
            if value_bill <= 0:
                print("Error: Please enter a bill greater than 0.")
                continue
            if value_tip_percent < 0:
                print("Error: Please enter a tip greater than or equal to 0.")
                continue

            # Valid inputs — return as a tuple of floats.
            return value_bill, value_tip_percent
        except ValueError:
            # Non-numeric input — ask again.
            print("Error: Invalid input. Please enter a valid number.")


def prompt_int(people: str) -> int:
    """Prompt for the number of people and return it as an int.

    Accepts whole-number input (e.g. "2"). Ensures value >= 1.
    Keeps prompting until a valid integer >= 1 is provided.
    """
    while True:
        try:
            user_input = input(people)
            value = int(user_input)

            # Ensure at least one person.
            if value < 1:
                print("Error: Please enter a whole number greater than or equal to 1.")
                continue

            return int(value)
        except ValueError:
            print("Error: Invalid input. Please enter a valid number.")


def compute_per_person(bill: float, tip_percent: float, people: int) -> float:
    """Pure function: compute how much each person should pay.

    Args:
        bill: Total bill amount (must be > 0).
        tip_percent: Tip percentage (>= 0).
        people: Number of people splitting the bill (>= 1).

    Returns:
        Amount each person should pay (float).
    """
    tip_amount = bill * (tip_percent / 100)
    total = bill + tip_amount
    return total / people


def calculate_per_person(bill: str, tip_percent: str, people: str) -> str:
    """Prompt the user and return a formatted string with the result.

    This wrapper handles prompting (I/O) separately from the pure
    computation in `compute_per_person`.
    """
    bill_value, tip_value = prompt_float(bill, tip_percent)
    people_value = prompt_int(people)

    per_person = compute_per_person(bill_value, tip_value, people_value)

    # Format to two decimal places for currency-like output.
    return f"Each person should pay: {per_person:.2f}"


if __name__ == "__main__":
    bill = "What is the total bill? $"
    tip_percent = "What percentage would you like to tip? "
    people = "How many people to split the bill? "
    print(calculate_per_person(bill, tip_percent, people))
