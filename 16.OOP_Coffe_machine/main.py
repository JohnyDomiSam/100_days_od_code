from menu import Menu
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

menu = Menu()
coffe_maker = CoffeeMaker()
money_machine = MoneyMachine()
off_check = True
while off_check:
    user_input = input("What would you like ? (espresso/latte/cappuccino): ")
    if user_input == "report":
        coffe_maker.report()
        money_machine.report()
    elif user_input == "off":
        off_check = False
    else:
        drink = menu.find_drink(user_input)
        if coffe_maker.is_resource_sufficient(drink):
            if money_machine.make_payment(drink.cost):
                coffe_maker.make_coffee(drink)

