# -*- coding: utf-8 -*-
"""
Created on Mon Mar 27 16:02:20 2023

@author: Hakan Batirhan
"""

aralik = range (10) # 0 dan basla 10 kadar sayi araliginda calis

listAralik=list(aralik)
setAralik=set(aralik)

print(aralik) #range(0, 10)

print(*aralik) #0 1 2 3 4 5 6 7 8 9

print(list(aralik)) #[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

print(set(aralik)) #{0, 1, 2, 3, 4, 5, 6, 7, 8, 9}

print(str(aralik))

print(str(aralik) [0:5])

#range(start=0, stop, step=1)

say= range(18,2,-5)

aralik= range(2, 20, 3)
print(aralik)