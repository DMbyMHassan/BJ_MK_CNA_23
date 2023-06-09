# This module to define deck cards using list to store suits,rank and points

import random

# define  card  suits, ranks and their respective values
SUITS = ['Hearts', 'Diamonds', 'clubs', 'Speades']
RANKS = ['Ace', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'Jack', 'Queen', 'King']
VALUE = {'Ace': 11, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9, '10': 10, 'Jack': 10,
         'Queen': 10, 'King': 10}


# The function to creat a deck of cards by combing list of suits and ranks
def create_deck():
    deck = []
    for suit in SUITS:
        for rank in RANKS:
            value = VALUE[rank]
            deck.append([suit, rank, value])
    return deck


# The function to Shuffle the deck of card
def shuffle_deck():
    random.shuffle()
