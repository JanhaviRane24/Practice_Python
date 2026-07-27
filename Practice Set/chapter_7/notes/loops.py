# loops.py

# Loops In Python
# CHAPTER 07
# Sometimes we want to repeat a set of statements in our program. For instance: Print 1 to 1000.
# Loops make it easy for a programmer to tell the computer which set of instructions to repeat and how!

# Types Of Loops In Python
# Primarily there are two types of loops in python.
# while loops
# for loops

# While Loop
# Syntax:
# while (condition): # The block keeps executing until the condition is true
# Body of the loop

# In while loops, the condition is checked first. If it evaluates to true, the body of the loop is executed
# otherwise not!
# If the loop is entered, the process of [condition check & execution] is continued until the condition
# # becomes False
# Note: If the condition never become false, the loop keeps getting executed.

# For Loop
# A for loop is used to iterate through a sequence like list, tuple, or string [iterables]
# Syntax:
# l = [1, 7, 8]
# for item in l:
# print(item) # prints 1, 7 and 8


# Range Function In Python
# The range() function in python is used to generate a sequence of number.
# We can also specify the start, stop and step-size as follows:
# range(start, stop, step_size)
# step_size is usually not used with range()

# For Loop With Else
# An optional else can be used with a for loop if the code is to be executed when the loops exhausts.
# Example:
# l= [1,7,8]
# for item in l:
# print(item)
# else:
# print("done") # this is printed when the loop exhausts

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


# The Break Statement
# break exits the loop completely
# ‘breakʼ is used to come out of the loop when encountered. It instructs the program to – exit the loop now

print("\nBreak Example:")

for i in range(1, 10):
    if i == 5:
        break
    print(i)


# The Continue Statement
# ‘continueʼ is used to stop the current iteration of the loop and continue with the next one. It instructs the
# Program to “skip this iteration”.
# continue skips the current iteration

print("\nContinue Example:")

for i in range(1, 6):
    if i == 3:
        continue
    print(i)


# Pass Statement
# pass is a null statement in python.
# It instructs to “do nothing”
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
