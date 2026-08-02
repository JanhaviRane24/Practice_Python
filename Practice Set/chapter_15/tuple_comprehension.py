tuple1=(1,2,3,4,5)
tuple2=tuple(i**2 for i in tuple1)
print(tuple2)

# Tuple comprehensions are not directly supported, Python's existing features like generator expressions 
# and the tuple() function provide flexible alternatives for creating tuples from iterable data.

# (i for i in (1, 2, 3))

# Explanation:

# In Python, expressions enclosed in parentheses with a for loop produce a generator expression, 
# which generates values lazily one at a time.
# Since tuples are immutable sequences, Python does not provide a separate tuple comprehension syntax. 
# Instead, the recommended approach is to use a generator expression and convert it into a tuple using tuple().
