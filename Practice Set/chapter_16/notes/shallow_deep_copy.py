# 34. What is the difference between a shallow copy and a deep copy?
# Below is the tabular difference between the Shallow Copy and Deep Copy:

# shallowCopy.webpshallowCopy.webp
# Shallow Copy	Deep Copy
# Shallow Copy stores the references of objects to the original memory address.   	Deep copy stores copies of the object’s value.
# Shallow Copy reflects changes made to the new/copied object in the original object.	Deep copy doesn’t reflect changes made to the new/copied object in the original object.
# Shallow Copy stores the copy of the original object and points the references to the objects.	Deep copy stores the copy of the original object and recursively copies the objects as well.
# A shallow copy is faster.	Deep copy is comparatively slower.
# Shallow Copy vs Deep Copy (Short)
import copy

original = [1, 2, [3, 4]]
shallow = copy.copy(original)
deep = copy.deepcopy(original)

shallow[0] = 99          # outer level change
shallow[2].append(5)     # nested/inner level change

print(original)  # [1, 2, [3, 4, 5]]  <- only inner change leaked through
print(shallow)    # [99, 2, [3, 4, 5]]
print(deep)       # [1, 2, [3, 4]]
# Import the copy module:

import copy
# 1. Shallow Copy (copy.copy())
# Creates a new outer object.
# Nested objects are shared.
original = [[1, 2], [3, 4]]
shallow = copy.copy(original)

shallow[0].append(100)

print(original)  # [[1, 2, 100], [3, 4]]
print(shallow)   # [[1, 2, 100], [3, 4]]

# Why? Both original and shallow point to the same inner list.

# 2. Deep Copy (copy.deepcopy())
# Creates a new outer object.
# Copies all nested objects.
original = [[1, 2], [3, 4]]
deep = copy.deepcopy(original)

deep[0].append(100)

print(original)  # [[1, 2], [3, 4]]
print(deep)      # [[1, 2, 100], [3, 4]]

# Why? The inner lists are copied too, so they are independent.

# Memory View

# Shallow Copy

# original --> [ A , B ]
# shallow  --> [ A , B ]   # A and B are shared

# Deep Copy

# original --> [ A , B ]
# deep     --> [ A', B' ]  # Completely new copies
# Summary
# Feature	Shallow Copy	Deep Copy
# New outer object	✅	✅
# New inner objects	❌	✅
# Nested changes affect original?	✅ Yes	❌ No

# Rule to remember:

# Shallow copy: Copies only the first level.
# Deep copy: Copies everything recursively.