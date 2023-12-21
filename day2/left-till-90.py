# calculates the number of days, week and months left till 90
age = int(input("Enter your age: "))

days = 365 * (90 - age)
weeks = 52 * (90 - age)
months = 12 * (90 - age)

print(f"You have {days} days, {weeks} weeks and {months} months left till 90.")
