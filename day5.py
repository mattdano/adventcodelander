import numpy as np
import datetime
import pandas as pd
from itertools import permutations,combinations
import copy

f = open("./input_5.txt",'r')

letters='abcdefghijklmnopqrstuvwxyz'
upletters = letters.upper()
lowletters=letters.lower()

possibles = []
for idx,u in enumerate(upletters):

    possibles.append(lowletters[idx]+u)
    possibles.append(u+lowletters[idx])

print(possibles)

ogline= f.read().splitlines()[0]
line=copy.copy(ogline)
#line='dabAcCaCBAcCcaDA'
polymer = []
for l in line:
    polymer.append(l)

pos = 0



#while True:
best = 40000
for poss in lowletters:
    print('removing',poss)
    line = copy.copy(ogline)
    line = line.replace(poss,'').replace(poss.upper(),'')
    print(line)
    polymer = []
    for l in line:
        polymer.append(l)

    while True:
        try:
            startsize = len(polymer)
            subunit = polymer[pos]+polymer[pos+1]

            if subunit in possibles:
                polymer.pop(pos)
                polymer.pop(pos)
                pos = pos-1
                #endsize = len(polymer)
            else:
                pos=pos+1
        except IndexError:
            break
        #print(''.join(polymer))

        #if startsize==endsize:
            #break

    final=''.join(polymer)
    #print(final)
    #print(len(final))
    if best > len(final):
        best=len(final)
print(best)