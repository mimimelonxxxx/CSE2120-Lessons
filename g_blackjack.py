"""
title: Blackjack
author: Michelle Jiang 
date-created: 2022-10-13
"""
from f_deck_of_cards import * 
### VARIABLES ### 
PLAYER1WINS = 0 
PLAYER2WINS = 0 
PLAYER1HAND = []
PLAYER2HAND = []

### FUNCTIONS ### 

# Inputs # 
def startGame(): 
    """
    intro to game 
    :return: None
    """
    print("Play blackjack between two players! Try to get to 21 without busting!")
    return 

def dealCards(PLAYER, DECK): 
    """
    deals two cards from the top of the deck to the player 
    :param PLAYER: list (empty)
    :param DECK: list (tuples->int)
    :return: PLAYER list (tuples->int), DECK list (tuples->int)
    """
    PLAYER.append(drawTopCard(DECK))
    PLAYER.append(drawTopCard(DECK))
    return PLAYER, DECK 

# Processing # 

def calculateHand(HAND):
    """
    calculates the value of the hand 
    :param HAND: list (tuples->int)
    :return: int 
    """
    CALCULATED = 0
    for i in range(len(HAND)):
        CARD = drawTopCard(HAND)
        if CARD[0] > 10:
            CALCULATED += 10
            HAND.append(CARD)
        elif CARD[0] > 1 and CARD[0] < 10:
            CALCULATED += CARD[0]
            HAND.append(CARD)
        elif CARD[0] == 1 and CALCULATED < 11: # if the total card value is 10 or less, then you can add 11 for aces
                CALCULATED += 11
                HAND.append(CARD)
        else: 
                CALCULATED += CARD[0]
                HAND.append(CARD)
    return CALCULATED

def drawCard(HAND, DECK, VALUE):
    """
    asks the player if they want to draw a card
    :param HAND: list(tuples->int)
    :param DECK: list(tuples->int)
    :param VALUE: int 
    :return: HAND list(tuples->int), DECK list(tuples->int), VALUE int
    """
    DRAW = input("Would you like to draw a card? 1 for yes: ")
    if DRAW == "1": 
        HAND.append(drawTopCard(DECK))
        VALUE = calculateHand(HAND)
        return HAND, DECK, VALUE
    else: 
        pass

def calculateWinner(VALUE1, VALUE2): 
    """
    calculates and displays the winner 
    :param VALUE1: int
    :param VALUE2: int 
    :return: int 
    """
    if VALUE2 > 21 or VALUE1 == 21 or VALUE1 > VALUE2 and VALUE1 < 21 and VALUE2 < 21: 
        return 1 # if player 1 wins
    elif VALUE1 > 21 or VALUE2 == 21 or VALUE2 > VALUE1 and VALUE2 < 21 and VALUE2 < 21 or VALUE1 == VALUE2 and VALUE1 < 21 and VALUE2 < 21: 
        return 2 # if the dealer wins
    else: 
        return 0 # to continue drawing 

# Outputs # 


### MAIN PROGRAM CODE ### 
if __name__ == "__main__": 
    # Inputs # 
    DECK = makeDeck() 
    DECK = shuffleDeck(DECK) 
    startGame() 
    # Processing # 
    PLAYER1HAND, DECK = dealCards(PLAYER1HAND, DECK)
    PLAYER2HAND, DECK = dealCards(PLAYER2HAND, DECK) # starting position 
    HAND1VALUE = calculateHand(PLAYER1HAND)
    HAND2VALUE = calculateHand(PLAYER2HAND) 
    displayAllCards(PLAYER1HAND) # shows the player what cards they have 
    PLAYER1HAND, DECK, HAND1VALUE = drawCard(PLAYER1HAND, DECK, HAND1VALUE) 
    displayAllCards(PLAYER1HAND) # shows the player their updated hand 
    # Outputs # 