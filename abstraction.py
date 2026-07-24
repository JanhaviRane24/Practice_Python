"""
ABSTRACTION IN PYTHON
---------------------

Abstraction hides internal implementation
and exposes only required functionality.

Python uses abstract classes through
the abc module.
"""


from abc import ABC, abstractmethod


# Abstract class

class Payment(ABC):


    @abstractmethod
    def pay(self, amount):
        pass



class CreditCardPayment(Payment):

    def pay(self, amount):

        print(f"Paid {amount} using Credit Card")



class UPIPayment(Payment):

    def pay(self, amount):

        print(f"Paid {amount} using UPI")



# User does not need to know internal details

payment1 = CreditCardPayment()

payment2 = UPIPayment()


payment1.pay(1000)

payment2.pay(500)

"""

Explanation:

Abstraction hides complexity.

Example:

When you use:

payment.pay()

you don't care about:

API calls
security checks
transaction processing
database operations

You only know:

Payment happens
Method Overriding vs Method Overloading
Method Overriding

A child class changes the implementation of a parent method.

Example:

class Animal:

    def sound(self):
        print("Sound")


class Dog(Animal):

    def sound(self):
        print("Bark")

Same method:

sound()

Different implementation.

Method Overloading

Multiple methods with the same name but different parameters.

Example in Java:

add(int a,int b)

add(int a,int b,int c)

Python does not support true method overloading.

Instead, Python uses:

Default arguments
def add(a,b,c=0):

    return a+b+c


print(add(2,3))
print(add(2,3,4))

or:

*args
def add(*numbers):

    total = 0

    for n in numbers:
        total += n

    return total


print(add(1,2))
print(add(1,2,3,4))
"""