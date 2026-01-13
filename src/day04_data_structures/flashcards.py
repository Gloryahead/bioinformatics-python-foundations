"""Interactive flashcard quiz utility.

This small script stores a set of question->answer pairs and quizzes
the user by selecting random cards without replacement. Comparison is
case-insensitive and whitespace is trimmed so small typing differences
don't cause incorrect scoring.
"""

import random


# A simple in-memory set of flashcards (question -> answer).
FLASHCARDS: dict[str, str] = {
    "What is Python?": "A programming language",
    "What is a dictionary?": "A key-value data structure",
    "What does FASTA store?": "Biological sequences",
    "What does CSV stand for?": "Comma-Separated Values",
    "What is reproducibility?": "Ability to rerun analysis with same results",
}


def ask_question(question: str, answer: str) -> bool:
    """Ask a single question and return True when the user is correct.

    Comparison is case-insensitive and trims surrounding whitespace.
    If the user is incorrect, the correct answer is shown.
    """

    # Prompt the user and normalize both answers for comparison.
    # Using `strip()` removes accidental leading/trailing spaces the user
    # might type; `lower()` makes comparison case-insensitive.
    user_answer = input(f"{question} ")
    if user_answer.strip().lower() == answer.strip().lower():
        print("Correct!")
        return True

    # Provide feedback and the correct answer when wrong.
    print(f"Incorrect. The correct answer is: {answer}")
    return False


def run_quiz(cards: dict[str, str], max_questions: int = 5) -> None:
    """Run a short quiz using the provided `cards`.

    - Selects up to `max_questions` distinct questions at random.
    - Calls `ask_question` for each and tallies a score.
    - Prints a final score summary.
    """

    if not cards:
        print("No flashcards available.")
        return

    # Determine how many questions to ask (no more than available cards).
    num_questions = min(max_questions, len(cards))

    # `random.sample` selects distinct items (no replacement), so the user
    # won't see the same question twice in a single quiz session.
    questions = random.sample(list(cards.items()), k=num_questions)

    score = 0
    for question, answer in questions:
        # Each call returns True when the user answers correctly.
        if ask_question(question, answer):
            score += 1

    # Summarize the user's performance at the end of the quiz.
    print(f"Quiz complete! Your score: {score}/{num_questions}")


def main() -> None:
    """Main entry point: run the flashcard quiz with the default cards.

    Keep `main()` small so the module can be imported and the quiz
    functions reused or unit-tested independently.
    """

    run_quiz(FLASHCARDS)


if __name__ == "__main__":
    main()
