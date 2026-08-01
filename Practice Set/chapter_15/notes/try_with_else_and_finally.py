# 8. else with try
# What is else?

# The else block executes only if no exception occurs in the try block.

# Syntax
# try:
#     # Risky code
# except SomeException:
#     # Handle exception
# else:
#     # Executes only if try succeeds
# Example 1
try:
    num = int(input("Enter a number: "))
    print(10 / num)

except ZeroDivisionError:
    print("Cannot divide by zero.")

except ValueError:
    print("Please enter a valid integer.")

else:
    print("Program executed successfully.")
# Case 1

# Input

# 2
# Step-by-Step
# try starts

# ↓

# num = 2

# ↓

# 10 / 2

# ↓

# 5.0

# ↓

# No exception

# ↓

# except blocks skipped

# ↓

# else executes
# Output
# 5.0
# Program executed successfully.
# Case 2

# Input

# 0
# Step-by-Step
# try starts

# ↓

# 10 / 0

# ↓

# ZeroDivisionError

# ↓

# except executes

# ↓

# else skipped
# Output
# Cannot divide by zero.

# Notice:

# The else block did not execute because an exception occurred.

# Example 2
try:
    name = "Janhavi"
    print(name)

except Exception:
    print("Error")

else:
    print("Everything is fine.")
# Output
# Janhavi
# Everything is fine.
# Flow Diagram
# No Exception
# try

# ↓

# No Exception

# ↓

# else

# ↓

# Program Ends
# Exception Occurs
# try

# ↓

# Exception

# ↓

# except

# ↓

# Program Ends
# Why Use else?

# Without else

try:
    result = 10 / 2
    print(result)

except ZeroDivisionError:
    print("Error")

print("Calculation completed.")

# The last print statement runs whether an error occurs or not.

# With else

try:
    result = 10 / 2

except ZeroDivisionError:
    print("Error")

else:
    print(result)
    print("Calculation completed.")

# Now these statements run only when there is no error, making the program logic clearer.

# 9. finally
# What is finally?

# The finally block always executes, whether an exception occurs or not.

# Syntax
# try:
#     ...
# except:
#     ...
# finally:
#     ...

# Think of it as a cleanup block.

# Example 1
try:
    print(10 / 2)

except ZeroDivisionError:
    print("Error")

finally:
    print("Program Finished")
# Output
# 5.0
# Program Finished
# Example 2
try:
    print(10 / 0)

except ZeroDivisionError:
    print("Cannot divide by zero.")

finally:
    print("Program Finished")
# Output
# Cannot divide by zero.
# Program Finished

# Notice:

# Even though an error occurred,

# finally:

# still executed.

# Step-by-Step
# try

# ↓

# Exception?

# ↓

# Yes

# ↓

# except

# ↓

# finally

# ↓

# End

# or

# try

# ↓

# No Exception

# ↓

# finally

# ↓

# End
# Why Use finally?

# Suppose you're opening a database connection.

# connection = connect_database()

# After using it, you must close it, even if an error occurs.

# try:
#     connection = connect_database()

#     # Work with database

# finally:
#     connection.close()

# This ensures the connection is always closed.

# The same idea applies to:

# Files
# Network connections
# Database connections
# Locks
# Example with File
try:
    file = open("data.txt", "r")
    print(file.read())

finally:
    file.close()
    print("File Closed")

# Even if an error occurs while reading,

# file.close()

# still executes.

# Note: In modern Python, using with open(...) is preferred because it automatically handles this cleanup for you.

# Difference Between else and finally
# else	finally
# Runs only if no exception occurs	Runs whether an exception occurs or not
# Used for success logic	Used for cleanup
# Example
try:
    print(10 / 2)

except ZeroDivisionError:
    print("Error")

else:
    print("Success")

finally:
    print("Always Executes")
# Output
# 5.0
# Success
# Always Executes

# Now change the code.

try:
    print(10 / 0)

except ZeroDivisionError:
    print("Error")

else:
    print("Success")

finally:
    print("Always Executes")
# Output
# Error
# Always Executes

# Notice:

# else did not execute.

# finally always executed.

# Complete Flow
#                 try
#                  │
#         ┌────────┴────────┐
#         │                 │
#  No Exception       Exception
#         │                 │
#       else            matching except
#         │                 │
#         └────────┬────────┘
#                  │
#              finally
#                  │
#              Program Ends
# 10. raise
# What is raise?

# Normally, Python raises exceptions automatically.

# Example

# 10 / 0

# Python automatically raises

# ZeroDivisionError

# But sometimes you want to raise an exception yourself.

# For that, use

raise
Syntax
raise ExceptionType("Error Message")
# Example 1
age = -5

if age < 0:
    raise ValueError("Age cannot be negative.")
# Step-by-Step
# age = -5

# ↓

# Check

# ↓

# age < 0

# ↓

# True

# ↓

# raise ValueError

# ↓

# Program Stops
# Output
# ValueError: Age cannot be negative.
# Example 2
marks = 120

if marks > 100:
    raise ValueError("Marks cannot be greater than 100.")
# Output
# ValueError: Marks cannot be greater than 100.
# Example 3
salary = -1000

if salary < 0:
    raise ValueError("Salary cannot be negative.")

print("Salary:", salary)

# Output

# ValueError: Salary cannot be negative.

# The last print() is never reached because execution stops when the exception is raised.

# Using raise with try-except
try:
    age = -5

    if age < 0:
        raise ValueError("Age cannot be negative.")

except ValueError as e:
    print(e)
# Output
# Age cannot be negative.
# Why Do We Use raise?

# Suppose a bank application allows only positive withdrawal amounts.

# withdraw_amount = -500

# Instead of continuing with invalid data,

# if withdraw_amount < 0:
#     raise ValueError("Withdrawal amount must be positive.")

# This prevents invalid data from moving further through the program.

# Interview Questions
# 1. What is the purpose of else in exception handling?

# Answer:
# The else block executes only if no exception occurs in the try block.

# 2. What is the purpose of finally?

# Answer:
# The finally block always executes and is mainly used for cleanup operations such as closing files or database connections.

# 3. What is raise?

# Answer:
# The raise statement is used to manually throw an exception when your program detects an invalid condition.

# 4. Can finally execute after an exception?

# Answer:
# Yes. The finally block executes whether an exception occurs or not.

# Summary Table
# Keyword	Executes When	Main Purpose
# try	Always	Contains code that may raise an exception
# except	If an exception occurs	Handles the exception
# else	Only if no exception occurs	Success path
# finally	Always	Cleanup (close files, release resources, etc.)
# raise	When called	Manually create and throw an exception
# Quick Revision
try:
    age = int(input("Enter age: "))

    if age < 0:
        raise ValueError("Age cannot be negative.")

except ValueError as e:
    print("Error:", e)

else:
    print("Valid age")

finally:
    print("Program Finished")

