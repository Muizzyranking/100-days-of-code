import random

print("Welcome to who will pay the bill picker")
names_string = input("Give me everybody's names, separated by a comma. ")
names_string = names_string.split(", ")
length = len(names_string)

choice_index = random.randint(0, length - 1)
should_pay = names_string[choice_index]
should_pay = should_pay.capitalize()

print(f"{should_pay} is going to buy the meal today")
