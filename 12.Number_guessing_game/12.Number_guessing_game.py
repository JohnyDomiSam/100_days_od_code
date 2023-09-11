# Number Guessing Game Objectives:

# Include an ASCII art logo.
# Allow the player to submit a guess for a number between 1 and 100.
# Check user's guess against actual answer. Print "Too high." or "Too low." depending on the user's answer.
# If they got the answer correct, show the actual answer to the player.
# Track the number of turns remaining.
# If they run out of turns, provide feedback to the player.
# Include two different difficulty levels (e.g., 10 guesses in easy mode, only 5 guesses in hard mode).
import random

print(
    """

 _        _______ _________ _  _______    _______           _______  _______  _______ 
( \      (  ____ \\__   __/( )(  ____ \  (  ____ \|\     /|(  ____ \(  ____ \(  ____ \
| (      | (    \/   ) (   |/ | (    \/  | (    \/| )   ( || (    \/| (    \/| (    \/
| |      | (__       | |      | (_____   | |      | |   | || (__    | (_____ | (_____ 
| |      |  __)      | |      (_____  )  | | ____ | |   | ||  __)   (_____  )(_____  )
| |      | (         | |            ) |  | | \_  )| |   | || (            ) |      ) |
| (____/\| (____/\   | |      /\____) |  | (___) || (___) || (____/\/\____) |/\____) |
(_______/(_______/   )_(      \_______)  (_______)(_______)(_______/\_______)\_______)
                                                                                    

"""
)
winner = False
actuall_number = random.randint(1, 101)
print(f"Pssst, the correct answer is {actuall_number}")
difficulty = input(
    "Welcome to the Number Guessing Game!\nI'm thinking of a number between 1 and 100.\nChoose a difficulty. Type 'easy' or 'hard': "
)
if difficulty == "easy":
    print("You have 10 attempts remaining to finish the game")
    attempts = 10
elif difficulty == "hard":
    print("You have 5 attempts remaining to guess the number.")
    attempts = 5

while attempts > 0 and not winner:
    guessed_number = int(input("Make a guess: "))
    if guessed_number > actuall_number:
        print("Too high.")
        attempts -= 1
        print(f"You have {attempts} lives remaining.")
    elif guessed_number < actuall_number:
        print("Too low.")
        attempts -= 1
        print(f"You have {attempts} lives remaining.")
    else:
        winner = True
        print(f"You got it! The answer was {actuall_number}")

if attempts == 0:
    print("You've run out of guesses, you lose.")
