message='Hello There. My name is Hakan Kara'

message=message.upper() #karakterleri buyuk harfe cevirir
message=message.lower() #karakterleri kucuk harfe cevirir
message=message.title() #kelimelerin ilk harfini buyuk harfe cevirir
message=message.capitalize() #kelimenin ilk harfini buyuk harfe cevirir

message=' Hello There. My name is Hakan Kara'
message=message.strip() #bastaki bosluk karakterini siler
print(message[1]) #1. kelimeyi yazdirir
message=message.split() #kelimeleri bosluktan parcalar
#message=message.split('.') #kelimeleri (.) dan parcalar
message=' '.join(message) # bosluktan ayrilmis kelimleri birlestirir.

index=message.find('Hakan') #kelimenin ilk harfinin indexini verir
print(index)

isFound=message.startswith('H') #metnin H ile baslayip baslamadigini true false olarak dondurur
isFound=message.endswith('H') #metnin H ile bitip bitmedigini true false olarak dondurur
print(isFound)

message=message.replace('Kara', 'Batur') # bir metinde verilen seyi degistirir. atama yapmaya gerek yoktur.
message=message.replace(' ', '.')
print(message)

message=message.center(100)# metin icin 100 karakterlik alan olusturur ve metni bunun ortasina ortalar.
print(message)

B= "Hakan Kara"
print(B.islower()) #kucuk mu diye sorar. true/false doner
print(B.isupper())