# exception_handling.py


# Basic try-except example

print("Basic Exception Handling:")

try:
    number = 10 / 0
    print(number)

except ZeroDivisionError:
    print("Cannot divide by zero")



# Multiple except blocks

print("\nMultiple Exceptions:")

try:
    value = int(input("Enter a number: "))
    result = 100 / value
    print("Result:", result)

except ValueError:
    print("Please enter a valid integer")

except ZeroDivisionError:
    print("Number cannot be zero")



# IndexError

print("\nIndex Error:")

numbers = [10, 20, 30]

try:
    print(numbers[5])

except IndexError:
    print("Index does not exist")



# KeyError

print("\nKey Error:")

student = {
    "name": "Pavan",
    "age": 21
}

try:
    print(student["city"])

except KeyError:
    print("Key does not exist")



# TypeError

print("\nType Error:")

try:
    result = "10" + 5

except TypeError:
    print("Cannot add string and integer")



# try-except-else-finally

print("\nElse and Finally Example:")

try:
    num = 10 / 2

except ZeroDivisionError:
    print("Division error")

else:
    print("No exception occurred")
    print("Result:", num)

finally:
    print("This block always executes")



# Custom Exception

print("\nCustom Exception:")


class InsufficientBalanceError(Exception):
    pass



def withdraw(balance, amount):

    if amount > balance:
        raise InsufficientBalanceError("Not enough balance")

    return balance - amount



try:
    remaining_balance = withdraw(5000, 6000)
    print("Remaining Balance:", remaining_balance)

except InsufficientBalanceError as error:
    print(error)



# Difference between bare except and specific exception

print("\nSpecific Exception Example:")

try:
    x = int("abc")

except ValueError:
    print("Value conversion failed")


# Avoid using:
#
# except:
#     print("Something went wrong")
#
# because it catches every error and can hide bugs.


# 7. Exception Handling in Python
# What is an Exception?

# An exception is an error that occurs while the program is running (runtime).

# When an exception occurs, Python normally stops the program immediately.

# Example Without Exception Handling
num1 = 10
num2 = 0

print(num1 / num2)

print("Program End")
# Output
# ZeroDivisionError: division by zero

# Notice

# print("Program End")

# never executes because the program stops at the error.

# Why Do We Need Exception Handling?

# Suppose you're building:

# ATM Software
# Banking Application
# Hospital Management System
# E-commerce Website

# Imagine the program crashes because the user enters invalid input.

# That would be a poor user experience.

# Instead of crashing, we can handle the error gracefully.

# What is try?

# The try block contains code that might cause an exception.

# try:
#     # Risky code
# What is except?

# The except block runs only if an exception occurs.

# Syntax

# try:
#     # Risky Code
# except:
#     # Handle Error
# Example 1
try:
    print(10 / 0)
except:
    print("An error occurred.")
# Step-by-Step
# try block starts

# ↓

# 10 / 0

# ↓

# ZeroDivisionError occurs

# ↓

# Python jumps to except

# ↓

# Print

# An error occurred.

# Output

# An error occurred.

# The program does not crash.

# Example 2
try:
    number = int(input("Enter Number: "))
    print(number)
except:
    print("Please enter a valid integer.")
# User Input
# abc
# Execution
# Input

# ↓

# abc

# ↓

# int("abc")

# ↓

# ValueError

# ↓

# except executes

# ↓

# Please enter a valid integer.

# Output

# Please enter a valid integer.
# Catching Specific Exceptions

# Instead of catching every error, catch only the one you expect.

# Syntax

# try:
#     ...
# except ZeroDivisionError:
#     ...
# Example
try:
    print(10 / 0)
except ZeroDivisionError:
    print("Cannot divide by zero.")

# Output

# Cannot divide by zero.
# Multiple except Blocks

# A program can have different types of errors.

# Example

try:
    number = int(input("Enter Number: "))
    print(10 / number)

except ValueError:
    print("Please enter a valid integer.")

except ZeroDivisionError:
     print("Number cannot be zero.")
# Case 1

# Input

# 0

# Execution

# Input

# ↓

# 0

# ↓

# 10 / 0

# ↓

# ZeroDivisionError

# ↓

# Second except runs

# Output

# Number cannot be zero.
# Case 2

# Input

# abc

# Execution

# Input

# ↓

# abc

# ↓

# int("abc")

# ↓

# ValueError

# ↓

# First except runs

# Output

# Please enter a valid integer.
# Exception Object

# Sometimes we want to know what the actual error message is.

# Syntax

# except Exception as e:

# Here,

# Exception is the base class for most built-in exceptions.
# e stores the exception object.
# Example
try:
    print(10 / 0)
except Exception as e:
    print(e)

# Output

# division by zero

# Notice

# Instead of writing

# Cannot divide by zero

# Python prints the actual error message.

# Another Example
try:
    int("Hello")
except Exception as e:
    print(e)

# Output

# invalid literal for int() with base 10: 'Hello'
# Should We Always Use except Exception?

# Usually no.

# It's better to catch the specific exception you expect.

# ✅ Good

try:
    print(10 / 0)
except ZeroDivisionError:
    print("Division by zero is not allowed.")

# ❌ Less preferred

try:
    print(10 / 0)
except Exception:
    print("Some error occurred.")

# Why?

# Because specific exceptions make debugging easier and avoid hiding unexpected bugs.

# Flow Diagram
# No Error
# try

# ↓

# No Exception

# ↓

# Skip except

# ↓

# Continue Program
# Error Occurs
# try

# ↓

# Exception

# ↓

# Jump to matching except

# ↓

# Continue Program
# Common Built-in Exceptions
# Exception	When It Occurs
# ZeroDivisionError	Divide by zero
# ValueError	Invalid value (e.g., int("abc"))
# TypeError	Unsupported operation between types
# IndexError	List index out of range
# KeyError	Dictionary key not found
# FileNotFoundError	File does not exist
# NameError	Variable not defined
# Example of IndexError
numbers = [10, 20, 30]

try:
    print(numbers[5])
except IndexError:
    print("Index is out of range.")

# Output

# Index is out of range.
# Example of KeyError
student = {
    "name": "Alice"
}

try:
    print(student["age"])
except KeyError:
    print("Key not found.")

# Output

# Key not found.
# Interview Questions
# 1. What is an exception?

# Answer:
# An exception is a runtime error that interrupts the normal execution of a program.

# 2. Why do we use exception handling?

# Answer:
# To prevent the program from crashing and handle runtime errors gracefully.

# 3. What is the difference between try and except?
# try	except
# Contains code that may raise an exception	Handles the exception if one occurs
# 4. What does Exception as e do?

# It stores the exception object in the variable e, allowing you to access the actual error message.

# Example:

try:
    print(10 / 0)
except Exception as e:
    print("Error:", e)

# Output:

# Error: division by zero
# Summary So Far
# Keyword	Purpose
# try	Contains risky code
# except	Handles exceptions
# Multiple except	Handles different exception types separately
# Exception as e	Gives access to the actual error message