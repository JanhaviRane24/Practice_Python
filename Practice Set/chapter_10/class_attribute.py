# 3. Create a class with a class attribute a; create an object from it and set ‘aʼ directly using
# ‘object.a = 0ʼ. Does this change the class attribute

class Test:
    a=34


t=Test()
print(t.a)# Prints the class attribute because instance attribute is not present
#34
t.a=0  #Instance attribute is set
print(t.a) # Prints the instance attribute because instance attribute is present
#0
print(Test.a) # Prints the class attribute
#34

# Explanation
# a = 34 is a class attribute, shared by all objects of the class.
# Before t.a = 0, the object t does not have its own a, so t.a refers to Test.a.
# After t.a = 0, the object t gets its own instance attribute a, which hides the class attribute for that object only.
# The class attribute Test.a remains unchanged.

# Answer to the question:
# No, setting object.a = 0 does not change the class attribute. It creates an instance attribute, while the class attribute remains the same.