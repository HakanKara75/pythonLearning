kayitlar = """Hakan Kara
Pınar Kara
Merve Kara
Orhan Kara
Burak Kara"""

with open("C:/Users/HakanBatirhan/Python/ilk.txt", "a")  as dosya: #a ile dosya degistirilir.
        dosya.write("\nAyhan Kara\nTürkan Kara\n") #\n ile en alt satirdan yazdirmaya baslar.

with open("C:/Users/HakanBatirhan/Python/ilk.txt", "r+") as dosya:  # r+ ile dosya basindan itibaren okur, yazar.
    dosya.read()
    dosya.seek(0) #dosya basina gelir ve ilk satira yazdirmak icin imleci koyar.
    dosya.write("\nTalha Kara\nAyfer Kara\n")

with open("C:/Users/HakanBatirhan/Python/ilk.txt", "r+") as dosya:  # r+ ile dosya basindan itibaren okur, yazar.
    okunanlar=dosya.readlines() #satirlari liste haline getirir
    okunanlar.insert(2,"\nPınar : 468766357687645\n") #2 ile 2. satira ekler
    dosya.seek(0) #dosya okunup imlec en sona gittigi icin imleci basa dondurmek icin yapariz
    dosya.writelines(okunanlar) #liste son hali ile dosyaya geri yuklenir
