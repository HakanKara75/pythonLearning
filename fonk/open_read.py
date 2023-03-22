rehber=open("C:/Users/HakanBatirhan/Python/ilk.txt", "r") # r read demektir.
sonuc=rehber.read()
print(sonuc)

sonuc=rehber.readline() #ilk satiri okur.
sonuc=rehber.readline() #ikinci satiri okur.
sonuc=rehber.readline() #ucuncu satiri okur.

sonuc=rehber.readlines() #liste halinde verir

rehber.close()