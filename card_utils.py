# card_utils.py

import random

suits_deck = ["Spades", "Hearts", "Diamonds", "Clubs"]
ranks_deck = ["2", "3", "4", "5", "6", "7", "8", "9", "T", "J", "Q", "K", "A"]  #'T' is 10


# Create a full 52-card deck as strings
def create_deck():
    deck = []

    for suit in suits_deck:
        for rank in ranks_deck:
            card = rank + " " + suit
            deck.append(card)
    return deck

# Shuffle
def shuffle_deck(deck):
    random.shuffle(deck)

# Draw 
def draw_cards(deck, num):
    drawn = []

    for i in range(num):
        card = deck.pop(0)
        drawn.append(card)
    return drawn