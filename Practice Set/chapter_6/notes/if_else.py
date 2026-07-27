# # if_else.py
# If else and elif statements are a multiway decision taken by our program due to certain conditions in our code.

# Syntax:
# if(condition1): # if condition1 is True
# print("yes")
# elif(condition2): # if condition2 is True
# print("no")
# else:             
# # otherwise
# print("maybe")

# Elif Clause
# elif in python means [else if]. An if statements can be chained together with a lot of these elif statements
# followed by an else statement

# Important Notes:
# 1. There can be any number of elif statements.
# 2. Last else is executed only if all the conditions inside elifs fail

age = int(input("Enter your age: "))

if age >= 18:
    print("You are eligible to vote.")
else:
    print("You are not eligible to vote.")

marks = int(input("Enter your marks: "))

if marks >= 90:
    print("Grade: A")
elif marks >= 75:
    print("Grade: B")
elif marks >= 60:
    print("Grade: C")
elif marks >= 40:
    print("Grade: D")
else:
    print("Fail")

number = int(input("Enter a number: "))

if number > 0:
    print("Positive Number")
elif number < 0:
    print("Negative Number")
else:
    print("Zero")