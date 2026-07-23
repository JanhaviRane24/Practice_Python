# dictionary.py

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
