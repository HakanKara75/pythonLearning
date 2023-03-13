# 
# Example file for variables
# LinkedIn Learning Python course by Joe Marini
#


# Basic data types in Python: Numbers, Strings, Booleans, Sequences, Dictionaries
myint = 5                   #global variable
myfloat = 13.2              #global variable
mystr = "This is a string"  #global variable
mybool = True                  #global variable
mylist = [0, 1, "two", 3.2, False]      #global variable
mytuple = (0, 1, 2)                     #global variable
mydict = {"one" : 1, "two" : 2}  # key:value == > key is unique, value not.

print(myint)
print(myfloat)
print(mystr)
print(mybool)
print(mylist)
print(mytuple)
print(mydict)

# re-declaring a variable works
myint="abc"
print(myint)
# to access a member of a sequence type, use []
print(mylist[2]) #index 0 dan başlar, 3.elman olur.
print(mytuple[1]) #index 0 dan başlar, 2.elman olur.
# use slices to get parts of a sequence
print(mylist[1:5])
print(mylist[1:5:2]) #start index: end index : step value
# you can use slices to reverse a sequence
print(mylist[::-1]) #reverse order
# dictionaries are accessed via keys
print(mydict["one"]) #key. output value
# ERROR: variables of different types cannot be combined
print("string type"+ str(123)) #turn variable type
# Global vs. local variables in functions
def someFunction():
    global mystr  # changed local to global
    mystr="def"     #local variable

    print(mystr)

someFunction()
print(mystr) #print global mystr.

del mystr #delete