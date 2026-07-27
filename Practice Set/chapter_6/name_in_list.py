# 5. Write a program which finds out whether a given name is present in a list or not.

name=input("enter your name:").lower()
names=["sunita","geeta","rahul","tanmay","ridhi"]
if name in names:
    print("Your name is present in list")
else:
    print("Your name is not present in list")