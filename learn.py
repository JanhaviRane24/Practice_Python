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
x = str(3)    # x will be '3'
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
