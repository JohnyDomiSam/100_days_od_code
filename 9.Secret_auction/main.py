# from replit import clear
from art import logo

print(logo)

Other_bidders = True
bid_dict = {}


def auction(name, bid):
    bid_dict[name] = bid


while Other_bidders:
    name_inp = input("What is your name ?: ")
    bid_input = int(input("What is your bid ?: $"))
    auction(name=name_inp, bid=bid_input)
    inp_bidders = input('Are there any other bidders ? Reply "Yes" or "No".').lower()
    if inp_bidders == "yes":
        Other_bidders = True
        print("\033[2J\033[1;1H")
    elif inp_bidders == "no":
        max_value = max(bid_dict.values())
        winner = max(bid_dict, key=bid_dict.get)
        print(f"The winner is {winner} with a bid of {max_value}.")
        Other_bidders = False
