# " Hello World " un bas ve sonundaki bosluklari sil
result=" Hello World "
result=result.strip() #bas ve sondaki bosluklari siler
result=result.lstrip() #soldaki boslugu siler
result=result.rstrip() #sagdaki boslugu siler

website="https://www.hakankara.com"
result=website.lstrip("://.")

# "Merhaba Hakan Kara. Nasılsın?" metnindeki Hakan Kara haric herseyi silin
result= "Mrb Hakan Kara. www?".strip("Mrb . www?")

#course kelimesini buyuk harf yapin
c="course".upper()

#website icinde kac a karakteri var
result=website.count("a") #a lari sayar
result=website.count("a", 0,10) # 0-10 index arasindaki a lari sayar

# website www ile baslayip com ile bitiyor mu?
result=website.startswith("www")
result=website.endswith("com")

#website icinde com ifadesi var mı?
result=website.find("com") #varsa index numarasini verir
result=website.find("com", 0,10) # 0-10 index arasi var mi
result=website.index("com") # index verir

#course icindeki karakterlerin hepsi alafabetik mi
course= "Hakan merb 4643 ?343"
result=course.isalpha()
result="Hakan".isalpha()
result="242435".isdigit()

# contents ifadesini satirda 50 karakter icine yerlestirip sag ve soluna * ekleyiniz
result="Contents".center(50, "*")
result="Contents".ljust(50, "*") #kelimeyi sola yaslar
result="Contents".rjust(50, "*") #kelimeyi saga yaslar

#course karaketer dizesindeki tum bosluklari "-" ile degistirin.
result=course.replace(" ", "_", 5) #5 karakteri degistirir

#"Hello World" de "Worl" yerine "There" koyun
result="Hello World".replace("Worl", "There")

#course  dizisini bosluk karakterlerinden ayirin

result=course.split(" ")
result=result[2] #parcalanmis metinde 2. kelime












