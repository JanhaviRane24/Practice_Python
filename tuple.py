# tuple.py

colors = ("Red", "Green", "Blue", "Yellow")

print("Tuple:", colors)
print("First Color:", colors[0])
print("Last Color:", colors[-1])
print("Length:", len(colors))

for color in colors:
    print(color)

print("Index of Green:", colors.index("Green"))
print("Count of Red:", colors.count("Red"))

# tuples_sets.py


# =========================
# Tuples - Immutable
# =========================

# Creating a tuple

point = (3, 4)

print("Original Tuple:")
print(point)


# Indexing

print("\nTuple Indexing:")
print("First value:", point[0])
print("Second value:", point[1])


# count() - counts occurrences

numbers = (1, 2, 3, 2, 2, 4)

print("\nTuple count():")
print(numbers.count(2))


# index() - returns first index

print("\nTuple index():")
print(numbers.index(3))


# Tuple packing

print("\nTuple Packing:")

coordinates = 10, 20

print(coordinates)


# Tuple unpacking

print("\nTuple Unpacking:")

x, y = coordinates

print("x =", x)
print("y =", y)


# Nested tuple

student = ("Rahul", 21, ("Python", "SQL"))

print("\nNested Tuple:")
print(student)


# Tuple cannot be modified

# point[0] = 5
# This gives TypeError because tuples are immutable



# =========================
# Sets - Mutable and Unordered
# =========================

print("\n\nSets:")


# Creating a set

fruits = {"Apple", "Banana", "Mango"}

print("Original Set:")
print(fruits)


# add()

fruits.add("Orange")

print("\nAfter add:")
print(fruits)


# remove()

fruits.remove("Banana")

print("\nAfter remove:")
print(fruits)


# Set operations

set1 = {1, 2, 3, 4}
set2 = {3, 4, 5, 6}


# union()

print("\nUnion:")
print(set1.union(set2))


# intersection()

print("\nIntersection:")
print(set1.intersection(set2))


# difference()

print("\nDifference:")
print(set1.difference(set2))


# Membership checking

print("\nMembership Check:")

print(3 in set1)
print(10 in set1)



# Remove duplicates using set

print("\nRemove Duplicates:")

nums = [1, 2, 2, 3, 3, 3]

unique = list(set(nums))

print("Original:", nums)
print("Unique:", unique)


# Order preserving duplicate removal

print("\nOrder Preserving:")

unique_ordered = list(dict.fromkeys(nums))

print(unique_ordered)



# Set vs List search example

print("\nSet Search:")

my_set = {10, 20, 30, 40}

if 20 in my_set:
    print("20 exists in set")
