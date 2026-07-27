# 3. Check that a tuple type cannot be changed in python.

t=(1,2,3,"kan",45,"ff")
print(t)
t[1]=8
print(t)


#   File "c:\Users\ranej\OneDrive\Desktop\Practice_Python\Practice Set\chapter_4\check_tuple.py", line 5, in <module>
#  t[1]=8
#     ~^^^
# TypeError: 'tuple' object does not support item assignment
