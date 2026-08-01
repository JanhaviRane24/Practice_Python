# 12. enumerate() Function in Python
# What is enumerate()?

# The enumerate() function adds an index (counter) to each element of an iterable (like a list, tuple, string, etc.) and returns an enumerate object.

# Instead of writing your own counter variable, Python does it automatically.

# Why Do We Need enumerate()?

# Suppose you want to print both the index and the value of each item.

# Without enumerate()
# list1 = ["Harry", "Rohan", "Shubham"]

# index = 0

# for item in list1:
#     print(index, item)
#     index += 1
# Output
# 0 Harry
# 1 Rohan
# 2 Shubham
# Step-by-Step
# index = 0

# ↓

# Print
# 0 Harry

# ↓

# index = 1

# ↓

# Print
# 1 Rohan

# ↓

# index = 2

# ↓

# Print
# 2 Shubham

# Notice we had to:

# Create a counter variable.
# Increase it manually.
# Using enumerate()
# list1 = ["Harry", "Rohan", "Shubham"]

# for index, item in enumerate(list1):
#     print(index, item)
# Output
# 0 Harry
# 1 Rohan
# 2 Shubham

# Python automatically provides:

# index
# item

# No need to create or increment a counter.

# Step-by-Step Execution
# list1 = ["Harry", "Rohan", "Shubham"]

# Memory

# Index      Value

# 0          Harry
# 1          Rohan
# 2          Shubham

# Loop

# First Iteration
# index = 0
# item = Harry

# Print

# 0 Harry
# Second Iteration
# index = 1
# item = Rohan

# Print

# 1 Rohan
# Third Iteration
# index = 2
# item = Shubham

# Print

# 2 Shubham
# How Does enumerate() Work?
# list1 = ["A", "B", "C"]

# print(list(enumerate(list1)))
# Output
# [(0, 'A'), (1, 'B'), (2, 'C')]

# Notice:

# enumerate() returns pairs of:

# (index, value)

# Like this:

# (0, 'A')

# (1, 'B')

# (2, 'C')

# The for loop automatically unpacks each tuple into two variables:

# for index, item in enumerate(list1):

# is equivalent to:

# (index, item)

# ↓

# (0, "A")

# ↓

# index = 0

# item = "A"
# Example 2 – Printing Student Roll Numbers
# students = ["Alice", "Bob", "Charlie"]

# for roll_no, student in enumerate(students):
#     print(roll_no, student)

# Output

# 0 Alice
# 1 Bob
# 2 Charlie
# Example 3 – Starting the Counter from 1

# By default, counting starts from 0.

# You can change it using the start parameter.

# students = ["Alice", "Bob", "Charlie"]

# for roll_no, student in enumerate(students, start=1):
#     print(roll_no, student)
# Output
# 1 Alice
# 2 Bob
# 3 Charlie
# Step-by-Step
# start = 1

# ↓

# First Student

# ↓

# Index = 1

# ↓

# Second Student

# ↓

# Index = 2

# ↓

# Third Student

# ↓

# Index = 3
# Example 4 – Strings

# enumerate() also works with strings.

# word = "Python"

# for index, letter in enumerate(word):
#     print(index, letter)
# Output
# 0 P
# 1 y
# 2 t
# 3 h
# 4 o
# 5 n
# Example 5 – Tuples
# numbers = (10, 20, 30)

# for index, value in enumerate(numbers):
#     print(index, value)
# Output
# 0 10
# 1 20
# 2 30
# Example 6 – Finding an Item
# fruits = ["Apple", "Banana", "Orange"]

# for index, fruit in enumerate(fruits):
#     if fruit == "Banana":
#         print("Found at index:", index)
# Output
# Found at index: 1
# Example 7 – Numbered Menu
# menu = ["Pizza", "Burger", "Pasta"]

# for number, item in enumerate(menu, start=1):
#     print(number, item)
# Output
# 1 Pizza
# 2 Burger
# 3 Pasta

# This is commonly used in console applications.

# What Does enumerate() Return?
# numbers = [10, 20, 30]

# result = enumerate(numbers)

# print(result)
# Output
# <enumerate object at 0x...>

# This is an enumerate object (an iterator).

# To see its contents:

# print(list(result))
# Output
# [(0, 10), (1, 20), (2, 30)]
# Difference Between Normal Loop and enumerate()
# Normal Loop
# fruits = ["Apple", "Banana", "Orange"]

# for fruit in fruits:
#     print(fruit)

# Output

# Apple
# Banana
# Orange

# No index is available.

# Using enumerate()
# fruits = ["Apple", "Banana", "Orange"]

# for index, fruit in enumerate(fruits):
#     print(index, fruit)

# Output

# 0 Apple
# 1 Banana
# 2 Orange

# Now you have both the index and the value.

# Interview Questions
# 1. What is enumerate()?

# Answer:
# enumerate() is a built-in function that adds an index (counter) to each item of an iterable and returns an enumerate object.

# 2. Why do we use enumerate()?

# Answer:
# It lets us access both the index and the value while looping, without maintaining a separate counter variable.

# 3. Does enumerate() start counting from 0?

# Answer:
# Yes, by default it starts from 0, but you can change the starting value using the start parameter.

# Example:

# for index, value in enumerate(["A", "B"], start=1):
#     print(index, value)

# Output:

# 1 A
# 2 B
# 4. What does enumerate() return?

# Answer:
# It returns an enumerate object, which is an iterator that produces (index, value) pairs.

# Summary
# Feature	Description
# Purpose	Adds an index to an iterable
# Default Start	0
# Custom Start	enumerate(iterable, start=1)
# Returns	An enumerate object (iterator)
# Common Use	Access index and value together in a loop
# Quick Revision
# names = ["Harry", "Rohan", "Shubham"]

# # Default indexing
# for index, name in enumerate(names):
#     print(index, name)

# # Start from 1
# for index, name in enumerate(names, start=1):
#     print(index, name)

# # See the actual output of enumerate()
# print(list(enumerate(names)))

# Output:

# 0 Harry
# 1 Rohan
# 2 Shubham

# 1 Harry
# 2 Rohan
# 3 Shubham

# [(0, 'Harry'), (1, 'Rohan'), (2, 'Shubham')]