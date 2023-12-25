print("Welcome to love calculator")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")
name = (name1 + " " + name2).lower()
count = 0
true = 0
love = 0
true = name.count("t") + name.count("r") + name.count("u") + name.count("e")
love = name.count("l") + name.count("o") + name.count("v") + name.count("e")

count = int(str(true) + str(love))

if count < 10 or count > 90:
    print(f"Your count is {count}, you go together like coke and mentos.")
elif 40 < count < 50:
    print(f"Your count is {count}, you are alright together.")
else:
    print(f"Your count is {count}.")
