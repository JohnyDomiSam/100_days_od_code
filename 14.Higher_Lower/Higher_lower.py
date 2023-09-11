from art import logo
from art import vs
from game_data import data
from random import randint


def acompare(a):
    """Vytlačí f string porovnania a uloží počet followerov ako output."""
    afollowers = data[a]["follower_count"]
    print(
        f'Compare A: {data[a]["name"]}, a  {data[a]["description"]}, from {data[a]["country"]}.'
    )
    return afollowers


def bcompare(b):
    """Vytlačí f string porovnania a uloží počet followerov ako output."""
    bfollowers = data[b]["follower_count"]
    print(
        f'Against B: {data[b]["name"]}, a  {data[b]["description"]}, from {data[b]["country"]}.'
    )
    return bfollowers


def compare(afoll, bfoll, guess):
    """Porovnaj počty followerov a odpoveď."""
    if afoll > bfoll and guess == "a":
        return True
    elif bfoll > afoll and guess == "b":
        return True
    return False


def game():
    """Hlavná hra"""
    answer = True
    score = 0
    a = randint(0, (len(data) - 1))
    b = randint(0, (len(data) - 1))
    print(logo)
    while answer:
        afoll = acompare(a)
        print(vs)
        bfoll = bcompare(b)
        while a == b:
            b = randint(0, (len(data) - 1))

        guess = input("Who has more followers? Type 'A' or 'B':").lower()
        answer = compare(afoll, bfoll, guess)
        if not answer:
            print("\033[2J\033[1;1H")
            print(f"Wrong answer. Your final score is {score}.")
        else:
            score += 1
            print("\033[2J\033[1;1H")
            print(logo)
            print(f"You are right, your score is {score}.")
            a = b
            b = randint(0, (len(data) - 1))


game()
