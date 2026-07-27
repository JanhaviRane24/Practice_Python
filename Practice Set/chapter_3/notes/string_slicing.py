# String Slicing
# A string in python can be sliced for getting a part of the strings.
# Consider the following string:
# The index in a string starts from 0 to (length -1) in Python. In order to slice a string, we use the following
# syntax:
#s=[name][start:end]
# first index is included(starting index)
# last index is not included(ending index)
# Python Programming Handbook
# Beginner Friendly Learning Guide
# Slicing with Skip Value
# We can provide a skip value as a part of our slice like this:
word = "amazing"
word[1:6:2] # mzn
# Other advanced slicing techniques:
word = "amazing"
word[-7:-1] # amazin
word[:7]    
# amazing
word[0:]    
# amazing