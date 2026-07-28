# functions.py
# Functions & Recursions
# A function is a group of statements performing a specific task.
# When a program gets bigger in size and its complexity grows, it gets difficult for a program to keep track
# on which piece of code is doing what!
# A function can be reused by the programmer in a given program any number of times.

# Example And Syntax Of A Function
# The syntax of a function looks as follows:
def func1():
    print('hello')
# This function can be called any number of times, anywhere in the program.

# Function Call
# Whenever we want to call a function, we put the name of the function followed by parentheses as follows:
func1() # This is called function call.
# Function Definition
# The part containing the exact set of instructions which are executed during the function call


# Types Of Functions In Python
# There are two types of functions in python:
# Built in functions (Already present in python)
# User defined functions (Defined by the user)
# Examples of built in functions includes len(), print(), range() etc.
# The func1() function we defined is an example of user defined function


# Recursion
# Recursion is a function which calls itself.
# It is used to directly use a mathematical formula as function.

def factorial(n):
    if n>1:
        return 1
    else:
        return n*factorial(n-1)

def greet(name):
    print(f"Hello, {name}!")


def add(a, b):
    return a + b


def square(number):
    return number * number


def is_even(number):
    return number % 2 == 0


greet("Rahul")

result = add(10, 20)
print("Sum:", result)

print("Square:", square(7))

num = 8
if is_even(num):
    print(num, "is Even")
else:
    print(num, "is Odd")


# functions_concepts.py


# Basic Function

def greet():
    print("Hello, Python!")


greet()


# Functions With Arguments
# A function can accept some value it can work with. We can put these values in the parentheses.
# A function can also return value as shown below:
def greet_user(name):
    print("Hello,", name)


greet_user("Pavan")


# Function with return value

def add(a, b):
    return a + b


result = add(10, 20)

print("\nAddition:", result)


# Parameters vs Arguments

# a and b are parameters
def multiply(a, b):
    return a * b


# 5 and 4 are arguments
print("\nMultiplication:", multiply(5, 4))



# Function without return

def show_message():
    print("\nThis function has no return value")


value = show_message()

print("Returned value:", value)
# Output will be None



# Default Parameters
# Default Parameter Value
# We can have a value as default as default argument in a function
# If we specify course="Python" in the line containing def, this value is used when no argument is passed.


def student(name, course="Python"):
    print(name, course)


print("\nDefault Parameter:")
student("Pavan")
student("Rahul", "Java")



# *args - variable number of positional arguments

def add_numbers(*args):
    print("\nArgs:", args)
    
    total = 0
    
    for num in args:
        total += num
        
    return total


print("Sum:", add_numbers(1, 2, 3, 4))


# **kwargs - variable number of keyword arguments

def display_info(**kwargs):
    print("\nKwargs:")
    
    for key, value in kwargs.items():
        print(key, ":", value)


display_info(name="Pavan", age=21, city="Nagpur")



# Using *args and **kwargs together

def demo(*args, **kwargs):
    print("\nDemo args:", args)
    print("Demo kwargs:", kwargs)


demo(1, 2, name="Pavan", role="Developer")



# Lambda Function

square = lambda x: x * x

print("\nLambda Square:")
print(square(5))


# Lambda with multiple arguments

addition = lambda a, b: a + b

print("Lambda Addition:")
print(addition(10, 20))



# Lambda with sorted()

students = [
    ("Rahul", 85),
    ("Pavan", 95),
    ("Amit", 75)
]

sorted_students = sorted(
    students,
    key=lambda student: student[1]
)

print("\nSorted Students:")
print(sorted_students)



# Lambda with map()

numbers = [1, 2, 3, 4, 5]

squared_numbers = list(
    map(lambda x: x * x, numbers)
)

print("\nMap Example:")
print(squared_numbers)



# Lambda with filter()

even_numbers = list(
    filter(lambda x: x % 2 == 0, numbers)
)

print("\nFilter Example:")
print(even_numbers)
