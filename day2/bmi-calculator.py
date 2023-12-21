# calculates the body mass index of a user
height = float(input("Enter your height in m: "))
weight = float(input("Enter your weight in kg: "))
bmi = weight / (height**2)
bmi = int(bmi)
print(f"Your BMI is {bmi}")
