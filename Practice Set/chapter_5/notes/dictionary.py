# dictionary.py

# Dictionary is a collection of keys-value pairs.

# A dictionary is faster because it uses hashing, which allows Python to find values directly instead of searching one by one.
# Dictionaries use hashing internally in Python.
# A dictionary stores data as key-value pairs.

# Example:

# d = {
#     "name": "Rahul",
#     "age": 20
# }

# Python calculates the hash of the keys:

# hash("name")
# hash("age")

# The hash helps Python find the value quickly.

# print(d["name"])

# Python:

# Calculates hash of "name".
# Finds the location of that key.
# Returns "Rahul".

# Dictionary keys must be hashable.

# Valid:

# d = {
#     "name": "Rahul",
#     1: "one",
#     (1, 2): "tuple"
# }


# Invalid:

# d = {
#     [1, 2]: "list"
# }

# because lists are mutable.

# Properties Of Python Dictionaries
# It is unordered.
# It is mutable.
# It is indexed.
# Cannot contain duplicate keys.

# Dictionary Methods
# Consider the following dictionary
# a={"name":"harry","from":"india","marks":[92,98,96]}
# a.items(): Returns a list of (key,value) tuples.
# a.keys(): Returns a list containing dictionary's keys.
# a.update({"friends":}): Updates the dictionary with supplied key-value pairs.
# a.get("name"): Returns the value of the specified keys

student = {
    "name": "Rahul",
    "age": 21,
    "course": "Python"
}

print("Student Details")
print(student)

print("Name:", student["name"])

student["age"] = 22
student["city"] = "Nagpur"

print("\nUpdated Dictionary:")
print(student)

print("\nKeys:")
for key in student:
    print(key)

print("\nKey-Value Pairs:")
for key, value in student.items():
    print(f"{key}: {value}")


# dictionary_methods.py

# Creating a dictionary

student = {
    "name": "Rahul",
    "age": 21,
    "course": "Python",
    "marks": 85
}

print("Original Dictionary:")
print(student)


# keys() - returns all keys

print("\nKeys:")
print(student.keys())


# values() - returns all values

print("\nValues:")
print(student.values())


# items() - returns key-value pairs

print("\nItems:")
print(student.items())


# get() method

print("\nUsing get():")

print(student.get("name"))
print(student.get("city"))  # Returns None if key does not exist
print(student.get("city", "Not Found"))  # Default value


# Difference between [] and get()

print("\nDictionary Access:")

print(student["name"])

# student["city"]  -> Gives KeyError because key doesn't exist

print(student.get("city"))  # Safe access


# update() method

print("\nUpdate Method:")

new_data = {
    "age": 22,
    "city": "Nagpur"
}

student.update(new_data)

print(student)


# pop() method

print("\nPop Method:")

removed_value = student.pop("marks")

print("Removed Marks:", removed_value)
print("Updated Dictionary:", student)


# Loop through dictionary

print("\nLoop Through Dictionary:")

for key, value in student.items():
    print(key, ":", value)


# Nested dictionary

print("\nNested Dictionary:")

students = {
    "student1": {
        "name": "Rahul",
        "age": 21
    },
    "student2": {
        "name": "Amit",
        "age": 22
    }
}

print(students["student1"]["name"])
