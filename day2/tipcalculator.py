# calculates and split the bill amongst n number of people
# the tip percentage is 15%, 10%, or 5%
print("Welcome to tip calculator")
amount = input("What was the total bill? $")
number_of_people = input("How many people to split the bill? ")
tip = input("What percentage tip would you like to give? 10, 15, or 20? ")
amount = float(amount)
number_of_people = int(number_of_people)
tip = (int(tip) / 100) * amount
total = amount + tip
split = round((total / number_of_people), 2)
print(f"Each person should pay: ${split}")
