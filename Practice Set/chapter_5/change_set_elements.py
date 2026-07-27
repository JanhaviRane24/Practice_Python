# 9. Can you change the values inside a list which is contained in set S?
s = {8, 7, 12, "Harry", [1,2]}
print(s)

# Traceback (most recent call last):
#   File "c:\Users\ranej\OneDrive\Desktop\Practice_Python\Practice Set\chapter_5\change_set_elements.py", line 2, in <module>
#     s = {8, 7, 12, "Harry", [1,2]}
#         ^^^^^^^^^^^^^^^^^^^^^^^^^^
# TypeError: unhashable type: 'list'
# PS C:\Users\ranej\OneDrive\Desktop\Practice_Python> 

# A set can only contain hashable (immutable) elements, such as:

# int
# float
# str
# tuple (if it contains only immutable elements)
# s = {8, 7, 12, "Harry", (1, 2)}
# print(s)
# {'Harry', (1, 2), 7, 8, 12}


# A list is mutable (its contents can be changed), so it is unhashable and cannot be stored in a set.