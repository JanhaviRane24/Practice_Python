class Student:
    def details(self, **kwargs):
        for i, j in kwargs.items():
            print(i, ":", j)

s = Student()
s.details(name="janhavi", age=22, roll_no=12)


# Example with **kwargs – collects keyword arguments into a dictionary:

# Here, kwargs becomes {'Name': 'Alice', 'Age': 25, 'City': 'New York'}.


# Like args, kwargs is just a name that can be changed to whatever you want. Again, what is important here is the use of the unpacking operator (**).

# So, the previous example could be written like this:

# Filename:concatenate_2.py
def concatenate(**words):
    result = ""
    for arg in words.values():
        result += arg
    return result

print(concatenate(a="Real", b="Python", c="Is", d="Great", e="!"))
# Note that in the example above the iterable object is a standard dict. 
# If you iterate over the dictionary and want to return its values, like in the example shown, then you must use .values().

