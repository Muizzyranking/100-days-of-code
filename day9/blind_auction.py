from arts import logo
import os

print(logo)
print("Welcome to the secret auction program.")

bidders = {}


def highest_bid(bidders):
    highest_bid = 0
    name = ""
    for bids in bidders:
        if bidders[bids] > highest_bid:
            highest_bid = bidders[bids]
            name = bids
    print(f"The highest bidder is {name} with a bid of ${highest_bid}")


def clear():
    os.system("cls" if os.name == "nt" else "clear")


is_bidding = True
while is_bidding:
    name = input("What is your name?: ").capitalize()
    bid = int(input("What is your bid?: $"))
    bidders[name] = bid

    should_continue = input("Are there any other bidders? Type 'yes' or 'no'.\n")
    if should_continue.lower() == "no":
        clear()
        highest_bid(bidders)
        is_bidding = False
    elif should_continue.lower() == "yes":
        clear()
        print(logo)
