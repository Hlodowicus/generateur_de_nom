from random import *
from cons import *
from diph import *
from voye import *
from voyeMA import *

demande = input("c = voyelle\nv = voyelle\nd = diphtongue\nm = diphtongue ancienne\nles espaces sont acceptés pour créer des phrases\n")
resultat = []
pattern = list(demande)
x = 0
y = len(demande)
mot = ""

while x < y:
    #p = pattern(x)
    if pattern[x] == "c":
        resultat.append(consonne())
    elif pattern[x] == "v":
        resultat.append(voyelle())
    elif pattern[x] == "d":
        resultat.append(diphtongue())
    elif pattern[x] == "m":
        resultat.append(voyelleMA())
    elif pattern[x] == " ":
        resultat.append(" ")

    x += 1

mot = "".join(resultat)
print(resultat)
print(mot)