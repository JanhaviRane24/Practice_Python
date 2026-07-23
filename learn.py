n=5
print(n)
# output:
# 5

str="Janhavi"
print(str)
# output:
# Janhavi

flag="True"
flag="False"
print(flag)
# output:
# False (as second flag replace or overwrite the first value)


#This is a comment.

"""
This is a comment
written in
more than just one line
"""

if 5 > 2:
  print("Five is greater than two!")
#Five is greater than two!
  #indentation is important in python indentation is like brackets
  # in java tell which which code belong to which block
  #usually we take 4 space as indentation

print("Hello World!", end=" ")
print("Python")
#hello to python
#we use end="" to end print statements with
#we use print statements to print output in python

a=45
print("my weight is :",a)
#my weight is : 45

w=input("enter a value: ")
#we use input function to take values from user
print(w)
#enter a value: 4
#4


#You can also do math inside the print() function:
print(3 + 3)
print(2 * 5)


#Casting
#If you want to specify the data type of a variable, this can be done with casting.
x = input(3)    # x will be '3'
y = int(3)    # y will be 3
z = float(3)  # z will be 3.0

#You can get the data type of a variable with the type() function.
x = 5
y = "John"
print(type(x))
print(type(y))

#many values to many variables
x, y, z = "Orange", "Banana", "Cherry"
print(x)
print(y)
print(z)

#unpack collection
fruits = ["apple", "banana", "cherry"]
x, y, z = fruits
print(x)
print(y)
print(z)

#output variables
x = "Python"
y = "is"
z = "awesome"
print(x, y, z)

#Notice the space character after "Python " and "is ", 
# without them the result would be "Pythonisawesome".
x = "Python "
y = "is "
z = "awesome"
print(x + y + z)

#global variables
#Variables that are created outside of a function 
# (as in all of the examples in the previous pages) are known as global variables.

#Global variables can be used by everyone, both inside of functions and outside.


x = "awesome"

def myfunc():
  print("Python is " + x)

myfunc()

#If you create a variable with the same name inside a function, 
# this variable will be local, and can only be used inside the function.
#  The global variable with the same name will remain as it was, 
# global and with the original value.
x = "awesome"

def myfunc():
  x = "fantastic"
  print("Python is " + x)

myfunc()

print("Python is " + x)

