"""
title: Black Jack - Zhang Version
author: Michelle Jiang 
date-created: 2022-10-17
"""

from f_deck_of_cards import *

### FUNCTIONS ### 

# Inputs # 

def playerAction(): 
    """
    Player chooses to draw a card or stay 
    :return: int 
    """
    global PLAYERHAND
    displayAllCards(PLAYERHAND)
    print("""
1. Hit me! 
2. Stay
    """)
    CHOICE = int(input("> "))
    if CHOICE < 1 or CHOICE > 2: 
        print("Please enter a valid action!")
        return playerAction()
    else: 
        return CHOICE 



def gameSetup(): 
    """
    Shuffles the deck and deals the starting cards to the players, starts the game 
    :return: None
    """
    print("Welcome to blackjack! Get to 21 without busting! ")
    global PLAYERHAND, DEALERHAND, DECK, PLAYERVALUE, DEALERVALUE, PLAYERSTAY, DEALERSTAY
    DECK = shuffleDeck(DECK)
    PLAYERHAND = []
    DEALERHAND = []
    for i in range(2): 
        PLAYERHAND.append(drawTopCard(DECK))
        DEALERHAND.append(drawTopCard(DECK))
    PLAYERVALUE = 0 
    DEALERVALUE = 0 
    PLAYERSTAY = False 
    DEALERSTAY = False 
    

# Processing # 

def calcPoints(HAND): 
    """
    calculate the total points for the given hand 
    :param HAND: list (tuples->int)
    :return: int (total points)
    """
    # solve the ace problem 
    POINTS = 0
    ACES = 0 
    for card in HAND: 
        if card[0] == 1: 
            POINTS = POINTS + 11 # assumes all aces are 11
            ACES = ACES + 1
        elif card[0] > 9: 
            POINTS = POINTS + 10 
        else: 
            POINTS = POINTS + card[0]
    while POINTS > 21 and ACES > 0: 
        POINTS = POINTS - 10 # if bust then the aces need to be 1
        ACES = ACES - 1 
    return POINTS 

def calcWinner(VALUE1, VALUE2): 
    """
    tests which player wins 
    :param VALUE1: int -> player points
    :paramm VALUE2: int -> dealer points
    :return: int 0 -> no winner, 1 -> player 1, 2 -> player 2
    """
    if VALUE1 < 22 and VALUE2 > 21 or VALUE1 > VALUE2: # if dealer busts or if player > dealer 
        return 1 
    elif VALUE1 > 21 and VALUE2 < 22 or VALUE2 < VALUE1 or VALUE1 == VALUE2: # if player busts, if dealer is greater than player, or if they are equal 
        return 2 
    else: # if they both bust
        return 0 

# Outputs # 

def displayAllHands():
    """
    displays players and dealers hands 
    :param HAND1: list (tuples->int)
    :param HAND2: list (tuples->int)
    :return: None
    """
    global PLAYERHAND, DEALERHAND
    print("Player: ")
    displayAllCards(PLAYERHAND)
    print("Dealer: ")
    displayAllCards(DEALERHAND)

### VARIABLES ### 

PLAYERHAND = []
DEALERHAND = []
DECK = makeDeck()

PLAYERWINS = 0
DEALERWINS = 0 

PLAYERVALUE = 0 
DEALERVALUE = 0 

PLAYERSTAY = False 
DEALERSTAY = False 

### MAIN PROGRAM CODE ## 

if __name__ == "__main__": 
    while PLAYERWINS < 3 and DEALERWINS < 3: 
        gameSetup()

        # Inputs # 

        # Player turn
        while not PLAYERSTAY and PLAYERVALUE < 22: 
            ACTION = playerAction()
            if ACTION == 1: 
                PLAYERHAND.append(drawTopCard(DECK))
                PLAYERVALUE = calcPoints(PLAYERHAND)
            else: 
                PLAYERSTAY = True 
        displayAllCards(PLAYERHAND)

        # Processing # 

        # Dealer turn 
        while not DEALERSTAY and DEALERVALUE < 21: 
            DEALERVALUE = calcPoints(DEALERHAND)    
            if DEALERVALUE < 16: 
                DEALERHAND.append(drawTopCard(DECK))
            else: 
                DEALERSTAY = True 
        displayAllCards(DEALERHAND)
    # determine winner
        WINNER = calcWinner(PLAYERVALUE, DEALERVALUE)
        if WINNER == 1: 
            PLAYERWINS = PLAYERWINS + 1 
            print("Player wins the round! ")
        else: 
            DEALERWINS = DEALERWINS + 1 
            print("Dealer wins the round! ")

        # Outputs # 
        if WINNER == 1: 
            print("Player wins the round! ")
        else: 
            print("Dealer wins the round! ")
    if DEALERWINS < PLAYERWINS: 
        print("Dealer wins the game! ")
    else: 
        print("Player wins the game! ")