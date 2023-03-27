# -*- coding: utf-8 -*-
"""
Created on Mon Mar 27 13:52:37 2023

@author: Hakan Batirhan
"""

onerme= "Fenerbahce bir futbol takimidir"
onetme1="Fenerbahce dunyanin en iyi futbol takimidir"

onerme2= "Galatasaray bir futbol takimidir"
onetme3="Galatasaray dunyanin en iyi futbol takimidir"

o=True      #1
o1=False    #0
o2=True
o3=False

# or | and | not

a , b= 10, 12
c , d, e= 20, 25, 30

print(a <15 or b < 20 )
print("{} or {} = {}". format(a < 15, b < 20, a < 15 or b < 20))
print("{} or {} = {}". format(a < 10, b < 20, a < 10 or b < 20))
print("{} or {} = {}". format(a < 15, b < 15, a < 15 or b < 15))
print("{} or {} = {}". format(a < 10, b < 15, a < 10 or b < 20))

print("{} or {} = {}". format(a < 15, b < 20, a < 15 and b < 20))
print("{} or {} = {}". format(a < 10, b < 20, a < 10 and b < 20))
print("{} or {} = {}". format(a < 15, b < 15, a < 15 and b < 15))
print("{} or {} = {}". format(a < 10, b < 15, a < 10 and b < 20))

anahtar = True
print(anahtar)
anahtar = not anahtar
print(anahtar)

sonuc= not (a < 15 and b < 20 or c < 25 and d < 30 )
#sonuc=False

