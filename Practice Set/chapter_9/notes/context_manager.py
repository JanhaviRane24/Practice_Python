# 6. Context Manager (with Statement)
# What is a Context Manager?

# A Context Manager is a Python feature that automatically manages resources like:

# Files
# Database connections
# Network connections
# Locks (Multithreading)

# The most common example is opening files.

# Instead of remembering to close a file yourself, Python closes it automatically.

# Why Do We Need It?

# Suppose you want to read a file.

# Without with
file = open("data.txt", "r")

content = file.read()

print(content)

file.close()
# Step-by-Step
# Open File
# ↓

# Read File
# ↓

# Print Content
# ↓

# Close File

# This works.

# But what happens if an error occurs before file.close()?

file = open("data.txt", "r")

print(file.read())

10 / 0      # Error occurs here

file.close()

# Output

# ZeroDivisionError

# Since the program crashes,

# file.close()

# is never executed.

# The file remains open.

# This can cause:

# Memory leaks
# Locked files
# Wasted system resources
# Solution → Use with
with open("data.txt", "r") as file:
    content = file.read()
    print(content)
# Step-by-Step
# Open File

# ↓

# Assign it to variable "file"

# ↓

# Execute code inside with

# ↓

# Automatically close file

# ↓

# Program continues

# Even if an error occurs, Python still closes the file.

# Syntax
# with open("filename", "mode") as variable:
#     # Code

# Meaning

# open()

# ↓

# returns file object

# ↓

# stored in variable

# ↓

# use file

# ↓

# Python automatically closes it
# Example 1 – Read File

# Suppose students.txt contains

# Alice
# Bob
# Charlie

# Program

with open("students.txt", "r") as file:
    print(file.read())

# Output

# Alice
# Bob
# Charlie
# Example 2 – Read Line by Line

# Suppose students.txt

# Alice
# Bob
# Charlie
with open("students.txt", "r") as file:
    for line in file:
        print(line.strip())

# Output

# Alice
# Bob
# Charlie
# Why strip()?

# Each line ends with a newline (\n).

# Without strip()

# Alice

# Bob

# Charlie

# With strip()

# Alice
# Bob
# Charlie
# Example 3 – Write File
with open("notes.txt", "w") as file:
    file.write("Hello Python")
# Step-by-Step
# Open notes.txt

# ↓

# Write

# Hello Python

# ↓

# Automatically Close

# Contents of file

# Hello Python
# Example 4 – Append File

# Suppose

# notes.txt

# Hello Python

# Program

with open("notes.txt", "a") as file:
    file.write("\nWelcome")

# Now file becomes

# Hello Python
# Welcome
# What Does as Mean?

# Example

# with open("data.txt") as file:

# is similar to

# file = open("data.txt")

# The difference is that with with, Python automatically closes the file afterward.

# Multiple Context Managers

# Before Python 3.10, we wrote:

with open("file1.txt") as f1, open("file2.txt") as f2:
    print(f1.read())
    print(f2.read())

# This opens both files in one with statement.

# Python 3.10+ (Cleaner Formatting)

# You can split multiple context managers across multiple lines.

with (
    open("file1.txt") as f1,
    open("file2.txt") as f2
):
    print(f1.read())
    print(f2.read())

# This is especially useful when you have many files or resources to manage.

# Example

# Suppose

# file1.txt

# Python

# file2.txt

# Programming

# Program

with (
    open("file1.txt") as f1,
    open("file2.txt") as f2
):
    print(f1.read())
    print(f2.read())

# Output

# Python
# Programming
# Step-by-Step
# Open file1

# ↓

# Open file2

# ↓

# Assign

# f1
# f2

# ↓

# Read both files

# ↓

# Automatically close file1

# ↓

# Automatically close file2
# How Does Python Close Files Automatically?

# When execution leaves the with block—whether normally or because of an exception—Python calls the context manager's cleanup method (__exit__()).

# Think of it like this:

# Enter with block

# ↓

# Open resource

# ↓

# Run your code

# ↓

# Leave block

# ↓

# Cleanup happens automatically

# This automatic cleanup is what makes context managers safe and reliable.

# Example with Error
try:
    with open("students.txt", "r") as file:
        print(file.read())
        10 / 0
except ZeroDivisionError:
    print("Cannot divide by zero")

# Output (assuming the file exists)

# Alice
# Bob
# Charlie
# Cannot divide by zero

# Even though an exception occurred, the file is still closed properly because the with block handles cleanup.

# Advantages of with
# Without with	With with
# Must call close() manually	Automatically closes resources
# Can leave files open if an error occurs	Safe even if an error occurs
# More code	Cleaner and shorter
# Easier to forget cleanup	Cleanup is automatic

# Interview Questions
# 1. What is a context manager?

# Answer:
# A context manager is an object that manages resources like files or database connections. It automatically performs setup when entering a block and cleanup when leaving it.

# 2. Why do we use the with statement?

# Answer:
# The with statement ensures resources are automatically released after use, even if an exception occurs. This prevents resource leaks and makes the code cleaner.

# 3. What is the advantage of with open() over open()?

# Answer:

# No need to call close() manually.
# Files are always closed properly.
# Code is safer and easier to read.

# Quick Revision
# # Read a file
# with open("data.txt", "r") as file:
#     print(file.read())

# # Write a file
# with open("data.txt", "w") as file:
#     file.write("Hello")

# # Open multiple files
# with (
#     open("file1.txt") as f1,
#     open("file2.txt") as f2
# ):
#     print(f1.read())
#     print(f2.read())

# Summary
# Concept	Purpose
# with	Automatically manages resources
# open()	Opens a file
# as	Stores the opened file object in a variable
# Automatic Cleanup	Calls close() for you when leaving the block
# Multiple Context Managers	Open and manage multiple resources in one with statement
