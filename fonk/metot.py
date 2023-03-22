import os
if os.name!='nt': # isletim sistemi, windows degilse
    print("bu program windowsta calisir")
else:
    print("bu program windows disinda calismaz")


sozluk= { "kitap": "book", "bilgisayar":"computer"}

def ara(sozcuk):
    hata="{} kelimesi sozlukte yok"
    return sozluk.get(sozcuk, hata.format(sozcuk))

# import sozluk
#         sonuc=sozluk.ara("kitap")
#         print(sonuc)
