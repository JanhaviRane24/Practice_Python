
#4. Write a python program to print the contents of a directory using the os module. 
#Search online for the function which does that.


# 5. Label the program written in problem 4 with comments.
import os

contents = os.listdir()
# print(contents)

#we use listdir() fuction to give contents of directory

for content in contents:
    print(content)