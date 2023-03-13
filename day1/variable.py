# 5 variables: integer, float, string, boolean, sequences, dictionaries
x=3 #integer
y=x*5
print("y : ",y)

pi=3.14 #float
a=pi+x
print("a : ",a)

ilkharf= "A" #string
print("ilkharf karakter uzunlugu :",len (ilkharf)) #karakter uzunlugunu verir

mybool= True # boolean

mylist=[0,123, "for you", 4.5, False] #sequences

mydict= {"one": 1, "two": 2} #dictionaries

#re-declare variable
x="Hello" #chanced variable type int to string
print(x)
mybool=123423 #chanced variable type boolean to integer
print(mybool)

kullaniciadi="hakan"
parola="112proje"
print("kullaniciadi karakter uzunlugu :",len(kullaniciadi))
print("parola karakter uzunlugu : " ,len(parola))

a=kullaniciadi+parola
print("kullaniciadi ve parola birlesimi : ",a)

print(len(kullaniciadi)+len(parola))

#access to a member of a sequence type, use []
print(mylist[3])

#use slices to get parts of a sequence
print("slices",mylist[1:4])
print(mylist[0:4:2]) #start index: end index: step value

#reverse a sequence
print(mylist[ ::-1]) # start value: end value: step value (-1)