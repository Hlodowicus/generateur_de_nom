from random import *

def voyelleMA(): #diphtongue du moyen-âge
    r = randint(1, 3)
    c = ""

    if r == 1:
        c = "oy"
    elif r == 2:
        c = "ay"
    elif r == 3:
        c = "uy"
    
    return c