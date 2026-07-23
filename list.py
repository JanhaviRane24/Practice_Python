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


# lists_methods.py

# List is mutable and ordered

numbers = [4, 8, 2, 9, 1]

print("Original List:")
print(numbers)


# append() - adds one item at the end

numbers.append(10)
print("\nAfter append:")
print(numbers)


# extend() - adds multiple items

numbers.extend([20, 30])
print("\nAfter extend:")
print(numbers)


# insert(index, value)

numbers.insert(1, 100)
print("\nAfter insert:")
print(numbers)


# remove(value) - removes first occurrence

numbers.remove(100)
print("\nAfter remove:")
print(numbers)


# pop() - removes and returns item

removed = numbers.pop()

print("\nRemoved item:", removed)
print("After pop:")
print(numbers)


# reverse()

numbers.reverse()
print("\nAfter reverse:")
print(numbers)


# copy()

new_list = numbers.copy()

print("\nCopied List:")
print(new_list)


# sort()

numbers.sort()

print("\nAfter sort:")
print(numbers)


# del keyword

del numbers[0]

print("\nAfter deleting first item:")
print(numbers)


# Reverse a number

print("\nReverse Number:")

num = 98765
rev = 0

while num > 0:
    rev = rev * 10 + num % 10
    num = num // 10

print(rev)


# Find largest without max()

print("\nFind Largest:")

nums = [4, 8, 2, 9, 1]

largest = nums[0]

for n in nums:
    if n > largest:
        largest = n

print("Largest:", largest)


# Find smallest without min()

smallest = nums[0]

for n in nums:
    if n < smallest:
        smallest = n

print("Smallest:", smallest)


# Remove duplicates

print("\nRemove Duplicates:")

nums = [1, 2, 2, 3, 3, 3]

unique = list(set(nums))

print("Without order:", unique)


# Order preserving duplicate removal

unique_ordered = list(dict.fromkeys(nums))

print("With order:", unique_ordered)


# append vs extend example

print("\nAppend vs Extend:")

a = [1, 2]
a.append([3, 4])

print("append:", a)


a2 = [1, 2]
a2.extend([3, 4])

print("extend:", a2)


# remove first occurrence example

print("\nRemove First Occurrence:")

values = [20, 30, 20, 40]

values.remove(20)

print(values)
