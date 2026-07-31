class Addition:
    def sum_of(self,*args):
        return sum(args)

a=Addition()
print(a.sum_of(1,2,3,4,5))


# Note that args is just a name. You’re not required to use the name args. You can choose any name that you prefer, such as integers:

# Filename:sum_integers_args_2.py

def my_sum(*integers):
    result = 0
    for x in integers:
        result += x
    return result

print(my_sum(1, 2, 3))

# The function still works, even if you pass the iterable object as integers instead of args. All that matters here is that you use the unpacking operator (*).

# Bear in mind that the iterable object you’ll get using the unpacking operator * is not a list but a tuple. 
# A tuple is similar to a list in that they both support slicing and iteration. 
# However, tuples are very different in at least one aspect: lists are mutable, while tuples are not. 


# # In Python, *args and **kwargs allow functions to accept a variable number of arguments, making them highly flexible for dynamic inputs.

# # *args is used to capture positional arguments as a tuple, while **kwargs captures keyword arguments as a dictionary.

# # Example with *args – collects positional arguments into a tuple:

# Here, args becomes (2, 3, 4) and is iterated for multiplication.

# Using both together – order matters: Regular parameters → *args → **kwargs.

# Unpacking with * and ** – expands iterables/dicts into arguments:

# This is useful for passing dynamic data structures directly into functions.

# Key Points:

# *args → tuple of extra positional arguments.

# **kwargs → dict of extra keyword arguments.

# Can be combined in one function, but *args must come before **kwargs.

# * and ** also work in function calls for unpacking iterables and dictionaries.

# These tools are essential for writing flexible, reusable, and clean Python functions.

