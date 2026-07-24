"""
ENCAPSULATION IN PYTHON
-----------------------

Encapsulation means wrapping data and methods
inside a single class and controlling access
to that data.
"""


class BankAccount:

    def __init__(self, balance):

        # Public variable
        self.owner = "John"

        # Protected variable
        self._balance = balance

        # Private variable
        self.__pin = 1234


    def show_balance(self):

        print("Balance:", self._balance)


    def verify_pin(self, pin):

        if pin == self.__pin:
            print("Access granted")

        else:
            print("Wrong PIN")



account = BankAccount(5000)


# Public access
print(account.owner)


# Protected access
# Possible but not recommended
print(account._balance)


# Private access
# This will not work directly

# print(account.__pin)


account.show_balance()

account.verify_pin(1234)
account.verify_pin(1111)



# Accessing private variable using name mangling

print(account._BankAccount__pin)

"""
Explanation:

Encapsulation protects data by controlling access.

Python access levels:

Syntax	Meaning
variable	Public
_variable	Protected (convention only)
__variable	Private (name mangling)

Example:

self.__pin

Python internally changes it:

_BankAccount__pin

making direct access harder.

Encapsulation vs Abstraction

Encapsulation

Focus:

Protecting data and controlling access.

Example:

__password

Abstraction

Focus:

Hiding unnecessary implementation details.

Example:

Using:

list.sort()

without knowing the sorting algorithm.

"""