"""
IMPORTANT PYTHON BUILT-IN FUNCTIONS
"""


numbers = [5,2,8,1,9]


# length

print(len(numbers))


# range

for i in range(5):

    print(i)



# sum

print(sum(numbers))


# maximum

print(max(numbers))


# minimum

print(min(numbers))


# sorted()

new_list = sorted(numbers)


print(new_list)

print(numbers)



# all()

positive = [1,2,3,4]


print(
    all(x > 0 for x in positive)
)



negative = [1,-2,3]


print(
    all(x > 0 for x in negative)
)

"""
Explanation
sort() vs sorted()

sort()

list.sort()
modifies original list
returns None

Example:

nums.sort()

sorted()

sorted(nums)
creates a new list
original remains unchanged
works with any iterable
all()

Returns True only if every item is True.

Example:

all(x > 0 for x in [1,2,3])

Output:

True
"""