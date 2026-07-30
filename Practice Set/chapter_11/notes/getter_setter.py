# 7. Getter and Setter

# Suppose salary should never be negative.

# Without Setter

# emp.salary=-5000

# Wrong.

# Using Property

class Employee:

    def __init__(self):
        self._salary=0

    @property
    def salary(self):
        return self._salary

    @salary.setter
    def salary(self,value):

        if value<0:
            print("Invalid Salary")
        else:
            self._salary=value

e=Employee()

e.salary=50000

print(e.salary)

# Output

# 50000

# Now

# e.salary=-100

# Output

# Invalid Salary

# Salary remains unchanged.

# Step-by-Step
# Step 1
# e.salary=50000

# Python calls

# Employee.salary.fset(e, 50000)

# Inside setter

# value=50000

# 50000>0

# _store in _salary
# Step 2
# print(e.salary)

# Python calls

# Employee.salary.fget(e)

# Getter returns

# 50000
# Why use _salary instead of salary?

# If you write:

class Employee:
    @property
    def salary(self):
        return self.salary

#or

    @salary.setter
    def salary(self, value):
        self.salary = value

# the property keeps calling itself, causing infinite recursion and eventually a RecursionError.

# Using a separate internal variable like _salary avoids this:

class Employee:
    def __init__(self):
        self._salary = 0

    @property
    def salary(self):
        return self._salary

    @salary.setter
    def salary(self, value):
        self._salary = value

# Here:

# salary is the public property.
# _salary stores the actual value internally.