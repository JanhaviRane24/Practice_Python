# file_handling.py

import os


# Creating and writing to a file

print("Write Mode:")

file = open("demo.txt", "w")

file.write("Hello Python\n")
file.write("Learning File Handling")

file.close()

print("File written successfully")



# Reading a file

print("\nRead Mode:")

file = open("demo.txt", "r")

content = file.read()

print(content)

file.close()



# readline() - reads one line

print("\nRead Line:")

file = open("demo.txt", "r")

line = file.readline()

print(line)

file.close()



# Reading using with statement

print("\nUsing with open:")

with open("demo.txt", "r") as file:
    print(file.read())



# Append mode

print("\nAppend Mode:")

with open("demo.txt", "a") as file:
    file.write("\nNew line added using append mode")


with open("demo.txt", "r") as file:
    print(file.read())



# Write mode overwrites existing content

print("\nOverwrite Example:")

with open("demo.txt", "w") as file:
    file.write("New content overwrites old content")


with open("demo.txt", "r") as file:
    print(file.read())



# r+ mode - read and write

print("\nr+ Mode:")

with open("demo.txt", "r+") as file:
    print(file.read())
    file.write("\nAdded using r+ mode")



# w+ mode - write and read

print("\nw+ Mode:")

with open("new_file.txt", "w+") as file:
    file.write("Hello from w+ mode")
    file.seek(0)
    print(file.read())



# Delete file using os module

print("\nDelete File:")

if os.path.exists("new_file.txt"):
    os.remove("new_file.txt")
    print("File deleted")

else:
    print("File does not exist")


#Why use with open()?

#Manual approach:

file = open("demo.txt", "r")
data = file.read()
file.close()

#Problem: if an error happens before close(), the file may remain open.

#Better approach:

with open("demo.txt", "r") as file:
    data = file.read()

#The with statement automatically closes the file after the block finishes, 
# even if an exception occurs.


