# 4. What will be the length of following set s:

s = set()
s.add(20)# int
s.add(20.0)    # float
s.add('20')    # string
 # length of s after these operations
print(len(s))

#output:2

# In Python, 20 == 20.0 is True.
# They also have the same hash value.
# # Since sets store only unique elements, 20.0 is considered the same element as 20.
# Add '20' (string):

# '20' is a string, not a number.
# '20' != 20, so it is a different element.
# Key point: In Python, if two objects compare equal (==) and have the same hash, a set treats them as the same element. 
# That's why 20 and 20.0 occupy only one position in the set, while '20' is stored separately.