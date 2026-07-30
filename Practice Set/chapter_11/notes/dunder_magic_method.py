# 4. Dunder (Magic) Methods
# What are Dunder Methods?

# Dunder means

# Double Under Score

# Example

# __init__

# __str__

# __len__

# __add__

# __repr__

# __eq__

# Python automatically calls them.

# init

# Constructor

class Student:

    def __init__(self,name):
        self.name=name

# Automatically called during object creation.

Student("Janhavi")

# becomes

Student.__init__(object,"Janhavi")
str

# Controls

print(object)

# Example

class Student:

    def __init__(self,name):
        self.name=name

    def __str__(self):
        return self.name

s=Student("Janhavi")

print(s)

# Output

# Janhavi

# Without str

# <__main__.Student object at 0x...>
len
class Team:

    def __len__(self):
        return 5

t=Team()

print(len(t))

# Output

# 5

# Python internally

# len(t)

# ↓

# t.__len__()
# eq

# Used for

# ==

# Example

class Student:

    def __init__(self,marks):
        self.marks=marks

    def __eq__(self,other):
        return self.marks==other.marks

s1=Student(90)
s2=Student(90)

print(s1==s2)

# Output

# True