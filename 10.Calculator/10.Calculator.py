from art import logo


def add(n1, n2):
    return n1 + n2


def subtract(n1, n2):
    return n1 - n2


def multiply(n1, n2):
    return n1 * n2


def divide(n1, n2):
    return n1 / n2


operations = {"+": add, "-": subtract, "*": multiply, "/": divide}


def calculator():
    """kalkulačka"""
    print(logo)
    num1 = float(input("What's the first number?: "))
    for symbol in operations:
        print(symbol)
    user_continue = True
    while user_continue:
        operation_symbol = input("Pick an operation: ")
        next_number = float(input("What's the next number?: "))
        calculation_function = operations[operation_symbol]
        answer = calculation_function(num1, next_number)
        print(f"{num1} {operation_symbol} {next_number} = {answer}")
        num1 = answer
        want_continue = input(
            f'Type "y" to continue calculation with {answer}, or "n" to start a new calculation. '
        ).lower()
        if want_continue == "y":
            user_continue = True
        else:
            user_continue = False
            calculator()


calculator()
