# Method 1: Default arguments
class Calculator:
    def add(self, a, b, c=0):
        return a + b + c

c = Calculator()

print(c.add(1, 2))
print(c.add(1, 2, 4))

# Method 2: Variable-length arguments (*args) ✅ Recommended
class Calculator:
    def add(self, *args):
        return sum(args)

c = Calculator()

print(c.add(1, 2))
print(c.add(1, 2, 4))
print(c.add(1, 2, 3, 4, 5))