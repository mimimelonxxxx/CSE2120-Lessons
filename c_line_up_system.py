"""
title: Waiting In Line 
author: Michelle Jiang 
date-created: 2022-10-06
"""

### SUBROUTINES ### 

# Inputs # 

from ast import Return


def menu():
    """
    user selects a function
    :return: int 
    """
    print("""
1. Stand in line 
2. Serve a customer 
3. Exit
    """)
    CHOICE = input("> ")
    return(int(CHOICE))

def askName():
    """
    waiting customer inputs their name 
    :return: str
    """
    return input("Name: ")

# Processing # 

def addToLine(NAME, LINE):
    """
    :param NAME: str
    :param LINE: list
    :return: list
    """
    LINE.append(NAME)
    return LINE 

def serveNextCustomer(LINE):
    """
    returns the next customer in the line
    :param LINE: 
    :return: str
    """
    CUSTOMER = LINE.pop(0)
    return CUSTOMER 
    

# Outputs # 

def displayNextCustomer(CUSTOMER): 
    """
    displays the next customer
    :param CUSTOMER: str 
    :return: 
    """
    print(f"Next customer: {CUSTOMER}")

def displayLineLength(LINE):
    """
    displays to the customer where they are in the line
    :param LINE: list 
    :return: 
    """
    print(f"{LINE[-1]}, you are number {len(LINE)} in line.")

### MAIN PROGRAM CODE ### 
if __name__ == "__main__":

### VARIABLES ### 
    CUSTOMERS = []

    while True:
# Inputs # 
        ACTION = menu()
        if ACTION == 1: 
            CUSTOMER = askName()
# Processing # 
            CUSTOMERS = addToLine(CUSTOMER, CUSTOMERS)
# Outputs # 
            print(CUSTOMERS)
            displayLineLength(CUSTOMERS)
        elif ACTION == 2: 
            if len(CUSTOMERS) > 0: 
                NOWSERVING = serveNextCustomer(CUSTOMERS)
                displayNextCustomer(NOWSERVING)
            else: 
                print("No one is in line. ")
        else:
            exit()