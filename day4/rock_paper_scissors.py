import random

images = [
    # Rock
    """
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
""",
    # Paper
    """
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
""",
    # Scissors
    """
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
""",
]

choices = ["Rock", "Paper", "Scissors"]

computer_choice = random.randint(0, 2)
user_choice = int(
    input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n")
)
if user_choice >= 0 and user_choice <= 2:
    print(f"You chose {choices[user_choice]}")
    print(images[user_choice])
    print(f"Computer chose {choices[computer_choice]}")
    print(images[computer_choice])
    if user_choice == computer_choice:
        print("It's a tie!")
    elif user_choice == 0 and computer_choice == 1:
        print("You Lose!")
    elif user_choice == 0 and computer_choice == 2:
        print("You Win!")
    elif user_choice == 1 and computer_choice == 0:
        print("You Win!")
    elif user_choice == 1 and computer_choice == 2:
        print("You Lose!")
    elif user_choice == 2 and computer_choice == 0:
        print("You Lose!")
    elif user_choice == 2 and computer_choice == 1:
        print("You Win!")
else:
    print("You entered an invalid number. You lose!")
