# conditional_statements.py

# Simple if statement

age = 18

if age >= 18:
    print("You are eligible to vote.")


# if-else statement

number = 10

if number % 2 == 0:
    print("Number is Even")
else:
    print("Number is Odd")


# if-elif-else statement

marks = 85

if marks >= 90:
    print("Grade: A+")
elif marks >= 75:
    print("Grade: A")
elif marks >= 60:
    print("Grade: B")
elif marks >= 40:
    print("Grade: C")
else:
    print("Fail")


# Nested if statement

username = "admin"
password = "12345"

if username == "admin":
    if password == "12345":
        print("Login Successful")
    else:
        print("Wrong Password")
else:
    print("Invalid Username")


# FizzBuzz Example

print("\nFizzBuzz:")

for i in range(1, 21):
    if i % 3 == 0 and i % 5 == 0:
        print(i, "FizzBuzz")
    elif i % 3 == 0:
        print(i, "Fizz")
    elif i % 5 == 0:
        print(i, "Buzz")
    else:
        print(i)
