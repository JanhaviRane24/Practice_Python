# 5. Dictionary Merge (|) and Update (|=) Operators
# What is a Dictionary?

# A dictionary stores data in key-value pairs.

# Example:

student = {
    "name": "Alice",
    "age": 20
}

print(student)
# Output
# {'name': 'Alice', 'age': 20}
# Why Do We Need Dictionary Merge?

# Suppose we have two dictionaries.

dict1 = {
    "a": 1,
    "b": 2
}

dict2 = {
    "c": 3,
    "d": 4
}

# We want one dictionary containing all data.

# Expected Result

# {
# 'a':1,
# 'b':2,
# 'c':3,
# 'd':4
# }

# Before Python 3.9, we had to use .update() or **.

# Python 3.9 introduced the cleaner | operator.

# Dictionary Merge (|)
# Syntax
# new_dict = dict1 | dict2

# It creates a new dictionary.

# The original dictionaries remain unchanged.

# Example 1
dict1 = {
    "a": 1,
    "b": 2
}

dict2 = {
    "c": 3,
    "d": 4
}

merged = dict1 | dict2

print(merged)
# Output
# {'a': 1, 'b': 2, 'c': 3, 'd': 4}
# Step-by-Step
# dict1

# ↓

# {'a':1,'b':2}

# dict2

# ↓

# {'c':3,'d':4}

# ↓

# Merge

# ↓

# New Dictionary

# ↓

# {'a':1,'b':2,'c':3,'d':4}
# Original Dictionaries
print(dict1)
print(dict2)

# Output

# {'a': 1, 'b': 2}
# {'c': 3, 'd': 4}

# Notice they did not change.

# Example 2 (Same Keys)
dict1 = {
    "a": 1,
    "b": 2
}

dict2 = {
    "b": 10,
    "c": 30
}

merged = dict1 | dict2

print(merged)
# Output
# {'a': 1, 'b': 10, 'c': 30}
# Step-by-Step
# dict1

# ↓

# b = 2

# dict2

# ↓

# b = 10

# ↓

# Same key found

# ↓

# Right dictionary wins

# ↓

# b = 10

# Final Dictionary

# {
# 'a':1,
# 'b':10,
# 'c':30
# }
# Important Rule

# When both dictionaries have the same key,

# The value from the right-side dictionary replaces the left-side value.

# dict1 | dict2

# dict2 wins.

# More Example
student = {
    "name": "Alice",
    "age": 20
}

marks = {
    "math": 90,
    "science": 85
}

result = student | marks

print(result)

# Output

# {'name': 'Alice', 'age': 20, 'math': 90, 'science': 85}
# Dictionary Update (|=)

# Now let's learn another operator.

# Syntax
# dict1 |= dict2

# Unlike |, this modifies the original dictionary.

# Example 1
dict1 = {
    "a": 1,
    "b": 2
}

dict2 = {
    "c": 3
}

dict1 |= dict2

print(dict1)

# Output

# {'a': 1, 'b': 2, 'c': 3}
# Step-by-Step
# dict1

# ↓

# {'a':1,'b':2}

# ↓

# Add dict2

# ↓

# dict1 changes

# ↓

# {'a':1,'b':2,'c':3}

# Notice

# There is no new dictionary.

# The existing one changes.

# Example 2
dict1 = {
    "a": 1,
    "b": 2
}

dict2 = {
    "b": 100,
    "d": 4
}

dict1 |= dict2

print(dict1)

# Output

# {'a': 1, 'b': 100, 'd': 4}
# Step-by-Step
# dict1

# ↓

# b = 2

# dict2

# ↓

# b = 100

# ↓

# Update existing key

# ↓

# dict1 becomes

# ↓

# {
# 'a':1,
# 'b':100,
# 'd':4
# }
# Difference Between | and |=
# Using |
dict1 = {"a": 1}
dict2 = {"b": 2}

result = dict1 | dict2

print(result)
print(dict1)

# Output

# {'a': 1, 'b': 2}
# {'a': 1}

# dict1 is unchanged.

# Using |=
dict1 = {"a": 1}
dict2 = {"b": 2}

dict1 |= dict2

print(dict1)

# Output

# {'a': 1, 'b': 2}

# dict1 has changed.

# How is |= Different from .update()?
# Using .update()
dict1 = {
    "a": 1
}

dict2 = {
    "b": 2
}

dict1.update(dict2)

print(dict1)

# Output

# {'a': 1, 'b': 2}
# Using |=
dict1 = {
    "a": 1
}

dict2 = {
    "b": 2
}

dict1 |= dict2

print(dict1)

# Output

# {'a': 1, 'b': 2}

# Both do the same thing.

# The only difference is that |= is newer and often considered more readable.

# Comparison Table

# | Feature | | | |= | .update() |
# |---------|-----|------|-------------|
# | Creates new dictionary | ✅ Yes | ❌ No | ❌ No |
# | Changes original dictionary | ❌ No | ✅ Yes | ✅ Yes |
# | Introduced | Python 3.9 | Python 3.9 | Available from older versions |

# Interview Questions
# 1. What does the | operator do?

# Answer:
# It merges two dictionaries and returns a new dictionary without modifying the originals.

# 2. What does the |= operator do?

# Answer:
# It updates the left dictionary by adding or replacing keys from the right dictionary.

# 3. If both dictionaries have the same key, which value is kept?

# Answer:
# The value from the right-hand dictionary replaces the value from the left-hand dictionary.

# Example:

# dict1 = {"x": 1}
# dict2 = {"x": 100}

# print(dict1 | dict2)

# Output:

# {'x': 100}
# Quick Revision
# # Merge (creates a new dictionary)
# d1 = {"a": 1}
# d2 = {"b": 2}

# d3 = d1 | d2
# print(d3)   # {'a': 1, 'b': 2}
# print(d1)   # {'a': 1}

# # Update (modifies original dictionary)
# d1 |= d2
# print(d1)   # {'a': 1, 'b': 2}
# Summary
# | Operator       | Meaning                     | Original Dictionary |             |
# | -------------- | --------------------------- | ------------------- | ----------- |
# | `              | `                           | Merge dictionaries  | Not changed |
# | `              | =`                          | Update dictionary   | Changed     |
# | Duplicate Keys | Right dictionary value wins | Applies to both     |             |
