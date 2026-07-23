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


# functions_concepts.py


# Basic Function

def greet():
    print("Hello, Python!")


greet()


# Function with parameters

def greet_user(name):
    print("Hello,", name)


greet_user("Pavan")


# Function with return value

def add(a, b):
    return a + b


result = add(10, 20)

print("\nAddition:", result)


# Parameters vs Arguments

# a and b are parameters
def multiply(a, b):
    return a * b


# 5 and 4 are arguments
print("\nMultiplication:", multiply(5, 4))



# Function without return

def show_message():
    print("\nThis function has no return value")


value = show_message()

print("Returned value:", value)
# Output will be None



# Default Parameters

def student(name, course="Python"):
    print(name, course)


print("\nDefault Parameter:")
student("Pavan")
student("Rahul", "Java")



# *args - variable number of positional arguments

def add_numbers(*args):
    print("\nArgs:", args)
    
    total = 0
    
    for num in args:
        total += num
        
    return total


print("Sum:", add_numbers(1, 2, 3, 4))


# **kwargs - variable number of keyword arguments

def display_info(**kwargs):
    print("\nKwargs:")
    
    for key, value in kwargs.items():
        print(key, ":", value)


display_info(name="Pavan", age=21, city="Nagpur")



# Using *args and **kwargs together

def demo(*args, **kwargs):
    print("\nDemo args:", args)
    print("Demo kwargs:", kwargs)


demo(1, 2, name="Pavan", role="Developer")



# Lambda Function

square = lambda x: x * x

print("\nLambda Square:")
print(square(5))


# Lambda with multiple arguments

addition = lambda a, b: a + b

print("Lambda Addition:")
print(addition(10, 20))



# Lambda with sorted()

students = [
    ("Rahul", 85),
    ("Pavan", 95),
    ("Amit", 75)
]

sorted_students = sorted(
    students,
    key=lambda student: student[1]
)

print("\nSorted Students:")
print(sorted_students)



# Lambda with map()

numbers = [1, 2, 3, 4, 5]

squared_numbers = list(
    map(lambda x: x * x, numbers)
)

print("\nMap Example:")
print(squared_numbers)



# Lambda with filter()

even_numbers = list(
    filter(lambda x: x % 2 == 0, numbers)
)

print("\nFilter Example:")
print(even_numbers)
