# Method Overriding
# Definition

# Method overriding occurs when a child class provides its own implementation of a method that already exists in the parent class.

# The parent and child methods must have the same name.
# They should have the same parameters (or a compatible signature).
# When the method is called using a child object, the child's version executes instead of the parent's.

# Your Example
class Animal:
    def sound(self):
        print("make a sound")

class Dog(Animal):
    def sound(self):
        print("woof")

class Cat(Animal):
    def sound(self):
        print("meow")

for a in [Dog(), Cat(), Animal()]:
    a.sound()
# Output
# woof
# meow
# make a sound
# How it Works
# Step 1

# Dog inherits from Animal.

# Animal
#    ↑
#   Dog
# Step 2

# Dog has its own sound() method.

# class Dog(Animal):
#     def sound(self):
#         print("woof")

# This overrides the parent's sound() method.

# Step 3

# When Python executes

# Dog().sound()

# it first searches inside the Dog class.

# It finds

# def sound():

# so it executes that method.

# It never goes to the parent class because the method already exists in the child.

# Step 4

# For

# Animal().sound()

# Python only has the parent's method.

# Output
# make a sound


# Method Resolution Order (MRO)

# Python searches for methods in this order:

# Child Class
#       ↓
# Parent Class
#       ↓
# Grandparent Class
#       ↓
# object

# Example:

# Dog().sound()

# Searches

# Dog
# ↓

# Animal
# ↓

# object

# Since Dog already has sound(), the search stops there.

# Runtime Polymorphism

# Your loop

# for a in [Dog(), Cat(), Animal()]:
#     a.sound()

# is the best example.

# Variable a refers to different object types.

# a = Dog()

# a = Cat()

# a = Animal()

# The same statement

# a.sound()

# produces different outputs depending on the object's type.

# This is called runtime polymorphism.

# Difference Between Inheritance and Overriding

# Inheritance

# class Animal:
#     pass

# class Dog(Animal):
#     pass

# means Dog acquires Animal's properties.

# Overriding

# class Dog(Animal):
#     def sound(self):
#         print("woof")

# means Dog changes the inherited behavior.

# Accessing Parent Method

# Use super().

# class Animal:
#     def sound(self):
#         print("Animal sound")

# class Dog(Animal):
#     def sound(self):
#         super().sound()
#         print("Woof")

# Output

# Animal sound
# Woof

# super() calls the parent class implementation.

# Method Overriding Rules
# Child class must inherit from the parent.
# Method names should be the same.
# Parameters should be compatible.
# The child method replaces the parent method for child objects.
#