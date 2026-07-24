"""
LIST COMPREHENSION
------------------

Short way to create lists.
"""


# Normal loop

numbers = []

for i in range(1,6):

    numbers.append(i)


print(numbers)



# List comprehension

numbers = [i for i in range(1,6)]

print(numbers)



# With condition

evens = [
    i 
    for i in range(1,20)
    if i % 2 == 0
]


print(evens)



# Transformation example

squares = [
    i*i 
    for i in range(1,6)
]


print(squares)

"""
Explanation

List comprehension:

[value for item in iterable if condition]

Example:

[i for i in range(5)]

creates:

[0,1,2,3,4]

Advantages:

shorter code
readable
faster for simple operations
"""