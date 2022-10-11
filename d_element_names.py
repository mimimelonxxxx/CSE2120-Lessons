"""
title: Chemical Element Names
author: Michelle Jiang 
date-created: 2022-10-11
"""
ELEM_NAMES = {
    "H": "Hydrogen",
    "He": "Helium",
    "Na": "Sodium", 
    "Cl": "Chlorine"
}

ELEM_ATOM_NUM = {
    "H": 1,
    "He": 2, 
    "Na": 10, 
    "Cl": 17
}

ELEM_MASS = {
    "H": 1.01,
    "He": 4.00,
    "Na": 22.99, 
    "Cl": 35.45
}

if __name__ == "__main__": 
    print(ELEM_NAMES["H"])
    print(ELEM_ATOM_NUM["H"])
    print(ELEM_MASS["H"])
    print(f"NaCl's mass is {ELEM_MASS['Na'] + ELEM_MASS['Cl']}g/mol.")