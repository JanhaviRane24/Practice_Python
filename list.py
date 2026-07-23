# list.py

fruits = ["Apple", "Banana", "Orange", "Mango"]

print("Original List:", fruits)

fruits.append("Grapes")
print("After Append:", fruits)

fruits.insert(1, "Pineapple")
print("After Insert:", fruits)

fruits.remove("Orange")
print("After Remove:", fruits)

print("First Fruit:", fruits[0])

print("Looping Through List:")
for fruit in fruits:
    print(fruit)

print("List Length:", len(fruits))
