# 1. Instance Method
# What is an Instance Method?

# An instance method works with object-specific data.

# First parameter is self
# Can access and modify instance variables.
# Called using an object.
# Syntax
class Student:

    def __init__(self, name):
        self.name = name

    def display(self):        # Instance Method
         print(self.name)
# Step-by-Step Execution
# Step 1
s1 = Student("Janhavi")

# Python internally does

# Student.__init__(s1, "Janhavi")

# Inside constructor

# self = s1
# self.name = "Janhavi"

# Now object becomes

# s1
# |
# +---- name = "Janhavi"
# Step 2
# s1.display()

# Internally Python converts it into

# Student.display(s1)

# Inside method

# self = s1

# Then

# print(self.name)

# prints

# Janhavi
# Complete Example
class Student:

    def __init__(self, name):
        self.name = name

    def display(self):
        print("Student:", self.name)

s1 = Student("Janhavi")
s2 = Student("Rahul")

s1.display()
s2.display()

# Output

# Student: Janhavi
# Student: Rahul
# Interview Point

# Instance methods can access

# ✔ Instance variables

# ✔ Class variables

# ✔ Other methods

