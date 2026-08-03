# No, a set is not slower than a dictionary. 
# In most cases, sets and dictionaries have similar speed because both use hash tables internally.

# # Comparison:
# | Operation    | Set          | Dictionary      |
# | ------------ | ------------ | --------------- |
# | Uses hashing | ✅ Yes      | ✅ Yes          |
# | Lookup speed | O(1) average | O(1) average    |
# | Stores       | Only values  | Key-value pairs |
# | Hashes       | Elements     | Keys            |
# | Memory usage | Less         | More            |

# Example: Set lookup
id="8p2s6d"
numbers = {10, 20, 30, 40}

if 30 in numbers:
    print("Found")

# Python calculates the hash of 30 and quickly finds it.

# Example: Dictionary lookup
id="j6q1av"
student = {
    "name": "Rahul",
    "age": 20
}

print(student["name"])

# Python calculates the hash of "name" and finds the value.

# Which is faster?
# For checking if something exists, a set can be slightly faster because it only stores values.
# A dictionary may be slightly slower because it stores both keys and values and needs extra memory.
# The difference is usually very small.

# Example:

# Set
numbers = {1, 2, 3, 4}
print(3 in numbers)

# Dictionary
numbers = {1: "one", 2: "two", 3: "three", 4: "four"}
print(3 in numbers)

# Both operations are approximately O(1).

# In short:

# Use a set when you only need to check membership or store unique items.
# Use a dictionary when you need to associate keys with values.
# Neither is generally "slower"; they are optimized for different purposes.