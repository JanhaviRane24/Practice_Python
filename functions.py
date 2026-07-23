# functions.py

def greet(name):
    print(f"Hello, {name}!")


def add(a, b):
    return a + b


def square(number):
    return number * number


def is_even(number):
    return number % 2 == 0


greet("Rahul")

result = add(10, 20)
print("Sum:", result)

print("Square:", square(7))

num = 8
if is_even(num):
    print(num, "is Even")
else:
    print(num, "is Odd")
