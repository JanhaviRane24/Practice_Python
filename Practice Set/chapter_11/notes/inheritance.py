"""
INHERITANCE IN PYTHON
---------------------

Inheritance allows one class (child/subclass) to acquire
properties and methods from another class (parent/superclass).

Benefits:
- Code reuse
- Avoids duplication
- Creates parent-child relationships between classes
# """
# Inheritance & More On OOPS
# Inheritance is a way of creating a new class from an existing class.
# Syntax:
class Employee:  # Base class
    pass

class Programmer(Employee): # Derived or child class
    pass
# Code
# We can use the method and attributes of 'Employee' in 'Programmer' object.
# Also, we can overwrite or add new attributes and methods in 'Programmer' class.

# Types Of Inheritance
# Single inheritance
# Multiple inheritance
# Multilevel inheritance

# Single Inheritance
# Single inheritance occurs when child class inherits only a single parent class

# Multiple Inheritance
# Multiple Inheritance occurs when the child class inherits from more than one parent classes.

# Multilevel Inheritance
# When a child class becomes a parent for another child class.

# super() Method
# super() method is used to access the methods of a super class in the derived class.
super().__init__()
# __init__() Calls constructor of the base class

# Class Method
# A class method is a method which is bound to the class and not the object of the class.
# @classmethod decorator is used to create a class method.
# # Syntax:
# @classmethod
# def(cls,p1,p2):
#     pass

# @property Decorator
# # Consider the following class:
# class Employee:
# @property
# def name(self):
# return self.ename
# If e = Employee() is an object of class employee, we can print(e.name) to print the ename by internally calling
# name() function.

# @.getters and @.setters
# The method name with '@property' decorator is called getter method

# We can define a function + @ name.setter decorator like below:
# @name.setter
# def name(self,value):
#     self.ename = value

# Operator Overloading In Python
# Operators in Python can be overloaded using dunder methods.
# These methods are called when a given operator is used on the objects.
# Operators in Python can be overloaded using the following methods:
# p1+p2 # p1.__add__(p2)
# p1-p2 # p1.__sub__(p2)
# p1*p2 # p1.__mul__(p2)
# p1/p2 # p1.__truediv__(p2)
# p1//p2 # p1.__floordiv__(p2)

# Other dunder/magic methods in Python:
# __str__() # used to set what gets displayed upon calling str(obj)
# __len__() # used to set what gets displayed upon calling len(obj)


# Parent Class
class Animal:

    def __init__(self, name):
        self.name = name

    def speak(self):
        print("Some sound")


# Child Class inheriting Animal
class Dog(Animal):

    # Method overriding
    def speak(self):
        print("Bark")


# Another child class
class Cat(Animal):

    def speak(self):
        print("Meow")


# Creating objects
animal = Animal("Unknown")
dog = Dog("Tommy")
cat = Cat("Kitty")


animal.speak()
dog.speak()
cat.speak()


# ------------------------------------------------
# super() example
# ------------------------------------------------

class Vehicle:

    def start(self):
        print("Vehicle started")


class Car(Vehicle):

    def start(self):
        # Calling parent method
        super().start()

        print("Car engine started")


car = Car()

car.start()

"""
Explanation:

Inheritance means a child class can use the properties and methods of a parent class.

Example:

Animal
  |
  |
 Dog

Dog automatically gets everything from Animal.

Important Interview Points:
Parent class → superclass
Child class → subclass
Reusing existing code is the main advantage
super() is used to access parent methods

Example:

super().start()

calls the parent class method.
"""