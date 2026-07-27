# modules_packages.py


# Importing built-in modules

import math
import random
import datetime
import os


# math module

print("Math Module:")

number = 25

print("Square Root:", math.sqrt(number))
print("Power:", math.pow(2, 3))
print("Ceil:", math.ceil(4.3))
print("Floor:", math.floor(4.8))



# Import specific function from module

from random import randint

print("\nRandom Module:")

print("Random Number:", randint(1, 10))



# Using random module

print("\nRandom Choice:")

fruits = ["Apple", "Banana", "Mango"]

print(random.choice(fruits))



# datetime module

print("\nDatetime Module:")

current_time = datetime.datetime.now()

print("Current Date and Time:")
print(current_time)

print("Year:", current_time.year)
print("Month:", current_time.month)
print("Day:", current_time.day)



# os module

print("\nOS Module:")

print("Current Directory:")
print(os.getcwd())



# List files in current directory

print("\nFiles in Directory:")

files = os.listdir()

for file in files:
    print(file)



# Creating and importing your own module example

# Suppose we have another file:
#
# calculator.py
#
# def add(a, b):
#     return a + b
#
# We can import it:
#
# import calculator
#
# print(calculator.add(5, 10))


# Package example

# Project structure:
#
# my_package/
#     __init__.py
#     module1.py
#     module2.py
#
# Import:
#
# from my_package import module1

"""
Interview points:

Module vs Package

Module:

calculator.py

A single Python file.
Contains functions, classes, or variables.
Package:

my_package/
    __init__.py
    math_tools.py
    string_tools.py

A folder containing multiple modules.
__init__.py traditionally marks it as a package.

"""

"""
Installing third-party packages:

Example:

pip install requests

Then use:

import requests

A module is like one toolbox, while a package is like a box containing multiple toolboxes.



"""