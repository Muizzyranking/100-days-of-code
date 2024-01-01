import random
import os
from arts import logo


def clear():
    os.system("cls" if os.name == "nt" else "clear")


def check_score(user, dealer):
    if sum(dealer) == 21:
        print("Computer wins! You lose")
    elif sum(user) == 21 and sum(dealer) != 21:
        print("You win with a Blackjack")
    elif sum(user) == sum(dealer):
        print("Draw")
    elif sum(user) > 21:
        print("You went over. You lose")
    elif sum(user) < sum(dealer):
        print("Computer wins")
    elif sum(user) > sum(dealer):
        print("You win!")


def game():
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    user = []
    dealer = []
    for _ in range(2):
        user.append(random.choice(cards))
        dealer.append(random.choice(cards))

    print(f"    Your cards: {user} score: {sum(user)}")
    print(f"    Computer's first card {dealer[0]}")

    get_another = True
    while get_another and sum(user) < 21:
        get_card = input("Type 'y' to get another card, type 'n' to pass: ")
        if get_card == "y":
            user.append(random.choice(cards))
            if sum(user) > 21:
                if 11 in user:
                    user.remove(11)
                    user.append(1)
            user_score = sum(user)
            print(f"    Your cards: {user} score: {user_score}")
            print(f"    Computer's first card {dealer[0]}")
            if user_score > 21:
                get_another = False
        elif get_card == "n":
            get_another = False

    while sum(dealer) < 17:
        dealer.append(random.choice(cards))
        if sum(dealer) > 21:
            if 11 in user:
                dealer.remove(11)
                dealer.append(1)

    print(f"    Your final hand: {user} final score: {sum(user)}")
    print(f"    Computer's final hand: {dealer} final score: {sum(dealer)}")
    check_score(user, dealer)


while input("Enter 'y' to play or any key to exit: ").lower() == "y":
    clear()
    print(logo)
    game()
