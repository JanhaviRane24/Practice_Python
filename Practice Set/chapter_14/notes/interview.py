# 1. What is an Abstract Class?

# An abstract class is a class that cannot be instantiated directly. It is meant to be inherited by other classes.

# Example:

# from abc import ABC

# class Shape(ABC):
#     pass
# 2. What is an Abstract Method?

# An abstract method is a method declared in an abstract class without an implementation. Every concrete child class must implement it.

# from abc import ABC, abstractmethod

# class Shape(ABC):
#     @abstractmethod
#     def area(self):
#         pass
# 3. Can we create an object of an abstract class?

# No.

# s = Shape()

# Raises:

# TypeError: Can't instantiate abstract class Shape with abstract method area
# 4. Why do we use abstract classes?
# To define a common interface.
# To force child classes to implement required methods.
# To improve code consistency and design.
# 5. What happens if the child class does not implement the abstract method?

# The child class also becomes abstract and cannot be instantiated.

# from abc import ABC, abstractmethod

# class Shape(ABC):
#     @abstractmethod
#     def area(self):
#         pass

# class Circle(Shape):
#     pass

# c = Circle()

# This raises a TypeError.

# 6. Which module is used for abstract classes?

# Python provides the abc module.

# from abc import ABC, abstractmethod
# 7. Difference between normal class and abstract class
# Normal Class	Abstract Class
# Can create objects	Cannot create objects directly
# Methods may or may not be implemented	Can contain abstract methods
# Used directly	Used as a base class
# 8. Is an abstract class allowed to have normal methods?

# Yes.

# from abc import ABC, abstractmethod

# class Shape(ABC):

#     def display(self):
#         print("Shape class")

#     @abstractmethod
#     def area(self):
#         pass

# The display() method is a regular method, while area() is abstract.

# Interview Tip

# Although Python accepts your Circle.area(self, radius) implementation, 
# it's considered good practice to keep the method signature compatible with the abstract method. 
# If the abstract method is defined as area(self), t
# he subclass should generally implement it with the same parameters unless you have a clear design reason to do otherwise.

