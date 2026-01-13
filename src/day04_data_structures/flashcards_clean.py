"""Interactive flashcard quiz utility.

Stores a set of question->answer pairs and quizzes the user by selecting
random cards without replacement. Comparison is case-insensitive and
whitespace is trimmed.
"""

import random


FLASHCARDS: dict[str, str] = {
    "What is Python?": "A programming language",
    "What is a dictionary?": "A key-value data structure",
    "What does FASTA store?": "Biological sequences",
    "What does CSV stand for?": "Comma-Separated Values",
    "What is reproducibility?": "Ability to rerun analysis with same results",
}


def ask_question(question: str, answer: str) -> bool:
    """Ask one question and return True if the user's answer matches."""
    user_answer = input(f"{question} ").strip().lower()
    expected = answer.strip().lower()

    if user_answer == expected:
        print("Correct!\n")
        return True

    print(f"Incorrect. The correct answer is: {answer}\n")
    return False


def run_quiz(cards: dict[str, str], max_questions: int = 5) -> None:
    """Run a quiz using up to `max_questions` randomly selected cards."""
    if not cards:
        print("No flashcards available.")
        return

    num_questions = min(max_questions, len(cards))
    selected = random.sample(list(cards.items()), k=num_questions)

    score = 0
    for question, answer in selected:
        score += int(ask_question(question, answer))

    print(f"Score: {score} / {num_questions}")


def main() -> None:
    run_quiz(FLASHCARDS)


if __name__ == "__main__":
    main()
