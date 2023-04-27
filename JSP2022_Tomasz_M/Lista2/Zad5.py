import math
napis  = input("Podaj napis pierwszy: ")
napis2 = input("Podaj napis drugi: ")
if (len(napis)%2) == 0:
    print(napis[:math.floor(len(napis)/2)] + napis2 + napis[math.ceil(len(napis)/2):]) 
else:
    print(napis[:math.floor(len(napis)/2)] + napis2 + napis[math.ceil(len(napis)/2):])
