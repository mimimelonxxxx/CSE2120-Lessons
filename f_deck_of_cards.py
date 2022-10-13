"""
title: Deck of Cards Functions
author: Michelle Jiang 
date-created: 2022-10-13
"""
import random

### VARIABLES ### 

SUITS = {
    0: "Diamonds",
    1: "Clubs", 
    2: "Hearts", 
    3: "Spades"
}
VALUES = {
    1: "Ace", 
    11: "Jack", 
    12: "Queen", 
    13: "King"
}  

### FUNCTIONS ### 

# Inputs # 

# Processing # 
def makeDeck(): 
    """ 
    Create a 52-card deck 
    :return: list (tuples -> int)
    """
    DECK = []
    for i in range(4): # suits 
        for j in range(1, 14): # value 1-13
            DECK.append([j, i])
    return DECK 

def shuffleDeck(DECK):
    """
    randomizes the cards in deck
    :param DECK: list (tuples -> int)
    :return: DECK 
    """
    # pop a random index and then append it to a new deck
    SHUFFLEDDECK = []
    for i in range(len(DECK)):
        SHUFFLEDDECK.append(DECK.pop(random.randrange(len(DECK))))
        # you need to use the length of the deck because the deck is progressively getting smaller 
        # can also use random.shuffle(DECK) just to shuffle the deck 
        # go home and review this part 
    return SHUFFLEDDECK

def drawTopCard(DECK):
    """
    draws the top card from the deck 
    :param DECK: list (tuples -> int)
    :return: tuple(int)
    """
    CARD = DECK.pop(0)
    return CARD
    # can also just return DECK.pop(0) for more efficiency 


# Outputs # 
def displayCard(CARD): 
    """
    prints out one card
    :param CARD: tuple -> int 
    :return: None
    """
    global VALUES, SUITS
    if CARD[0] in VALUES: # checks if the value is in the key of VALUES 
        print(f"{VALUES[CARD[0]]} of {SUITS[CARD[1]]}")
    else: 
        print(f"{CARD[0]} of {SUITS[CARD[1]]}")

def displayAllCards(CARDS): 
    """
    prints all cards in a list
    :param CARDS: list (tuples->int)
    :return: None
    """
    global VALUES, SUITS
    DECKREAD = ""
    for CARD in CARDS: 
        if CARD[0] in VALUES: 
            DECKREAD = DECKREAD + f"{VALUES[CARD[0]]} of {SUITS[CARD[1]]}, "
        else: 
            DECKREAD = DECKREAD + f"{CARD[0]} of {SUITS[CARD[1]]}, "
    DECKREAD = DECKREAD[:-2]
    print(DECKREAD)
    

### MAIN PROGRAM CODE ### 

if __name__ == "__main__": 
    MYDECK = makeDeck()
    MYDECK = shuffleDeck(MYDECK)
    CARD = drawTopCard(MYDECK) 
    displayCard(CARD)
    # or you can do this
    HAND = []
    HAND.append(drawTopCard(MYDECK)) 
    print(HAND)
    # Reset deck #
    MYDECK = makeDeck() # resets the deck
    MYDECK = shuffleDeck(MYDECK) # shuffles the deck
    HAND = [] # resets the hand 
    
    displayAllCards(MYDECK)