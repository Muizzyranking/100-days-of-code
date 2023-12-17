# calculates and split the bill amongst n number of people
# the tip percentage is 15%, 10%, or 5%
print("Welcome to tip calculator")
amount = float(input("What was the total bill? $"))
number_of_people = int(input("How many people to split the bill? "))
tip = int(input("What percentage tip would you like to give? 10, 15, or 20? "))
tip = (tip / 100) * amount
total = amount + tip
split = total / number_of_people
print(f"Each person should pay: ${split:.2f}")
