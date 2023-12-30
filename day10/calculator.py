def add(n1, n2):
    return n1 + n2


def sub(n1, n2):
    return n1 - n2


def div(n1, n2):
    return n1 / n2


def mul(n1, n2):
    return n1 * n2


operations = {"+": add, "-": sub, "/": div, "*": mul}

num1 = int(input("What's the first number?: "))
num2 = int(input("What's the second number?: "))

for operator in operations:
    print(f"{operator}")

operation = input("Pick an operation from the line above: ")
answer = operations[operation](num1, num2)
print(f"{num1} {operation} {num2} = {answer}")
