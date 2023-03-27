# -*- coding: utf-8 -*-
"""
Created on Sat Mar 25 18:38:46 2023

@author: Hakan Batirhan
"""

print("hakan","kara", sep=("_")) #sep ile iki string arasina eklenir.
print("hakan","kara", sep=(". ."))
print("hakan", "kara", sep= "_")


ifade = "1012340"
ifade = ifade + "1"
print(ifade.strip("1")) #012340 yazdirir

degisken = 4
degisken*degisken #sonuc cikmaz bu islemle. yazdirmak lazim
print(degisken*degisken)

print("9" + 1) #typerror uretir. str ve int concat edilemez.

print(len(ifade))
