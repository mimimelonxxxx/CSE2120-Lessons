"""
title: Rock, Paper, Scissors, Lizard, Spock 
author: Michelle Jiang 
date-created: 2022-10-05
"""

from random import randrange
import sys
### VARIABLES ###
WEAPONS = ("Rock", "Lizard", "Spock", "Scissors", "Paper")

### SUBROUTINES ###
# Inputs # 
def checkInt(VALUE): 
    """
    Validate whether a string is an integer 
    :param VALUE: string 
    :return: int 
    """
    if VALUE.isnumeric(): 
        VALUE = int(VALUE) 
        return VALUE
    else: 
        print("Please enter a valid number! ")
        NEW_NUM = input("> ")
        return checkInt(NEW_NUM)

def menu():
    """
    displays user selection and user chooses their weapon 
    :return: int 
    """
    global WEAPONS
    print(f"""Welcome to {WEAPONS[0]}, {WEAPONS[4]}, {WEAPONS[3]}, {WEAPONS[1]}, {WEAPONS[2]}! Please choose your weapon wisely! 
1. {WEAPONS[0]}
2. {WEAPONS[1]}
3. {WEAPONS[2]}
4. {WEAPONS[3]}
5. {WEAPONS[4]}""")
    WEAPON = input("> ")
    WEAPON = checkInt(WEAPON)
    if WEAPON > 0 and WEAPON < 6: 
        return WEAPON-1
    else: 
        print("Please enter an integer between 1 and 5 inclusive! ")
        return menu()

def playAgain():
    """
    asks the user if they want to play again 
    :return: boolean
    """
    CHOICE = input("Would you like to play again? (Y/n): ")
    if CHOICE == "n" or CHOICE == "N": 
        return False
    else: 
        return True

# Processing # 
def computerChoice():
    """
    The computer chooses a weapon! 
    :return: int 
    """
    global WEAPONS
    WEAPON = randrange(len(WEAPONS))
    return WEAPON

def determineWinner(PLAYER, COMPUTER): 
    """
    determines the winner of this round! 
    :param PLAYER: int - player's choice
    :param COMPUTER: int - computer's choice
    :return: int - winner of the round (0: tie, 1: player, 2: computer)
    """
    global WEAPONS
    if PLAYER == COMPUTER: 
        return 0
    elif WEAPONS[COMPUTER] == WEAPONS[PLAYER-1] or WEAPONS[COMPUTER] == WEAPONS[PLAYER-3]: 
        return 2
    else:
        return 1

# Outputs # 
def displayWinner(WINNER, PLAYER, COMPUTER): 
    """
    display the winner of the round 
    :param WINNER: int 
    :return: None
    """
    global WEAPONS 
    print(f"You chose {WEAPONS[PLAYER]}, Computer chose {WEAPONS[COMPUTER]}.")
    if WINNER == 0: 
        print(f"It's a tie!")
    elif WINNER == 1: 
        print("You won! ")
    elif WINNER == 2: 
        print("You lost! ")
    
### MAIN PROGRAM CODE ### 
if __name__ == "__main__":
    while True:
        # Inputs # 
        PLAYER = menu() 
        COMPUTER = computerChoice() 
        # Processing # 
        WINNER = determineWinner(PLAYER, COMPUTER)
        # Outputs #
        displayWinner(WINNER, PLAYER, COMPUTER)
        if not playAgain():
            sys.exit()