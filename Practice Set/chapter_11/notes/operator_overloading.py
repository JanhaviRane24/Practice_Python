# 5. Operator Overloading

# Python operators call dunder methods.

# Example

# +

# ↓

# __add__()
# -

# ↓

# __sub__()
# *

# ↓

# __mul__()

# Example without overloading

print(5+4)

# Internally

# 5.__add__(4)

# Now overload

class Number:

    def __init__(self,value):
        self.value=value

    def __add__(self,other):
        return self.value+other.value

n1=Number(10)
n2=Number(20)

print(n1+n2)

# Output

# 30
# Step-by-Step
# n1+n2

# ↓

# n1.__add__(n2)

# ↓

# self=n1

# other=n2

# ↓

# 10+20

# ↓

# 30

# Another Example

class Book:

    def __init__(self,pages):
        self.pages=pages

    def __add__(self,other):
        return self.pages+other.pages

b1=Book(100)
b2=Book(200)

print(b1+b2)

# Output

# 300

# Common Operator Overloading Methods

# Operator	Method
# +	add
# -	sub
# *	mul
# /	truediv
# ==	eq
# >	gt
# <	lt
