"""
REGULAR EXPRESSIONS
-------------------

Used for searching patterns in strings.
"""


import re



text = "My phone number is 12345"



# search()

result = re.search(
    r"\d+",
    text
)


print(result.group())



# findall()

numbers = re.findall(
    r"\d+",
    "a1 b22 c333"
)


print(numbers)



# match()

result = re.match(
    r"Hello",
    "Hello Python"
)


print(result.group())


"""
Explanation
search()

Searches anywhere:

re.search()

Example:

Hello 123
     ^
match()

Only checks beginning:

Hello Python
^^^^^
findall()

Returns all matches:

Example:

['1','22','333']
"""