#  Write a program to open three files 1.txt, 2.txt and 3.txt. If any of these files are not
# present, a message without exiting the program must be printed prompting the same
try:
    f1 = open(r"C:\Users\ranej\OneDrive\Desktop\Practice_Python\Practice Set\chapter_15\1.txt", "r")
    f2 = open(r"C:\Users\ranej\OneDrive\Desktop\Practice_Python\Practice Set\chapter_15\2.txt", "r")
    f3 = open(r"C:\Users\ranej\OneDrive\Desktop\Practice_Python\Practice Set\chapter_15\3.txt", "r")
except FileNotFoundError:
    print("One or more files are not present.")