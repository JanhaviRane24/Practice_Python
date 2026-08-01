# 11. if __name__ == "__main__"
# Why Do We Need It?

# Imagine you create a Python file that contains useful functions.

# Example:

# def add(a, b):
#     return a + b

# print(add(10, 20))

# Now another file imports this file.

# What do you expect?

# Only the function should be imported.

# But something unexpected happens...

# Understanding __name__

# Every Python file has a special built-in variable called:

# __name__

# Python automatically assigns a value to it.

# The value depends on how the file is executed.

# There are only two possibilities.

# Case 1: File is Run Directly

# Suppose you execute

# python test.py

# Python sets

# __name__ = "__main__"
# Case 2: File is Imported

# Suppose another file imports it.

# import test

# Now Python sets

# __name__ = "test"

# Notice

# The value becomes the module (file) name, not "__main__".

# Example 1

# Create a file called

# hello.py
# print(__name__)

# Run

# python hello.py

# Output

# __main__

# Because Python executed this file directly.

# Example 2

# Create another file.

# hello.py
# print(__name__)
# main.py
# import hello

# Now run

# python main.py

# Output

# hello

# Why?

# Because

# main.py is the main program.
# hello.py is imported as a module.

# Therefore

# __name__ = "hello"

# inside hello.py.

# Problem Without if __name__ == "__main__"

# Suppose we have

# calculator.py
# def add(a, b):
#     return a + b

# print("Calculator Started")
# main.py
# import calculator

# print(calculator.add(10, 20))
# What happens?

# Python first imports

# calculator.py

# While importing,

# Python executes every line in the file.

# Execution

# Import calculator

# ↓

# Define add()

# ↓

# Print
# Calculator Started

# ↓

# Return to main.py

# ↓

# Print answer

# Output

# Calculator Started
# 30

# Question:

# Did we want

# Calculator Started

# to print?

# No.

# We only wanted the function.

# Solution

# Use

# if __name__ == "__main__":
# # calculator.py
# def add(a, b):
#     return a + b

# if __name__ == "__main__":
#     print("Calculator Started")
# main.py
# import calculator

# print(calculator.add(10, 20))

# Output

# 30

# Now

# Calculator Started

# does not print.

# Why?

# Because

# __name__

# inside calculator becomes

# calculator

# not

# __main__
# Step-by-Step Execution

# Run

# python main.py

# Execution

# main.py starts

# ↓

# Import calculator

# ↓

# Python sets

# __name__ = "calculator"

# ↓

# Check

# __name__ == "__main__"

# ↓

# False

# ↓

# Skip print

# ↓

# Return to main.py

# ↓

# Print

# 30
# When Running calculator.py Directly

# Now execute

# python calculator.py

# Execution

# calculator.py starts

# ↓

# Python sets

# __name__ = "__main__"

# ↓

# Check

# True

# ↓

# Print

# Calculator Started

# Output

# Calculator Started
# Visual Diagram
# Running Directly
# calculator.py

# ↓

# __name__

# ↓

# "__main__"

# ↓

# Condition True

# ↓

# Execute code
# Importing
# main.py

# ↓

# import calculator

# ↓

# __name__

# ↓

# "calculator"

# ↓

# Condition False

# ↓

# Skip code
# Real-Life Analogy

# Imagine a TV remote.

# The remote has many buttons:

# Volume
# Channel
# Power

# When another device uses the remote's functions, you don't want the TV to automatically turn on.

# You only want to use the function you requested.

# Similarly:

# Functions and classes should always be available for importing.
# Testing or demo code should run only when the file is executed directly.
# Real-World Example
# math_utils.py
def square(n):
    return n * n

def cube(n):
    return n * n * n

if __name__ == "__main__":
    print(square(5))
    print(cube(5))
# # app.py
# import math_utils

# print(math_utils.square(10))

# Output

# 100

# Notice

# Python doesn't print

# 25
# 125

# because that testing code is protected by

# if __name__ == "__main__":
# Why Do We Use It?

# Suppose your module contains

# 50 functions
# 10 classes

# You also want to test them.

# Instead of creating another test file, you can write

# if __name__ == "__main__":
#     # Test code here

# When importing the module elsewhere:

# Functions are imported.
# Classes are imported.
# Test code does not run.
# Interview Questions
# 1. What is __name__?

# Answer:
# __name__ is a built-in variable that stores the name of the current module.

# 2. When does __name__ become "__main__"?

# Answer:
# When the Python file is executed directly.

# Example:

# python app.py
# 3. What is the value of __name__ when a file is imported?

# Answer:
# It becomes the module (file) name.

# Example:

# import calculator

# Inside calculator.py:

# __name__ == "calculator"
# 4. Why do we use if __name__ == "__main__"?

# Answer:
# It ensures that specific code (such as testing or demonstration code) runs only when the file is executed directly, and not when it is imported into another module.

# Summary Table
# Situation	Value of __name__	if __name__ == "__main__"
# Run file directly	"__main__"	✅ Executes
# Import file	Module name (e.g., "calculator")	❌ Skipped
# Quick Revision
# calculator.py

def add(a, b):
    return a + b

if __name__ == "__main__":
    print(add(2, 3))
# main.py

# import calculator

# print(calculator.add(10, 20))
# Output when running calculator.py
# 5
# Output when running main.py
# 30
# Interview Tip

# A common misconception is that if __name__ == "__main__" is required in every Python file. It isn't.

# Use it only if the file contains code that should run only when executed directly, such as:

# Test code
# Demo examples
# Command-line entry points

# If a file only defines functions or classes and has no executable test code, you don't need this check.