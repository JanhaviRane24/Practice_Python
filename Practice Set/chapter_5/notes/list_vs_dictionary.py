# Example: List vs Dictionary
# Searching in a list (slow)
numbers = [10, 20, 30, 40, 50]

if 40 in numbers:
    print("Found")

# Python checks each element one by one:

# 10 → 20 → 30 → 40

# This is called linear search.

# Time complexity:

# O(n)

# (where n is the number of items)

# Searching in a dictionary (fast)
student = {
    "name": "Rahul",
    "age": 20,
    "course": "MCA"
}

print(student["course"])

# Python does not check every key.

# It:

# Calculates the hash of "course".
# Uses that hash to find the memory location.
# Directly retrieves the value.

# Average time complexity:

# O(1)

# (constant time)

# Why hashing makes it fast

# A dictionary stores data like this internally:

# Key        Hash value        Location
# --------------------------------------
# "name"     12345             Value
# "age"      67890             Value
# "course"   54321             Value

# When you ask:

# student["course"]

# Python calculates:

# hash("course") → 54321

# and jumps directly to that location.

# # Simple comparison:
# | Operation            | List                    | Dictionary                 |
# | -------------------- | ----------------------- | -------------------------- |
# | Search               | Checks items one by one | Uses hash to jump directly |
# | Average lookup speed | O(n)                    | O(1)                       |
# | Uses hashing         | ❌ No                    | ✅ Yes                   |
# | Access method        | Index                   | Key                        |


# That's why dictionaries are usually much faster than lists for searching data by a key.