# 2. Write a program to greet all the person names stored in a list ‘lʼ and which starts with S.
l = ["Harry", "Soham", "Sachin", "Rahul","Ashish"]

for i in l:
    s = str(i).lower()
    if s[0] == "s":
        print(i, "greetings")