# 4. Match-Case Statement (Python 3.10+)
# What is Match-Case?

# The match-case statement is similar to the switch-case statement in languages like Java, C++, and C#.

# It compares a value against different cases and executes the matching block.

# Syntax
# match variable:
#     case value1:
#         # Code
#     case value2:
#         # Code
#     case _:
#         # Default case
# Important Keywords
# Keyword	Meaning
# match	Checks a value against different cases
# case	A possible matching value
# _	Default case (like default in Java/C++)
# Before Python 3.10

# Suppose we want to print a day based on its number.

day = 2

if day == 1:
    print("Monday")
elif day == 2:
    print("Tuesday")
elif day == 3:
    print("Wednesday")
else:
    print("Invalid Day")
# Output
# Tuesday

# Notice how we keep writing day ==.

# Using Match-Case
day = 2

match day:
    case 1:
        print("Monday")
    case 2:
        print("Tuesday")
    case 3:
        print("Wednesday")
    case _:
        print("Invalid Day")
# Output
# Tuesday
# Step-by-Step Execution
# day = 2

# ↓

# match day

# ↓

# Case 1 ?
# 2 == 1
# False

# ↓

# Case 2 ?
# 2 == 2
# True

# ↓

# Print
# Tuesday

# ↓

# Stop checking remaining cases
# Example 2 – HTTP Status Code
def http_status(status):
    match status:
        case 200:
            return "OK"
        case 404:
            return "Not Found"
        case 500:
            return "Internal Server Error"
        case _:
            return "Unknown Status"

print(http_status(200))
print(http_status(404))
print(http_status(500))
print(http_status(300))
# Output
# OK
# Not Found
# Internal Server Error
# Unknown Status
# Step-by-Step (status = 404)
# status = 404

# ↓

# match status

# ↓

# 200 ?
# False

# ↓

# 404 ?
# True

# ↓

# Return "Not Found"
# Example 3 – Grade System
grade = "B"

match grade:
    case "A":
        print("Excellent")
    case "B":
        print("Very Good")
    case "C":
        print("Good")
    case _:
        print("Invalid Grade")
# Output
# Very Good
# Example 4 – Calculator
num1 = 10
num2 = 5
operator = "+"

match operator:
    case "+":
        print(num1 + num2)
    case "-":
        print(num1 - num2)
    case "*":
        print(num1 * num2)
    case "/":
        print(num1 / num2)
    case _:
        print("Invalid Operator")
# Output
# 15
# Example 5 – Multiple Values in One Case

# You can match multiple values using |.

day = 6

match day:
    case 1 | 7:
        print("Weekend")
    case 2 | 3 | 4 | 5 | 6:
        print("Weekday")
# Output
# Weekday
# Step-by-Step
# day = 6

# ↓

# 1 or 7 ?
# False

# ↓

# 2 or 3 or 4 or 5 or 6 ?

# ↓

# 6 matches

# ↓

# Print Weekday
# Example 6 – Matching Strings
fruit = "Apple"

match fruit:
    case "Apple":
        print("Red Fruit")
    case "Banana":
        print("Yellow Fruit")
    case "Orange":
        print("Orange Fruit")
    case _:
        print("Unknown Fruit")
# Output
# Red Fruit
# Example 7 – User Input
choice = int(input("Enter a number (1-3): "))

match choice:
    case 1:
        print("You selected One")
    case 2:
        print("You selected Two")
    case 3:
        print("You selected Three")
    case _:
        print("Invalid Choice")
# Suppose User Enters
# 2
# Execution
# choice = 2

# ↓

# match choice

# ↓

# case 1 ?
# False

# ↓

# case 2 ?
# True

# ↓

# Print

# You selected Two
# Match vs If-Else
# Using If-Else
number = 3

if number == 1:
    print("One")
elif number == 2:
    print("Two")
elif number == 3:
    print("Three")
else:
    print("Invalid")
# Using Match
number = 3

match number:
    case 1:
        print("One")
    case 2:
        print("Two")
    case 3:
        print("Three")
    case _:
        print("Invalid")

# Both give the same output:

# Three
# When Should You Use Match-Case?

# Use match-case when:

# You are comparing one variable against many fixed values.
# You want cleaner code than a long if-elif-else chain.

# Use if-elif-else when:

# Conditions involve ranges (age > 18).
# Conditions use logical operators (and, or).
# You need complex comparisons.

# For example, this cannot be written directly as simple match-case:

age = 20

if age >= 18:
    print("Adult")
else:
    print("Minor")
# Common Mistake

# ❌ Wrong

# match day:
#     case 1:
#         print("Monday")
#     default:
#         print("Invalid")

# There is no default keyword in Python.

# ✅ Correct

match day:
    case 1:
        print("Monday")
    case _:
        print("Invalid")

# Interview Questions
# 1. What is match-case in Python?

# Answer:
# match-case is a control flow statement introduced in Python 3.10. It compares a value against multiple cases and executes the matching block, similar to the switch statement in other programming languages.

# 2. What does case _ mean?

# Answer:
# case _ is the default case. It executes when none of the other cases match.

# 3. Can we use multiple values in one case?

# Answer: Yes.

# match day:
#     case 6 | 7:
#         print("Weekend")
# Summary
# Feature	Description
# match	Starts pattern matching
# case	Defines a value to compare
# case _	Default case
# `	`
# Introduced in	Python 3.10