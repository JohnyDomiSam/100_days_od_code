rock = """
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
"""

paper = """
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
"""

scissors = """
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
"""

# Write your code below this line 👇
import random

znaky = ["rock", "paper", "scissors"]
nahodny_vyber = random.randint(0, 2)
volbaPC = znaky[nahodny_vyber]

volba = input("What do you choose? Type 0 for rock, 1 for Paper and 2 for Scissors.\n ")
if volba == "0":
    print(rock)
elif volba == "1":
    print(paper)
elif volba == "2":
    print(scissors)

print("Computer choose:")
if volba == "0":
    if volbaPC == "rock":
        print(rock + "Draw. Play again.")
    elif volbaPC == "paper":
        print(paper + "You loose.")
    else:
        print(scissors + "You win!")
elif volba == "1":
    if volbaPC == "rock":
        print(rock + "You win!")
    elif volbaPC == "paper":
        print(paper + "Draw. Play again.")
    else:
        print(scissors + "You loose")
elif volba == "2":
    if volbaPC == "rock":
        print(rock + "You loose.")
    elif volbaPC == "paper":
        print(paper + "You win!")
    else:
        print(scissors + "Draw. Play again.")
input("Press ENTER to exit.")
