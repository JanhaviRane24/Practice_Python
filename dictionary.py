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
