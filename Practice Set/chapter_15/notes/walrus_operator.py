# 1. Walrus Operator (:=) (Python 3.8+)
# What is the Walrus Operator?

# The Walrus Operator (:=) lets you assign a value to a variable while using it in an expression.

# Before Python 3.8, you had to assign first and then use the variable.

# Without Walrus Operator
numbers = [10, 20, 30, 40]

length = len(numbers)

if length > 3:
    print("Length is:", length)
# Output
# Length is: 4
# Step-by-Step
# numbers list is created.
# len(numbers) returns 4.
# 4 is stored in length.
# Condition checks 4 > 3.
# Prints the result.
# With Walrus Operator
# numbers = [10, 20, 30, 40]

if (length := len(numbers)) > 3:
    print("Length is:", length)
# Output
# Length is: 4
# Step-by-Step
# len(numbers)
# ↓
# 4

# (length := 4)
# ↓
# length becomes 4

# Check:
# 4 > 3
# ↓
# True

# Print:
# Length is: 4

# Notice that assignment and checking happen together.

# Example 2

# Without Walrus

name = input("Enter your name: ")

if name:
    print("Hello", name)

# Suppose user enters

# Rahul

# Output

# Hello Rahul

# With Walrus

if (name := input("Enter your name: ")):
    print("Hello", name)

# Same Output

# Enter your name: Rahul
# Hello Rahul
# Example 3

# Finding square

if (square := 5 * 5) > 20:
    print(square)
# Step-by-Step
# 5 * 5 = 25

# square = 25

# 25 > 20
# True

# Print 25

# Output

# 25
# Why use Walrus?

# Without Walrus
data = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]
length = len(data)

if length > 10:
    print(length)

# With Walrus

if (length := len(data)) > 10:
    print(length)

# Less code and no repeated calculation.