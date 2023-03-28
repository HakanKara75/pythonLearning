#mutable
# key

sozluk= {1:"Hakan", 2:"Kaan", 3:"Merve", 5:"Kemal", 9:"Jale"}

print(sozluk[2]) #Kaan

print(sozluk.get(3)) #Merve

print(sozluk.get(4, "bu anahtar sozlukta yok"))

yaslar= (1,25,65,84)
bilgiler=("doktor", "ogretmen", "ciftci", "garson")

sozlukElemanlari= zip(yaslar,bilgiler)
print(*sozlukElemanlari) #(1, 'doktor') (25, 'ogretmen') (65, 'ciftci') (84, 'garson')

