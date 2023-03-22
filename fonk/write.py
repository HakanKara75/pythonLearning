try:
    rehber = open("C:/Users/HakanBatirhan/Python/ilk.txt", "w")  # w yazma demektir.

    kayitlar = """Hakan Kara
Pınar Kara
Merve Kara
Orhan Kara
Burak Kara"""

    rehber.write(kayitlar)

except IOError:
    print("Bir hata olustu")
finally:
    rehber.close()
