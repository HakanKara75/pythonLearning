name='Hakan'
surname='Kara'
age=46

greting= "My name is "+name+ ' surname is '+ surname+ ' and \nI am '+ str(age)+ ' years old.'
print(greting)

length=len(greting)
print(greting[0]) #0. karakter M
print(greting[2]) #2. karakter bosluk
print(greting[12]) #12. karakter a
print(greting[22]) #22. karakter m
print(greting[length-1]) #son karakter (.)
print(greting[3:7]) #3 ten 7. karaktere kadar name
print(greting[8:]) #8 den son karaktere kadar is Hakan surname is Kara and I am 46 years old.
print(greting[4:36:2]) #4 ten 36. karaktere kadar 2 şer atlayarak (aei aa unm sKr n)

