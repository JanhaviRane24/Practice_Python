# variables.py
#A variable is the name given to a memory location in a program. For example.
# variables = container to store a value
# keywords = reserved words in python
# identifiers = class/function/variable name
#Rules for Choosing an Identifier
# A variable name can contain alphabets, digits, and underscores.
# A variable name can only start with an alphabet and underscores.
# A variable name canʼt start with a digit.
# No white space is allowed to be used inside a variable name.
# Examples of a few variable names are: harry, one8, seven_, _seven etc

# Integer
age = 21

# Float
height = 5.8

# String
name = "John"

# Boolean
is_student = True

print("Name:", name)
print("Age:", age)
print("Height:", height)
print("Student:", is_student)

# Multiple variable assignment
x, y, z = 10, 20, 30
print("x =", x)
print("y =", y)
print("z =", z)

# Same value to multiple variables
a = b = c = 100
print("a =", a)
print("b =", b)
print("c =", c)

# Dynamic typing
value = 50
print("Value:", value)

value = "Python"
print("Updated Value:", value)

# Variable swapping
first = 5
second = 10

first, second = second, first

print("First:", first)
print("Second:", second)
