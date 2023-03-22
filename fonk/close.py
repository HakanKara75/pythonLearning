kayitlar = """Hakan Kara
Pınar Kara
Merve Kara
Orhan Kara
Burak Kara"""

with open("C:/Users/HakanBatirhan/Python/ilk.txt", "w")  as dosya: #with ile dosya hata verse bile kapatılır.
        dosya.write(kayitlar)

