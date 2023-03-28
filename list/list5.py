# -*- coding: utf-8 -*-
"""
Created on Mon Mar 27 15:51:48 2023

@author: Hakan Batirhan
"""

#Tuple immutable

liste= [2 ,22, 435, 645]

tuple= (34, 34645, 6, 65)

liste[0]=34556534

print(liste) #[34556534, 22, 435, 645]

#tuple[0]=543256435 #bunu kabul etmez. calisinca hata verir
#print(tuple) #(34, 34645, 6, 65)

karakter= "f"
karakter1= "f"

isim = "Hakan Kara"
isim= isim[:6]+ "Selim"
print(isim) #Hakan Selim

print(isim[0]) #H
print(isim[4]) #n
