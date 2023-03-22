message='Hello There. My name is Hakan Kara'.split(" ")
print(message[0]) #Hello

list= [1,2,3]
list= ["araba",2,True, 345.34]

list1=["one","two","three"]
list2=["four","five","six", 345, 33.3, False]
result=list1+list2
print(result) #['one', 'two', 'three', 'four', 'five', 'six', 345, 33.3, False]
print(len(result)) #kac eleman var onu verir

userA=["Hakan", 46]
userB=["Pinar", 45]
users=[userA]+[userB] # liseyi 2 elemanli hale getirdi.
print(users) #[['Hakan', 46], ['Pinar', 45]]
print(users[1][0]) #Pinar













