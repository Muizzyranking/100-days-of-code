import random
import os


def clear():
    """Clears the screen"""
    os.system("cls" if os.name == "nt" else "clear")


def set_diffculty():
    """Request user to choose difficulty"""
    mode = input("Choose easy or hard mode: ").lower()
    trials = 0
    if mode == "easy":
        print("You have 10 tries")
        trials = 10
    elif mode == "hard":
        print("You have 5 tries")
        trials = 5
    else:
        print("Invalid mode")
        set_diffculty()
    return trials


def play_game():
    """Run guess the game"""
    number = random.randint(1, 100)
    trials = 0
    print("Welcome to number guessing game ")
    print("I am thinking of a number between 1 and 100")
    trials = set_diffculty()

    is_game_over = False
    while not is_game_over and trials > 0:
        user_guess = int(input("Enter your guess: "))
        clear()
        if user_guess == number:
            print("You guessed it right")
            print("You win")
            is_game_over = True
        elif user_guess > number:
            print("Your guess is too high")
        elif user_guess < number:
            print("Your guess is too low")
        trials -= 1
        if user_guess != number:
            print(f"You have {trials} trials left")
        if user_guess != number and trials == 0:
            print("You lose")


clear()
play_game()
