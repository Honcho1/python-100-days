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
