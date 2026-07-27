# 3. Write a program to detect double space in a string.

s=input("enter a string:")
double_space=s.count("  ")
print("count of double space in string:",double_space)


if "  " in s:
    print("Double spaces detected")
else:
    print("No double spaces found")