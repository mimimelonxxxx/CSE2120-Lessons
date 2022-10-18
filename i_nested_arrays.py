"""
title: 2D Array Practice
author: Michelle Jiang 
date-created: 2022-10-18
"""

if __name__ == "__main__":

    SIZE = 5

    # Example
    print("Example:")
    GRID = []

    # Fill the grid 
    for row in range(SIZE): 
        GRID.append([]) # appends an empty row 
        for column in range(SIZE): 
            GRID[row].append(row*SIZE+column+1) # your row * size + column # + 1 eg: if row = 1 then 5 + column # + 1 (second row)

    # Output
    for row in range(SIZE): 
        print(GRID[row])

    # Problem 4 
    print("Problem 4:")
    GRID = []

    # Fill the grid 
    for row in range(SIZE): 
        GRID.append([]) # appends an empty row 
        for column in range(SIZE): 
            GRID[row].append(SIZE**2-SIZE*(row+1)+column+1) # size ^ 2 for the top right corner and then you go to the left (subtract the difference in column number) and decrease by rows 

    # Output 
    for row in range(SIZE): 
        print(GRID[row])

    # Problem 1 
    print("Problem 1: ")

    GRID = []

    # Fill the grid 
    for row in range(SIZE): 
        GRID.append([]) # appends an empty row 
        for column in range(SIZE): 
            GRID[row].append(column) 

    # Output 
    for row in range(SIZE): 
        print(GRID[row])

    # Problem 2
    print("Problem 2:")

    GRID = []

    # Fill the grid 
    for row in range(SIZE): 
        GRID.append([]) # appends an empty row 
        for column in range(SIZE): 
            GRID[row].append(row)

    # Output 
    for row in range(SIZE): 
        print(GRID[row])

    # Problem 7
    print("Problem 7:")
    
    GRID = []

    # Fill the grid 
    for row in range(SIZE): 
        GRID.append([]) # appends an empty row 
        for column in range(SIZE): 
            GRID[row].append(column+1+row%2*SIZE) # 

    # Output 
    for row in range(SIZE): 
        print(GRID[row])
        
    # Problem 8
    print("Problem 8:")
    
    GRID = []

    # Fill the grid 
    for row in range(SIZE): 
        GRID.append([]) # appends an empty row 
        for column in range(SIZE): 
            GRID[row].append(row+1+column*SIZE) # gave up for now 

    # Output 
    for row in range(SIZE): 
        print(GRID[row])