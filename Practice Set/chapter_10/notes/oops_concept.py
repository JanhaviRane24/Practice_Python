# oops_concepts.py


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