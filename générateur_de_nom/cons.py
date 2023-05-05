from random import *

def consonne():
    r = randint(1, 20)
    c = ""

    if r == 1:
        c = "b"
    elif r == 2:
        c = "c"
    elif r == 3:
        c = "d"
    elif r == 4:
        c = "f"
    elif r == 5:
        c = "g"
    elif r == 6:
        c = "h"
    elif r == 7:
        c = "j"
    elif r == 8:
        c = "k"
    elif r == 9:
        c = "l"
    elif r == 10:
        c = "m"
    elif r == 11:
        c = "n"
    elif r == 12:
        c = "p"
    elif r == 13:
        c = "qu"
    elif r == 14:
        c = "r"
    elif r == 15:
        c = "s"
    elif r == 16:
        c = "t"
    elif r == 17:
        c = "v"
    elif r == 18:
        c = "w"
    elif r == 19:
        c = "x"
    elif r == 20:
        c = "z"
    
    return c