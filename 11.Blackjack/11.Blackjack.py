############### Our Blackjack House Rules #####################

## The deck is unlimited in size.
## There are no jokers.
## The Jack/Queen/King all count as 10.
## The the Ace can count as 11 or 1.
## Use the following list as the deck of cards:
## cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
## The cards in the list have equal probability of being drawn.
## Cards are not removed from the deck as they are drawn.
## The computer is the dealer.

import random
from art import logo

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]


def blackjack():
    your_cards = []
    comp_cards = []
    user_score = 0
    comp_score = 0
    user_blackjack = False
    user_winner = False
    computer_winner = False
    print(logo)

    def score():
        print(f"Your cards: {your_cards}, current score: {user_score}")
        print(f"Computer's first card: {comp_cards[0]}")

    def final_score():
        print(f"Your final cards: {your_cards}, and final score: {user_score}")
        print(f"Computer's final cards: {comp_cards} and his final score: {comp_score}")

    for card in range(2):
        your_cards.append(random.choice(cards))
        comp_cards.append(random.choice(cards))
    user_score = sum(your_cards)
    comp_score = sum(comp_cards)
    score()
    if 11 in your_cards and 10 in your_cards:
        user_blackjack = True
    if 11 in comp_cards and 10 in comp_cards:
        computer_winner = True
        print("Computer win!\nComputer got a Blackjack!")
    elif user_blackjack:
        user_winner = True
        print("You win!\nYou got a Blackjack !")
    if user_score > 21:
        computer_winner = True
        print("You lose!\nYour score is greater than 21.")
    while not computer_winner and not user_winner:
        another_card = input('Do you want do get another card ? Type "y" or "n".')
        if another_card == "y":
            new_card = random.choice(cards)
            your_cards.append(new_card)
            user_score = sum(your_cards)
            if new_card == 11 and user_score > 21:
                user_score - 10
            score()
            if user_score > 21:
                computer_winner = True
                print("You lose.\nYour score is greater than 21.")
        elif another_card == "n":
            while not comp_score > 16:
                new_comp_card = random.choice(cards)
                comp_cards.append(new_comp_card)
                comp_score = sum(comp_cards)
                if new_comp_card == 11 and comp_score > 21:
                    comp_score - 10
            if comp_score > 21:
                user_winner = True
                print("You win!")
            elif user_score == comp_score:
                user_winner = True
                print("It's a draw.")
            elif user_score > comp_score:
                user_winner = True
                print("You win!")
            else:
                computer_winner = True
                print("Computer win!")
    final_score()
    start()


def start():
    want_play = input('Do you want to play a game of Blackjack? Type "y" or "n".')
    if want_play == "y":
        print("\033[2J\033[1;1H")
        blackjack()
    else:
        print("Have a nice day!")


start()
