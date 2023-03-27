# -*- coding: utf-8 -*-
"""
Created on Sun Mar 26 10:43:02 2023

@author: Hakan Batirhan
"""
#append liste eleman ekler

liste= ["hakan", 4353, True, "pinar"]
liste.append("merve")
dir(liste)

#remove elemani verilen value ya gore siler
liste.remove("hakan")
print(liste)

#insert indekse gore eleman ekler

liste.insert(2, 8564.6)
liste.insert(0, "tahir")
print(liste)

liste.insert(len(liste), "burak") #liste sonuna eleman eklendi.

#pop elemani indekse gore siler
liste.pop(0)
liste.pop(4)