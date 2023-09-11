MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}

def check_beverage(user_input):
    """Skontroluje či je dostatok surovín a vráti bool."""
    if user_input == "espresso":
        water = MENU[user_input]["ingredients"]["water"]
        coffee = MENU[user_input]["ingredients"]["coffee"]
        r_water = resources["water"]
        r_coffee = resources["coffee"]
        if water > r_water:
            print("There ins't enough water !")
            return False
        elif coffee > r_coffee:
            print("There ins't enough coffee !")
            return False
        else:
            return True
    else:
        water = MENU[user_input]["ingredients"]["water"]
        coffee = MENU[user_input]["ingredients"]["coffee"]
        milk = MENU[user_input]["ingredients"]["milk"]
        r_water = resources["water"]
        r_coffee = resources["coffee"]
        r_milk = resources["milk"]
        if water > r_water:
            print("There ins't enough water !")
            return False
        elif coffee > r_coffee:
            print("There ins't enough coffee !")
            return False
        elif milk > r_milk:
            print("There ins't enough milk !")
            return False
        else:
            return True


def count_money(quarters, dimes, nickles, pennies):
    """Spočíta peniaze."""
    sum = quarters * 0.25 + dimes * 0.1 + nickles * 0.05 + pennies * 0.01
    return sum


def is_enough(sum, user_input):
    """Skontroluje, či je suma dostatočná ."""
    cost = MENU[user_input]["cost"]
    if sum < cost:
        print("Sorry that's not enough money. Money refunded.")
        return False
    elif sum > cost:
        spare = round(sum - cost, 2)
        print(f"Here is {spare} dollars in change.")
        return True


def new_resources(user_input):
    """Odpočíta ingrediencie a prídá cash."""
    if user_input == "espresso":
        resources["water"] = resources["water"] - MENU["espresso"]["ingredients"]["water"]
        resources["coffee"] = resources["coffee"] - MENU["espresso"]["ingredients"]["coffee"]
        resources["cash"] += MENU["espresso"]["cost"]
        return resources
    resources["water"] = resources["water"] - MENU[user_input]["ingredients"]["water"]
    resources["coffee"] = resources["coffee"] - MENU[user_input]["ingredients"]["coffee"]
    resources["milk"] = resources["milk"] - MENU[user_input]["ingredients"]["milk"]
    resources["cash"] += MENU[user_input]["cost"]
    return resources


resources["cash"] = 0
off_check = True
while off_check:
    user_input = input("What would you like ? (espresso/latte/cappuccino): ")
    if user_input == "report":
        print(resources)
    elif user_input == "off":
        off_check = False
    else:
        choice = check_beverage(user_input)
        if choice:
            quarters = int(input("How many quarters are you inserting ?"))
            dimes = int(input("How many dimes are you inserting ?"))
            nickles = int(input("How many nickles are you inserting ?"))
            pennies = int(input("How many pennies are you inserting ?"))
            sum = count_money(quarters, dimes, nickles, pennies)
            enough = is_enough(sum, user_input)
            if enough:
                print(f"Enjoy your {user_input}! ☕")
                resources = new_resources(user_input)
