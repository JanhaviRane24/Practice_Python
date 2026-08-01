# 3. Write a list comprehension to print a list which contains the multiplication table of a user
# entered number
n=int(input("enter a number:"))
table=[n*i for i in range(1,11)]
print(table)


# 5. Store the multiplication tables generated in problem 3 in a file named Tables.txt 

with open(r"C:\Users\ranej\OneDrive\Desktop\Practice_Python\Practice Set\chapter_15\Tables.txt", "w") as f:
    f.write(str(table))