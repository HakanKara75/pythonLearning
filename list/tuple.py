tuple()

tup=(15, 58, 8966)
tup1=("Hakan", 575, 574.54, False)
tup4=tuple([2145,556,-578, 54.54, "gsdf", "gfsfsf", 487.5])

butunTup=tup1+tup+tup4

print(butunTup) #('Hakan', 575, 574.54, False, 15, 58, 8966, 2145, 556, -578, 54.54)

print(tup1[2])
print(tup1[3:])

print(tup4[0: len(tup1):3]) #3 er atlayarak

print(tup4[-1:0:-1]) #en sondan basla, 0'a kadar, 1'er eksilt

print(tup.count(575)) #kac tane 575 var

print(tup4.index(54.54)) #54.54'un indeksini verir




