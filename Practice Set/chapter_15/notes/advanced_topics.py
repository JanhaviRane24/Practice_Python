# Walrus Operator
# CHAPTER 12
# The walrus operator (:=), introduced in Python 3.8, allows you to assign values to variables as part of an expression.
# # Using Walrus operator
# if (n := len([1, 2, 3, 4, 5])) > 3:
# print(f"List is too long ({n} elements, expected <= 3)")
# In this example, n is assigned the value of len([1, 2, 3, 4, 5]) and then used in the comparison within the if statement.
# Types Definitions In Python
# Type hints are added using the colon (:) syntax for variables and the -> syntax for function return types.
# # Variable type hint
# age: int = 25
# # Function type hints
# def greeting(name: str) -> str:
# return f"Hello, {name}!"
# # Usage
# print(greeting("Alice"))
# Advanced Type Hints
# Python's typing module provides more advanced type hints, such as List, Tuple, Dict and Union.
# from typing import List, Tuple, Dict, Union
# from typing import List, Tuple, Dict, Union
# # List of integers
# numbers: List[int] = [1, 2, 3, 4, 5]
# # Tuple of a string and an integer
# person: Tuple[str, int] = ("Alice", 30)
# # Dictionary with string keys and integer values
# scores: Dict[str, int] = {"Alice": 90, "Bob": 85}
# # Union type
# identifier: Union[int, str] = "ID123"
# Python Programming Handbook
# Beginner Friendly Learning Guide
# Match Case
# CHAPTER 12
# Python 3.10 introduced the match statement, which is similar to the switch statement found in other programming
# languages.
# def http_status(status):
# match status:
# case 200:
# return "OK"
# case 404:
# return "Not Found"
# case 500:
# return "Internal Server Error"
# case _:
# return "Unknown status"
# print(http_status(200))
# print(http_status(404))
# Dictionary Merge & Update Operators
# New operators | and |= allow for merging and updating dictionaries.
# dict1 = {'a': 1, 'b': 2}
# dict2 = {'b': 3, 'c': 4}
# merged = dict1 | dict2
# print(merged)
# with (
# open('file1.txt') as f1,
# open('file2.txt') as f2
# ):
# # Process files
# pass
# Python Programming Handbook
# Beginner Friendly Learning Guide
# Exception Handling In Python
# There are many built-in exceptions which are raised in python when something goes wrong.
# try:
# # Code which might throw exception
# print(10 / 0)
# except Exception as e:
# print(e)
# try:
# # Code
# except ZeroDivisionError:
# # Code
# except TypeError:
# # Code
# except:
# # All other exceptions
# Raising Exceptions
# We can raise custom exceptions using the raise keyword in python.
# age = -5
# if age < 0:
# raise ValueError("Age cannot be negative")
# Try With Else Clause
# try:
# # Some code
# except:
# # Some code
# else:
# # Executed if try was successful
# Try With Finally
# try:
# # Some code
# except:
# # Some code
# CHAPTER 12
# finally:
# # Executed regardless of error
# Python Programming Handbook
# Beginner Friendly Learning Guide
# If __name__ == '__main__' In Python
# '__name__' evaluates to the name of the module in python from where the program is ran.
# If the module is being run directly from the command line, the '__name__' is set to string "__main__".
# Thus, this behaviour is used to check whether the module is run directly or imported to another file.
# if __name__ == "__main__":
# print("Running directly")
# CHAPTER 12
# The Global Keyword
# 'global' keyword is used to modify the variable outside of the current scope.
# x = 10
# def change():
# global x
#     x 
# = 20
# Enumerate Function In Python
# The 'enumerate' function adds counter to an iterable and returns it.
# list1 = ["Harry", "Rohan", "Shubham"]
# for i, item in enumerate(list1):
# print(i, item)
# List Comprehensions
# List Comprehension is an elegant way to create lists based on existing lists.
# list1 = [1,7,12,11,22]
# list2 = [item for item in list1 if item > 8]
# Python Programming Handbook
# Beginner Friendly Learning Guide
# Practice Set
# CHAPTER 12
# 1. Write a program to open three files 1.txt, 2.txt and 3.txt. If any of these files are not
# present, a message without exiting the program must be printed prompting the same.
# 2. Write a program to print third, fifth and seventh element from a list using enumerat