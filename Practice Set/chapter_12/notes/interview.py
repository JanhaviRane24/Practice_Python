# Polymorphism
# │
# ├── Runtime Polymorphism
# │      └── Method Overriding
# │
# └── Compile-time Polymorphism
#        └── Method Overloading
# #           (Not directly supported in Python)

# Interview Questions

# 1. What is polymorphism?
# Answer: Polymorphism means one interface, many forms. The same method can behave differently depending on the object.

# 2. How many types of polymorphism are there?
# There are two types:
# Compile-time polymorphism (method overloading)
# Runtime polymorphism (method overriding)

# 3. Does Python support method overloading?
# Answer: Not in the traditional sense. Python uses default arguments, *args, or **kwargs to achieve similar behavior.

# 4. Does Python support method overriding?
# Answer: Yes. Python fully supports method overriding through inheritance.

# 5. Which type of polymorphism is more common in Python?
# Method overriding (runtime polymorphism) is the primary form of polymorphism used in Python.

# # Quick Comparison
# | Feature                      | Method Overloading                        | Method Overriding          |
# | ---------------------------- | ----------------------------------------- | -------------------------- |
# | Same method name             | Yes                                       | Yes                        |
# | Different parameters         | Yes                                       | Usually same or compatible |
# | Inheritance required         | No                                        | Yes                        |
# | Supported directly in Python | No                                        | Yes                        |
# | Decided at                   | Compile time (in languages like Java/C++) | Runtime                    |

# Polymorphism means one interface, many forms. It allows the same method name to perform different tasks depending on the object. In Python, polymorphism is mainly achieved through method overriding, while overloading is simulated using features like *args and default arguments.

# Interview Questions
# 1. What is method overriding?

# Answer:
# Method overriding is when a child class provides a new implementation of a method already defined in its parent class.

# 2. Why is method overriding used?

# Answer:
# It allows a child class to customize or extend the behavior inherited from the parent class.

# 3. What is runtime polymorphism?

# Answer:
# Runtime polymorphism means the method that executes is determined by the actual object at runtime, not by the variable name.

# Example:

# Animal obj = Dog()

# Calling

# obj.sound()

# executes the Dog implementation.

# 4. What is the difference between overloading and overriding?
# Method Overloading	                                     Method Overriding
# Same method name with different parameters	             Same method name and compatible parameters
# Decided at compile time (in languages that support it)	 Decided at runtime
# Python does not support traditional method overloading	 Python fully supports method overriding

# 5. Can we call the parent method after overriding?

# Yes.

# super().sound()

# 6. What happens if the child does not override the method?

# The parent method is inherited and executed.

# Example:

class Animal:
    def sound(self):
        print("Animal")

class Dog(Animal):
    pass

Dog().sound()

# Output

# Animal
# 7. Can we override the constructor (__init__)?

# Yes.

class Animal:
    def __init__(self):
        print("Animal")

class Dog(Animal):
    def __init__(self):
        print("Dog")

# 8. What is super()?

# super() returns a proxy object that allows you to access methods and attributes from the parent class.

# 9. Does Python support method overriding?

# Yes. Python supports method overriding as part of its object-oriented programming features.

# 10. Explain your code in an interview.

# You can say:

"Dog and Cat inherit from Animal. Each child class overrides the sound() method with its own implementation. When I iterate through different objects and call a.sound(), Python invokes the appropriate method based on the object's actual type. This demonstrates runtime polymorphism through method overriding."

# Interview Questions

# 1. Does Python support method overloading?

# Answer: No. Python does not support traditional method overloading because a later method with the same name replaces the earlier one.

# 2. Why doesn't your code work?

# Answer: The second add() method overrides the first one, so only the last definition exists. Calling c.add(1, 2, 4) results in a TypeError because the method expects fewer arguments.

# 3. How can we simulate method overloading in Python?
# Default arguments
# *args (variable-length arguments)
# Optional keyword arguments (**kwargs)
# Manual type/argument checking inside a single method

# 4. Difference between Overloading and Overriding
# Method Overloading	Method Overriding
# Same method name with different parameter lists	Child class provides a new implementation of a parent class method
# Not supported traditionally in Python	Fully supported in Python
# Achieved using *args or default arguments	Achieved using inheritance

# A common interview point is that Python supports method overriding but not traditional method overloading. When asked about overloading, explain that Python achieves similar behavior using features like *args and default parameter values rather than multiple methods with the same name.