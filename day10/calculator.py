import os


def clear():
    os.system("cls" if os.name == "nt" else "clear")


def add(n1, n2):
    return n1 + n2


def sub(n1, n2):
    return n1 - n2


def div(n1, n2):
    return n1 / n2


def mul(n1, n2):
    return n1 * n2


operations = {"+": add, "-": sub, "/": div, "*": mul}


def calculator():
    num1 = float(input("What's the first number?: "))
    num2 = float(input("What's the second number?: "))

    for operator in operations:
        print(f"{operator}")

    operator = input("Pick an operation from the line above: ")
    answer = operations[operator](num1, num2)
    print(f"{num1} {operator} {num2} = {answer}")

    calc_continue = True
    while calc_continue:
        continue_calc = input(
            (f"Type 'y' to continue calculating with {answer} or 'n'  to exit: ")
        )
        if continue_calc == "y":
            operator = input("Choose an operation: ")
            num3 = float(input("Enter another number: "))
            answer = operations[operator](answer, num3)
            print(f"{num1} {operator} {num3} = {answer}")
        elif continue_calc == "n":
            clear()
            calculator()


calculator()
