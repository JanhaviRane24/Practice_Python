# exception_handling.py


# Basic try-except example

print("Basic Exception Handling:")

try:
    number = 10 / 0
    print(number)

except ZeroDivisionError:
    print("Cannot divide by zero")



# Multiple except blocks

print("\nMultiple Exceptions:")

try:
    value = int(input("Enter a number: "))
    result = 100 / value
    print("Result:", result)

except ValueError:
    print("Please enter a valid integer")

except ZeroDivisionError:
    print("Number cannot be zero")



# IndexError

print("\nIndex Error:")

numbers = [10, 20, 30]

try:
    print(numbers[5])

except IndexError:
    print("Index does not exist")



# KeyError

print("\nKey Error:")

student = {
    "name": "Pavan",
    "age": 21
}

try:
    print(student["city"])

except KeyError:
    print("Key does not exist")



# TypeError

print("\nType Error:")

try:
    result = "10" + 5

except TypeError:
    print("Cannot add string and integer")



# try-except-else-finally

print("\nElse and Finally Example:")

try:
    num = 10 / 2

except ZeroDivisionError:
    print("Division error")

else:
    print("No exception occurred")
    print("Result:", num)

finally:
    print("This block always executes")



# Custom Exception

print("\nCustom Exception:")


class InsufficientBalanceError(Exception):
    pass



def withdraw(balance, amount):

    if amount > balance:
        raise InsufficientBalanceError("Not enough balance")

    return balance - amount



try:
    remaining_balance = withdraw(5000, 6000)
    print("Remaining Balance:", remaining_balance)

except InsufficientBalanceError as error:
    print(error)



# Difference between bare except and specific exception

print("\nSpecific Exception Example:")

try:
    x = int("abc")

except ValueError:
    print("Value conversion failed")


# Avoid using:
#
# except:
#     print("Something went wrong")
#
# because it catches every error and can hide bugs.
