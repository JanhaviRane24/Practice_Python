# What is Encapsulation?

# Encapsulation is the OOP concept of binding data (variables) and methods (functions) together into a single unit (class) and controlling access to the data.

# In simple terms:

# Encapsulation = Data Hiding + Data Protection + Controlled Access

# Example:

# class Student:
#     def __init__(self):
#         self.name = "Janhavi"

#     def display(self):
#         print(self.name)

# Here, name (data) and display() (method) are inside the same class.

# Why is Encapsulation Needed?

# Suppose anyone can directly modify your bank balance.

# account.balance = -100000

# This is not safe.

# Instead, we use methods to control access.

# account.deposit(500)
# account.withdraw(200)

# Advantages:

# Protects data
# Prevents invalid modifications
# Improves security
# Makes code easier to maintain
# Data Members in Encapsulation

# Python uses three kinds of attributes.

# 1. Public Members

# Accessible from anywhere.

# class Student:
#     def __init__(self):
#         self.name = "Janhavi"

# s = Student()

# print(s.name)

# Output

# Janhavi
# 2. Protected Members

# Begin with a single underscore (_).

# class Student:
#     def __init__(self):
#         self._marks = 90

# s = Student()

# print(s._marks)

# Output

# 90
# Important

# Protected members are not truly protected. The underscore is a convention indicating they are intended for internal use.

# 3. Private Members

# Begin with double underscores (__).

# class Student:
#     def __init__(self):
#         self.__marks = 90

# s = Student()

# print(s.__marks)

# Output

# AttributeError

# Python performs name mangling.

# Internally,

# self.__marks

# becomes

# self._Student__marks

# So,

# print(s._Student__marks)

# Output

# 90
# Name Mangling

# Example

# class Bag:
#     def __init__(self):
#         self.__notes = "Important"

# b = Bag()

# print(b._Bag__notes)

# Output

# Important

# Purpose:

# Avoid accidental access
# Avoid accidental overriding in subclasses
# Getter Method

# A getter returns private data.

# class Student:
#     def __init__(self):
#         self.__marks = 90

#     def get_marks(self):
#         return self.__marks

# s = Student()

# print(s.get_marks())

# Output

# 90
# Setter Method

# A setter modifies private data.

# class Student:
#     def __init__(self):
#         self.__marks = 90

#     def set_marks(self, marks):
#         self.__marks = marks

#     def get_marks(self):
#         return self.__marks

# s = Student()

# s.set_marks(95)

# print(s.get_marks())

# Output

# 95
# Validation Using Encapsulation
# class Student:
#     def __init__(self):
#         self.__marks = 0

#     def set_marks(self, marks):
#         if 0 <= marks <= 100:
#             self.__marks = marks
#         else:
#             print("Invalid Marks")

#     def get_marks(self):
#         return self.__marks

# s = Student()

# s.set_marks(110)

# print(s.get_marks())

# Output

# Invalid Marks
# 0

# This is one of the biggest advantages of encapsulation.

# Encapsulation Using Properties

# Instead of explicit getters and setters, Python provides @property.

# class Employee:
#     def __init__(self):
#         self.__salary = 50000

#     @property
#     def salary(self):
#         return self.__salary

#     @salary.setter
#     def salary(self, value):
#         if value > 0:
#             self.__salary = value

# e = Employee()

# print(e.salary)

# e.salary = 60000

# print(e.salary)

# Output

# 50000
# 60000
# Real-Life Example: Bank Account
# class BankAccount:
#     def __init__(self, balance):
#         self.__balance = balance

#     def deposit(self, amount):
#         self.__balance += amount

#     def withdraw(self, amount):
#         if amount <= self.__balance:
#             self.__balance -= amount
#         else:
#             print("Insufficient Balance")

#     def show_balance(self):
#         print("Balance:", self.__balance)

# b = BankAccount(5000)

# b.deposit(2000)
# b.withdraw(1000)

# b.show_balance()

# Output

# Balance: 6000
# Real-Life Example: Mobile
# class Mobile:
#     def __init__(self):
#         self.apps = ("WhatsApp", "Instagram")
#         self._contacts = {"Rahul": "9876543210"}
#         self.__messages = {"Rahul": "Hello"}

#     def see_messages(self):
#         return self.__messages

# m = Mobile()

# print(m.apps)
# print(m._contacts)
# print(m.see_messages())
# Advantages of Encapsulation
# Data security
# Data hiding
# Easy maintenance
# Prevents accidental modification
# Allows validation before updating data
# Improves code reusability
# Disadvantages
# Slightly more code because of methods.
# Accessing private data requires getters/setters or properties.
# Encapsulation vs Abstraction
# Encapsulation	Abstraction
# Hides data	Hides implementation details
# Achieved using private/protected members	Achieved using abstract classes and methods
# Focuses on data protection	Focuses on essential functionality
# Interview Questions
# 1. What is encapsulation?

# Answer: Encapsulation is the process of wrapping data and methods into a single class and controlling access to the data.

# 2. What are the benefits of encapsulation?
# Data hiding
# Security
# Validation
# Better maintenance
# Reduced coupling
# 3. What are access modifiers in Python?
# Public (variable)
# Protected (_variable)
# Private (__variable)
# 4. Does Python support true private variables?

# No. Python uses name mangling, not strict access control.

# 5. What is name mangling?

# Python changes a private attribute like:

# self.__data

# to:

# self._ClassName__data

# to reduce accidental access or overriding.

# 6. What is the difference between getters/setters and properties?
# Getter/Setter methods: Explicit methods like get_marks() and set_marks().
# Properties (@property): Allow attribute-style access while still using getter and setter logic behind the scenes.
# 7. Is encapsulation the same as data hiding?

# Not exactly. Data hiding is one result of encapsulation. Encapsulation also organizes related data and methods together and provides controlled access.

# 8. What is the difference between _name and __name?
# _name: Protected by convention; still directly accessible.
# __name: Name-mangled by Python to discourage direct access.
# Quick Revision
# Encapsulation
# │
# ├── Public Members
# │      self.name
# │
# ├── Protected Members
# │      self._name
# │
# ├── Private Members
# │      self.__name
# │
# ├── Name Mangling
# │      _ClassName__name
# │
# ├── Getter Methods
# │
# ├── Setter Methods
# │
# ├── @property
# │
# ├── Validation
# │
# └── Real-world Examples
#        Bank Account
#        Mobile
#        Student