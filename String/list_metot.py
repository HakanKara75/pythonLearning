# -*- coding: utf-8 -*-
"""
Created on Sun Mar 26 10:53:08 2023

@author: Hakan Batirhan
"""

#count sayma yapar
liste=[454, 63, 653, -354, "hakan", "kara", 24.54]
liste.count(653)
liste.count("hakan")

#copy kopyalama yapar
yedek=liste.copy()

#extend listeleri birlestirir
ad=["yesim", "merve", "kara"]

liste.extend(["selam", "sabah"])
print(liste)

#index
liste.index("sabah")

#reverse terse cevirir
liste.reverse()
print(liste)

#sort aynş turden variable elemani olan listeleri siralama yapar.
ad.sort()

#clear listeyi temizler. icini siler. liste kalir.

liste.clear()