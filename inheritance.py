"""
INHERITANCE IN PYTHON
---------------------

Inheritance allows one class (child/subclass) to acquire
properties and methods from another class (parent/superclass).

Benefits:
- Code reuse
- Avoids duplication
- Creates parent-child relationships between classes
"""


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