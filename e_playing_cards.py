"""
title: Playing Cards 
author: Michelle Jiang 
date-created: 2022-10-12
"""

CARDS = []

for i in range(4): # suits
    CARDS.append([])
    for j in range(13): # value 
        CARDS[i].append(j+1)

print(CARDS)

# the problem is that no one structure represents a single card 

# a data structure must represent a single card 

CARDS = []
for i in range(4): 
    for j in range(13): 
        CARDS.append((i, j+1))

print(CARDS)

SUITS = {
    0: "Diamonds", 
    1: "Clubs", 
    2: "Hearts", 
    3: "Spades"
}

VALUES = {
    1: "Ace", 
    2: 2, 
    3: 3, 
    4: 4, 
    5: 5, 
    6: 6, 
    7: 7, 
    8: 8, 
    9: 9, 
    10: 10, 
    11: "Jack", 
    12: "Queen", 
    13: "King"
}

print(CARDS[5])
print(f"{VALUES[CARDS[12][1]]} of {SUITS[CARDS[12][0]]}")

ONE_CARD = CARDS[15]
print(f"{VALUES[ONE_CARD[1]]} of {SUITS[ONE_CARD[0]]}")