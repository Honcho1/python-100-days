import os
from art import logo

print(logo)

def clear_screen():
    """Clears the console screen."""
    os.system('cls' if os.name == 'nt' else 'clear')

def add_bidder(bidder_name, bidder_amount, bidders):
    """Adds a bidder to the bidders dictionary."""
    bidders[bidder_name] = bidder_amount
    return bidders

def find_highest_bidder(bidders):
    highest_bid = 0
    winner = ""

    for bidder in bidders:
        bid_amount = bidders[bidder]
        if bid_amount > highest_bid:
            highest_bid = bid_amount
            winner = bidder
    return winner, highest_bid

def run_auction():
    """Runs the auction process."""
    print("Welcome to the secret auction program.")
    auction_active = True
    bids = {}

    while auction_active:
        name = input("What is your name? ")
        bid = int(input("What is your bid? $"))

        add_bidder(name, bid, bids)

        more_bidders = input("Are there any other bidders? Type 'yes' or 'no': ").lower()
        clear_screen()

        if more_bidders != 'yes':
            auction_active = False

    winner, highest_bid = find_highest_bidder(bids)
    print(f"The winner is {winner} with a bid of ${highest_bid}.")
    
if __name__ == "__main__":
    run_auction()
# This code implements a simple auction program where users can place bids.
# It collects bids from multiple users and determines the highest bidder at the end.