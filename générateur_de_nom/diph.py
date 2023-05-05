from random import *

def diphtongue():
    r = randint(1, 6)
    c = ""

    if r == 1:
        c = "ai"
    elif r == 2:
        c = "oi"
    elif r == 3:
        c = "ui"
    elif r == 4:
        c = "ou"
    elif r == 5:
        c = "au"
    elif r == 6:
        c = "eau"
    
    return c