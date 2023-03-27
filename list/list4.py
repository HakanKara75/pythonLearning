# -*- coding: utf-8 -*-
"""
Created on Sun Mar 26 10:10:51 2023

@author: Hakan Batirhan
"""

#1.yol
notlar=[56,6,65686,686,-54472]
type(notlar)

liste=["sfgsgf", 19.3, True, -15467]
type(liste)

genis_liste=["hakan", -54, 17.8, notlar, liste]
type(genis_liste)
len(genis_liste) #eleman sayisini verir
type(genis_liste[2]) #list icindeki elemanin tipini verir
type(genis_liste[4]) #list icindeki elemanin tipini verir


#del genis_liste #listeyi siler

genis_liste[0:2] #0 dan 2. elemana kadar listele

yeni_list=["d", 57, 25.8, False, [564, "gdg", "gfsgf"]]

yeni_list[4][2] #liste icindeki list elemanina ulasilir

karisik=[yeni_list, "hl", "lhl", 825, -548, 2654.5]
karisik[0][1]

isimler=["ali", "merve", "pinar", "hakan"]
isimler[3]="hakan kara" #elemani yeni degerle degistirir
print(isimler)

isimler[0:3]= "ali seker", "merve yeni", "pinar gul" #araliktaki elemanlari sirali degistirir
print(isimler)

isimler = isimler + ["kemal tahir"] #yeni eleman atanarak eklenir

del liste[2] #indeksteki elemani siler

isimler [0]="orhan orkun" #istenen indekse eleman ekler
print(isimler)







