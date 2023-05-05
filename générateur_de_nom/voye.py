from random import *

def voyelle():
    r = randint(1, 10)
    c = ""

    if r == 1:
        c = "a"
    elif r == 2:
        c = "e"
    elif r == 3:
        c = "i"
    elif r == 4:
        c = "o"
    elif r == 5:
        c = "u"
    elif r == 6:
        c = "y"
    elif r == 7:
        c = "eu"
    elif r == 8:
        c = "é"
    elif r == 9:
        c = "è"
    elif r == 10:
        c = "ê"
    
    return c