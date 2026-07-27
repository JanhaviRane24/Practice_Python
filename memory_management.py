"""
PYTHON MEMORY MANAGEMENT
------------------------

Python manages memory automatically.

Main concepts:
1. Reference Counting
2. Garbage Collector
3. Namespaces
"""


import sys
import gc


# -----------------------------------
# Reference Counting
# -----------------------------------

class Student:
    pass


student1 = Student()

# Checking reference count
print(sys.getrefcount(student1))


student2 = student1

print(sys.getrefcount(student1))


del student2

print(sys.getrefcount(student1))



# -----------------------------------
# Circular Reference Example
# -----------------------------------

class A:

    def __init__(self):
        self.other = None



class B:

    def __init__(self):
        self.other = None



obj1 = A()
obj2 = B()


# Creating circular reference

obj1.other = obj2
obj2.other = obj1


del obj1
del obj2


# Garbage collector removes cycles

gc.collect()


print("Circular references cleaned")



# -----------------------------------
# Namespace Example
# -----------------------------------

# Built-in namespace
print(len([1,2,3]))


# Global namespace

name = "Python"


def example():

    # Local namespace

    age = 10

    print(name)
    print(age)


example()

"""

Explanation
Reference Counting

Python stores how many references point to an object.

Example:

a = object()
b = a

Reference count becomes:

a ---> object <--- b

When count reaches zero:

object
   |
deleted

Memory is released.

Why reference counting is not enough?

Circular reference:

Object A ---> Object B
Object B ---> Object A

Their reference count never becomes zero.

Python Garbage Collector detects and removes these cycles.

Namespace Lookup Order

Python searches variables in:

LEGB

L - Local
E - Enclosing
G - Global
B - Built-in

"""