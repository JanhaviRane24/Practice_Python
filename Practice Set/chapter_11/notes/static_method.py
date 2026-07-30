
# 3. Static Method
# What is Static Method?

# A static method belongs to the class but does not access

# self
# cls

# Uses

# @staticmethod

# Example

class Calculator:

    @staticmethod
    def add(a, b):
        return a + b

print(Calculator.add(10,20))

# Output

# 30
# Step-by-Step

# Call

Calculator.add(10,20)

# Python simply executes

# a = 10
# b = 20

# Returns

# 30

# No object created.

# No self.

# No cls.

# Real-Life Example
class Employee:

    @staticmethod
    def company_policy():
        print("Office starts at 9 AM")

Employee.company_policy()

# Every employee has same rule.

# Difference
# Feature	Instance	Class	Static
# First parameter	self	cls	None
# Access instance variables	✅	❌	❌
# Access class variables	✅	✅	❌ (unless class name is used)
# Needs object	Yes	No	No
