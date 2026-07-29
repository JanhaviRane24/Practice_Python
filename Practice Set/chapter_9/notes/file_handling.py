# file_handling.py

# File I/O
# The random-access memory is volatile, and all its contents are lost once a program terminates. In order to
# persist the data forever, we use files.
# A file is data stored in a storage device. A python program can talk to the file by reading content from it and
# writing content to it.

# Type Of Files.
# There are 2 types of files:
# 1. Text files (.txt, .c, etc)
# 2. Binary files (.jpg, .dat, etc)
# Python has a lot of functions for reading, updating, and deleting files.

# Opening A File
# Python has an open() function for opening files. It takes 2 parameters: filename and mode.
# open("filename", "mode of opening(read mode by default)")
open("this.txt", "r")

# Open the file in read mode
f = open("this.txt", "r")
# Read its contents
text = f.read()
# Print its contents
print(text)
# Close the file
f.close()

# Other Methods To Read The File.
# We can also use f.readline() function to read one full line at a time.
# f.readline() # Read one line from the file.

# Modes Of Opening A File
# r – open for reading
# w - open for writing
# a - open for appending
# + - open for updating.
# ‘rbʼ will open for read in binary mode.
# ‘rtʼ will open for read in text mode.

# Write Files In Python

# In order to write to a file, we first open it in write or append mode after which, we use the pythonʼs f.write()
# method to write to the file!
# Open the file in write mode
f = open("this.txt", "w")
# Write a string to the file
f.write("this is nice")
# Close the file
f.close()

# With Statement
# The best way to open and close the file automatically is the with statement
# Open the file in read mode using 'with'
with open("this.txt", "r") as f:
# Read the contents of the file
    text = f.read()
# Print the content
print(text)


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


