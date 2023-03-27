# -*- coding: utf-8 -*-
"""
Created on Mon Mar 27 14:08:03 2023

@author: Hakan Batirhan
"""

x = 12
y = ---x
print(y)

z= ++++++++15
print(z)
z = - z
print(z)


x = 5
y = 43

print(x is y) #false hem tip hem degere bakar

x= 546
y= 546

print(x is y) #true hem tip hem degere bakar

a= 5456
b= 5456.12

print(a is b) #false

print(x is not y) #false
print(a is not b) #true

#print(45 is 45)

k1 = 2 < 3 #boolean True
print((2<3) is True) #True
print(type(2<3), 2<3) #True
print(type(True), True) #True