# 6. @property Decorator

# Suppose you have

class Student:

    def __init__(self):
        self.marks=90

# Access

print(Student.marks)

# Suppose later you want

# Percentage

# Grade

# Validation

# without changing user code.

# That's where @property helps.

# Without Property
class Student:

    def get_marks(self):
        return 90

s=Student()

print(s.get_marks())

# Need

()
# With Property
class Student:

    @property
    def marks(self):
        return 90

s=Student()

print(s.marks)

# Output

# 90

# Looks like a variable but actually calls a method.

# Internally

# s.marks

# becomes

# s.marks()

# through the property descriptor (without writing parentheses yourself).

# Why use @property?

# Hide calculations.

# Validation.

# Read-only attributes.

# Backward compatibility.