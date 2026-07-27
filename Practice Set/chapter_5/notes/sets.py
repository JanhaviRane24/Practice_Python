# sets.py

# Set is a collection of non-repetitive elements.

# sets use hashing internally in Python.
# A set stores only unique elements. To quickly check whether an element already exists, Python uses the element's hash value.

# s = {10, 20, 30}
# print(hash(10))
# print(hash(20))

# Output will be hash values (numbers may vary between runs).
# When you do:

# s.add(20)

# Python checks the hash of 20. Since 20 already exists, it does not add it again.
# Therefore, set elements must be hashable.

# Properties Of Sets
# Sets are unordered => Elementʼs order doesnʼt matter
# Sets are unindexed => Cannot access elements by index
# There is no way to change items in sets.
# Sets cannot contain duplicate values

# Operations On Sets
# Consider the following set:
# s = {1,8,2,3}
# len(s): Returns 4, the length of the set
# s.remove(8): Updates the set s and removes 8 from s.
# s.pop(): Removes an arbitrary element from the set and return the element removed.
# s.clear(): empties the set s.
# s.union({8,11}): Returns a new set with all items from both sets.
# s.intersection({8,11}): Returns a set which contains only item in both sets {8}

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
