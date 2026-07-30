# 2. Class Method
# What is Class Method?

# A class method works with the class, not individual objects.

# Uses

# @classmethod

# First parameter is

# cls

# instead of

# self
# Example
class Student:

    college = "ABC College"

    @classmethod
    def show_college(cls):
        print(cls.college)

Student.show_college()

# Output

# ABC College
# Step-by-Step

# Class variable

Student

college = "ABC College"

# Call

Student.show_college()

# Python internally

Student.show_college(Student)

# Inside

cls = Student

# Then

print(cls.college)

# prints

# ABC College
# Changing Class Variable
class Student:

    college = "ABC"

    @classmethod
    def change_college(cls, new):
        cls.college = new

Student.change_college("XYZ")

print(Student.college)

# Output

# XYZ
# Why use Class Methods?

# When changing values shared by all objects.

# Example

# School Name

# Company Name

# Tax Rate

# Interest Rate
