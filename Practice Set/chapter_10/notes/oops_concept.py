# oops_concepts.py

# Object Oriented Programming
# Solving a problem by creating object is one of the most popular approaches in programming. This is called
# object-oriented programming.
# This concept focuses on using reusable code (DRY Principle).
# Class
# A class is a blueprint for creating object.
# Syntax:
class Eagle: # Class name is written in pascal case
    pass
# # Methods & Variables

# Object
# An object is an instantiation of a class. When class is defined, a template (info) is defined. Memory is
# allocated only after object instantiation.
# Objects of a given class can invoke the methods available to it without revealing the implementation details to
# the user. – Abstractions & Encapsulation!

# Modelling A Problem In OOPS
# We identify the following in our problem.
# Noun → Class → Employee
# Adjective →Attributes →name, age, salary
# Verbs → Methods →getSalary(), increment()

# Class Attributes
# An attribute that belongs to the class rather than a particular object.
# Example:

class Employee:
    company = "Google" # Specific to Each Class

harry = Employee() # Object Instantiation
harry.company
Employee.company = "YouTube" # Changing Class Attribute
# Instance Attributes
# An attribute that belongs to the Instance (object). Assuming the class from the previous example:
harry.name = "harry"
harry.salary = "30k" # Adding instance attribute

# Note: Instance attributes take preference over class attributes during assignment & retrieval.
# When looking up for harry.attribute it checks for the following:
# 1) Is attribute present in object?
# 2) Is attribute present in class?

# Self Parameter
# self refers to the instance of the class. It is automatically passed with a function call from an object.
harry.getSalary() # here self is harry
# # equivalent to Employee.getSalary(harry)
# The function getSalary() is defined as:
class Employee:
    company = "Google"
    def getSalary(self):
        print("Salary is not there")

# Static Method
# Sometimes we need a function that does not use the self-parameter. We can define a static method like this

@staticmethod  # decorator to mark greet as a static method
def greet():
    print("Hello user")
# __init__() Constructor
# __init__() is a special method which is first run as soon as the object is created.
# __init__() method is also known as constructor.
# It takes ‘selfʼ argument and can also take further arguments.
# For Example:
class Employee:
    def __init__(self, name):
        self.name=name
    def getSalary(self):
        pass
harry = Employee("Harry")

# =========================
# Class and Object
# =========================

class Student:

    def display(self):
        print("Welcome to Python")


# Object creation

obj = Student()

obj.display()



# =========================
# self keyword
# =========================

class StudentInfo:

    def display(self):
        print("self refers to the current object")


student1 = StudentInfo()

student1.display()



# =========================
# Constructor (__init__)
# =========================

class Student:

    def __init__(self, name, age):
        self.name = name
        self.age = age


    def show_details(self):
        print("Name:", self.name)
        print("Age:", self.age)



student = Student("Pavan", 21)

student.show_details()



# Multiple objects with different data

student1 = Student("Rahul", 22)
student2 = Student("Amit", 20)

print("\nMultiple Objects:")

student1.show_details()
student2.show_details()



# =========================
# Four Pillars of OOP
# =========================


# 1. Encapsulation
# Wrapping data and methods together in a class

class BankAccount:

    def __init__(self, balance):
        self.__balance = balance


    def get_balance(self):
        return self.__balance


account = BankAccount(5000)

print("\nEncapsulation:")
print("Balance:", account.get_balance())



# 2. Inheritance
# Child class inherits properties and methods from parent class


class Animal:

    def speak(self):
        print("Animal makes sound")


class Dog(Animal):

    def bark(self):
        print("Dog barks")


print("\nInheritance:")

dog = Dog()

dog.speak()
dog.bark()



# 3. Polymorphism
# Same method name, different behavior


class Cat:

    def sound(self):
        print("Cat says Meow")


class Cow:

    def sound(self):
        print("Cow says Moo")


print("\nPolymorphism:")

animals = [Cat(), Cow()]

for animal in animals:
    animal.sound()



# 4. Abstraction
# Hiding implementation details and showing only necessary features


from abc import ABC, abstractmethod


class Vehicle(ABC):

    @abstractmethod
    def start(self):
        pass



class Car(Vehicle):

    def start(self):
        print("Car starts with key")


print("\nAbstraction:")

car = Car()

car.start()

"""
Four Pillars of OOP
1. Encapsulation
Combining data and methods inside a class.
Protects data using access control.
Example:

self.__balance

2. Inheritance
Child class gets properties and methods from parent class.
Example:

class Dog(Animal):

Dog inherits Animal features.

3. Polymorphism
Same method name, different behavior.
Example:

cat.sound()
cow.sound()

Both have sound() but different outputs.

4. Abstraction
Hides internal implementation.
Shows only required functionality.
Example:

@abstractmethod
def start(self):

Users know what a car does, not the internal engine process.




"""