import random

EASY_DIFFICULTY = 10
HARD_DIFFICULTY = 5


def difficulty():
    """Nastaví počet životov"""
    diff = input('Choose the difficulty. Type "easy" or "hard"')
    if diff == "easy":
        return EASY_DIFFICULTY
    return HARD_DIFFICULTY


def check_number(actual_number, guessed_number, turns):
    """Skontroluje, či je hádané číslo správne a zaznamená skóre."""
    if guessed_number > actual_number:
        print("Too high.")
        return turns - 1
    if guessed_number < actual_number:
        print("Too low.")
        return turns - 1
    print(f"You got it! The answer was {actual_number}")
    return


def game():
    """Hlavná hra"""
    print("Welcome to the number guessing game!")
    print("I'm thinking about a number between 1 and 100.")
    actual_number = random.randint(1, 101)
    turns = difficulty()
    guessed_number = 0
    while guessed_number != actual_number:
        print(f"You have {turns} number of guesses.")
        guessed_number = int(input("Guess a number: "))
        turns = check_number(actual_number, guessed_number, turns)
        if turns == 0:
            print("You have run out of guesses, you loose.")
            return
        elif guessed_number != actual_number:
            print("Guess again.")


game()
