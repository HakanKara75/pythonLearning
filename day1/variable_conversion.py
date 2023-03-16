c = input("1.sayi: ")
d = input("2. sayi: ")
toplam = int(c) + int(d)  # bunu yapmazsak asagida c ve d yi yan yana yazdirir. string olarak algilar.
print(toplam)

x = 5
y = 35.34
name = 'Hakan'
isOnline = False
print(type(x))
print(type(y))
print(type(name))
print(type(isOnline))

# Type conversion
# int to float
x = 45
x = float(x)
print(x)
print(type(x))  # 45.0

# float to int
y = 45.34
y = int(y)
print(y)
print(type(y))  # 45

# int to string
result = str(x) + str(y)
print(result)
print(type(result))  # 45.045

# boolean to string
isOnline = str(isOnline)
print(isOnline)  # False
print(type(isOnline))

