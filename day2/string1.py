course= 'Python Kursu: Baştan sona python programlama rehberiniz (40 saat)'
website= "https://www.linkedin.com/notifications/?filter=all"
#1- "course" karakter dizisinde kac karakter bulunmaktadir?
print(len(course)) #66 karakter

#2- "website" icinde www karakterlerini alin.
print(website[8:11]) #www
#3- "website icinden all karakterlerini alin.
length=len(website)
print(website[length-3:length]) #all
#4- "course" icinden ilk 15 ve son 15 karakterlerini alin.
print(course[0:15]) #Python Kursu:
print(course[-15:]) #riniz (40 saat)
#5-"course" ifadesindeki karakterleri tersten yazdirin.
print(course[::-1]) #)taas 04( zinirebher amalmargorp nohtyp anos natşaB :usruK nohtyP
#6-"course" ifadesindeki karakterleri 2'şer atlayarak yazdirin.
print(course[::2]) #PyhnKru atnsn yhnpormaarheii 4 at

#7- 'Benim adim Hakan Kara, yasim 46 ve meslegim futbol muhendisi' ifadesini degiskenlerle yazdirin.
name="Hakan"
surname="Kara"
age=46
job= "futbol muhendisi"
result='Benim adim '+ name +' '+ surname+ ', yasim '+ str(age)+ ' ve meslegim '+ job
print(result) #Benim adim Hakan Kara, yasim 46 ve meslegim futbol muhendisi
result='Benim adim {} {}, yasim {} ve meslegim {}'.format(name,surname,age,job)
print(result) #Benim adim Hakan Kara, yasim 46 ve meslegim futbol muhendisi
result=f'Benim adim {name} {surname}, yasim {age} ve meslegim {job}'
print(result) #Benim adim Hakan Kara, yasim 46 ve meslegim futbol muhendisi

#8- 'Hello world' ifadesindeki w harfini W ile degistirin
str='Hello world'
str=str[0:6]+ 'W'+str[-4::]
str=str.replace('w', 'W')
print(str) #Hello World

#9- 'abc' ifadesini 3 defa yazdirin
s='abc'
print(s*3) #abcabcabc