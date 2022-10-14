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

            

# Outputs # 


### MAIN PROGRAM CODE ### 
if __name__ == "__main__": 
    # Inputs # 
    DECK = makeDeck() 
    DECK = shuffleDeck(DECK) 
    startGame() 
    # Processing # 
    PLAYER1HAND, DECK = dealCards(PLAYER1HAND, DECK)
    PLAYER2HAND, DECK = dealCards(PLAYER2HAND, DECK)
    HAND1VALUE = calculateHand(PLAYER1HAND)
    HAND2VALUE = calculateHand(PLAYER2HAND)
    print(PLAYER1HAND)
    print(HAND1VALUE)
    # Outputs # 