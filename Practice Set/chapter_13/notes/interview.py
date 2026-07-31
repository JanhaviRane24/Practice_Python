# # Interview Questions

# 1. What is encapsulation?

# Answer:
# Encapsulation is the process of combining data (attributes) and methods into a single class while controlling access to the data.

# Example:

# class Student:
#     def __init__(self):
#         self.__marks = 90

#     def get_marks(self):
#         return self.__marks
# 2. Why do we use encapsulation?

# Answer:

# Protects data from unauthorized access.
# Allows data validation.
# Improves code security.
# Makes code easier to maintain.
# Hides implementation details.
# 3. What are the access modifiers in Python?

# Answer:

# Access Modifier	Syntax	Accessible Outside?
# Public	name	✅ Yes
# Protected	_name	✅ Yes (by convention)
# Private	__name	❌ Not directly
# 4. What is a public member?

# Answer:
# A public member can be accessed from anywhere.

# class Student:
#     def __init__(self):
#         self.name = "Janhavi"

# s = Student()
# print(s.name)
# 5. What is a protected member?

# Answer:
# A protected member starts with a single underscore (_). It is a convention indicating that it should be used only within the class or its subclasses.

# class Student:
#     def __init__(self):
#         self._marks = 95

# s = Student()
# print(s._marks)

# Interview Point: Python does not enforce protection for _marks.

# 6. What is a private member?

# Answer:
# A private member starts with double underscores (__) and is name-mangled by Python.

# class Student:
#     def __init__(self):
#         self.__marks = 95

# Trying to access:

# print(s.__marks)

# raises:

# AttributeError
# 7. What is name mangling?

# Answer:
# Python internally changes private attribute names.

# Example:

# self.__marks

# becomes

# self._Student__marks

# Access:

# print(s._Student__marks)
# 8. Why does Python use name mangling?

# Answer:
# To reduce accidental access and avoid accidental overriding of private attributes in subclasses. It is not intended as a security feature.

# 9. Can we access private variables?

# Answer:
# Yes, indirectly through methods or by using the mangled name.

# print(s._Student__marks)

# or

# s.get_marks()
# 10. What is a getter method?

# Answer:
# A getter returns the value of a private attribute.

# def get_marks(self):
#     return self.__marks
# 11. What is a setter method?

# Answer:
# A setter updates the value of a private attribute, often after validation.

# def set_marks(self, marks):
#     self.__marks = marks
# 12. Why use getters and setters?

# Answer:

# Validate data before updating.
# Prevent invalid values.
# Hide internal implementation.
# Control how data is accessed.
# 13. What is the difference between getters/setters and @property?

# Getter/Setter

# student.get_marks()
# student.set_marks(90)

# Property

# print(student.marks)
# student.marks = 90

# @property provides a cleaner, more Pythonic interface.

# 14. Does Python have true private variables?

# Answer:
# No. Python relies on conventions and name mangling rather than strict access control.

# 15. Difference between _name and __name
# _name	__name
# Protected by convention	Private (name-mangled)
# Directly accessible	Not directly accessible
# No name mangling	Name mangling applied
# 16. Can private members be inherited?

# Answer:
# Yes, but they are inherited with their mangled names.

# class Parent:
#     def __init__(self):
#         self.__x = 10

# Internally:

# _Parent__x
# 17. Is encapsulation the same as data hiding?

# Answer:
# No.

# Data hiding means restricting direct access to data.
# Encapsulation means bundling data and methods together and providing controlled access.

# Data hiding is one benefit of encapsulation.

# 18. Give a real-life example of encapsulation.

# Answer:
# A bank account.

# Balance is private.
# Users deposit and withdraw money using methods.
# The balance cannot be modified directly.
# class Bank:
#     def __init__(self):
#         self.__balance = 1000

#     def deposit(self, amount):
#         self.__balance += amount

#     def show(self):
#         print(self.__balance)
# 19. Which OOP principle does encapsulation support?

# Answer:
# It supports data hiding and controlled access.

# 20. What are the advantages of encapsulation?
# Data security
# Better maintainability
# Easier validation
# Improved modularity
# Reduced coupling
# 21. What are the disadvantages?
# Slightly more code.
# Can add complexity for very simple classes.
# 22. Which is better: getters/setters or public variables?

# Answer:
# If the value needs validation or protection, use private variables with getters/setters or @property. If no control is needed, public variables are simpler.

# 23. Explain encapsulation in one sentence.

# Answer:

# Encapsulation is the process of combining data and methods into a class while controlling access to the data using public, protected, and private members.

# Interview Tip

# A strong interview answer is:

# "Encapsulation is an OOP principle that bundles data and methods into a class and controls access to the data. In Python, this is achieved using public, protected (_), and private (__) attributes. Private attributes are name-mangled rather than truly inaccessible, and controlled access is typically provided through methods or @property."
# # 1. What are access modifiers in Python?

# # There are three commonly used access levels:

# # Public (variable) – Accessible from anywhere.
# # Protected (_variable) – Intended for internal use; accessible but should be treated as non-public.
# # Private (__variable) – Name-mangled to reduce accidental access.
# # 2. Does Python have true private variables?

# # No. Python does not enforce true private access. Double underscores trigger name mangling, but the attribute can still be accessed using its mangled name (for example, object._ClassName__attribute).

# # 3. What is name mangling?

# # When an attribute starts with two underscores, Python internally renames it.

# # Example:

# # class Bag:
# #     def __init__(self):
# #         self.__notes = "Important"

# # Internally becomes:

# # self._Bag__notes
# # 4. Why use private variables?

# # To hide implementation details and reduce accidental modification by users of the class.

# # 5. Difference between _ and __
# # Modifier	Meaning	Accessible Outside?
# # name	Public	Yes
# # _name	Protected (convention)	Yes
# # __name	Private (name mangling)	Not directly; use the mangled name if needed

# # This distinction is important in Python interviews because _ is a convention, whereas __ changes the attribute's name internally.