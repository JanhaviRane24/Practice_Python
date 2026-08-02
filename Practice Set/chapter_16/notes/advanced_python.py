# Advanced Python 2
# Virtual Environment
# CHAPTER 13
# An environment which is same as the system interpreter but is isolated from the other Python environments
# on the system.
# Installation
# To use virtual environments, we write:
# pip install virtualenv
# We create a new environment using:
# virtualenv myprojectenv
# The next step after creating the virtual environment is to activate it.
# We can now use this virtual environment as a separate Python installation.

# Pip Freeze Command
# ‘pip freezeʼ returns all the package installed in a given python environment along with the versions.
# pip freeze > requirements.txt
# The above command creates a file named ‘requirements.txtʼ in the same directory containing the output of
# ‘pip freezeʼ.
# We can distribute this file to other users, and they can recreate the same environment using:
# pip install -r requirements.txt

# Lambda Functions
# Function created using an expression using ‘lambdaʼ keyword.
# Syntax:
# lambda arguments: expression
# Example:
# square = lambda x:x*x
# square(6)
# sum = lambda a,b,c:a+b+c
# sum(1,2,3)

# Join Method (Strings)

# Creates a string from iterable objects.
# l = ["apple", "mango", "banana"]
# result = ", and, ".join(l)
# print(result)
# The above line will return: “apple,and,mango,and,banana”.

# Format Method (Strings)
# Formats the values inside the string into a desired output.
# template.format(p1,p2...)
# Syntax:
# "{} is a good {}".format("harry", "boy")
# "{1} is a good {0}".format("harry", "boy")

# Map, Filter & Reduce
# Map applies a function to all the items in an input_list.
# Syntax:
# map(function, input_list)
# Filter creates a list of items for which the function returns true.
# list(filter(function))
# Reduce applies a rolling computation to sequential pair of elements.
# from functools import reduce
# val = reduce(function, list1)
# If the function computes sum of two numbers and the list is [1,2,3,4]
# 1 2 3 4
# 3 3 4
# 6 4
# 10
# Sequential Computation