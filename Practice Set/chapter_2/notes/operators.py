# operators.py

# Arithmetic Operators
a = 10
b = 3

print("Arithmetic Operators")
print("Addition:", a + b)
print("Subtraction:", a - b)
print("Multiplication:", a * b)
print("Division:", a / b)
print("Floor Division:", a // b)
print("Modulus:", a % b)
print("Power:", a ** b)


# Comparison Operators
print("\nComparison Operators")
print("a == b:", a == b)
print("a != b:", a != b)
print("a > b:", a > b)
print("a < b:", a < b)
print("a >= b:", a >= b)
print("a <= b:", a <= b)


# Assignment Operators
print("\nAssignment Operators")
x = 10
print("Initial x:", x)

x += 5
print("After +=:", x)

x -= 3
print("After -=:", x)

x *= 2
print("After *=:", x)

x /= 4
print("After /=:", x)


# Logical Operators
print("\nLogical Operators")

age = 20
has_id = True

print("and:", age >= 18 and has_id)
print("or:", age < 18 or has_id)
print("not:", not has_id)


# Membership Operators
print("\nMembership Operators")

languages = ["Python", "Java", "C++"]

print("'Python' in languages:", "Python" in languages)
print("'HTML' not in languages:", "HTML" not in languages)


# Identity Operators
print("\nIdentity Operators")

list1 = [1, 2, 3]
list2 = [1, 2, 3]
list3 = list1

print("list1 == list2:", list1 == list2)
print("list1 is list2:", list1 is list2)
print("list1 is list3:", list1 is list3)


# Bitwise Operators
print("\nBitwise Operators")

num1 = 5   # Binary: 101
num2 = 3   # Binary: 011

print("AND (&):", num1 & num2)
print("OR (|):", num1 | num2)
print("XOR (^):", num1 ^ num2)
print("NOT (~):", ~num1)
print("Left Shift (<<):", num1 << 1)
print("Right Shift (>>):", num1 >> 1)


# Difference between == and is

print("\nDifference between == and is")

x = [10, 20]
y = [10, 20]

print("x == y:", x == y)  # Same values
print("x is y:", x is y)  # Different objects
