# sets.py

# Creating a set
fruits = {"Apple", "Banana", "Mango", "Orange"}

print("Original Set:", fruits)

# Adding an element
fruits.add("Grapes")
print("After Adding:", fruits)

# Removing an element
fruits.remove("Banana")
print("After Removing:", fruits)

# Checking if an element exists
if "Apple" in fruits:
    print("Apple is present in the set.")

# Loop through the set
print("\nElements in the set:")
for fruit in fruits:
    print(fruit)

# Set operations
set1 = {1, 2, 3, 4}
set2 = {3, 4, 5, 6}

print("\nSet 1:", set1)
print("Set 2:", set2)

print("Union:", set1.union(set2))
print("Intersection:", set1.intersection(set2))
print("Difference (set1 - set2):", set1.difference(set2))
print("Symmetric Difference:", set1.symmetric_difference(set2))

print("Length of set1:", len(set1))
