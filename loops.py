# loops.py

# For loop with range()

print("For Loop:")
for i in range(5):
    print(i)


# range(start, stop)

print("\nRange from 1 to 5:")
for i in range(1, 6):
    print(i)


# While loop

print("\nWhile Loop:")

i = 1

while i <= 5:
    print(i)
    i += 1


# Break statement
# break exits the loop completely

print("\nBreak Example:")

for i in range(1, 10):
    if i == 5:
        break
    print(i)


# Continue statement
# continue skips the current iteration

print("\nContinue Example:")

for i in range(1, 6):
    if i == 3:
        continue
    print(i)


# Pass statement
# pass does nothing, used as a placeholder

print("\nPass Example:")

for i in range(1, 5):
    if i == 2:
        pass
    print(i)


# Nested loops

print("\nNested Loop:")

for i in range(1, 4):
    for j in range(1, 4):
        print(i, j)


# Loop through a list

print("\nList Loop:")

fruits = ["Apple", "Banana", "Mango"]

for fruit in fruits:
    print(fruit)


# FizzBuzz using loops

print("\nFizzBuzz:")

for i in range(1, 16):
    if i % 3 == 0 and i % 5 == 0:
        print("FizzBuzz")
    elif i % 3 == 0:
        print("Fizz")
    elif i % 5 == 0:
        print("Buzz")
    else:
        print(i)
