# 10. Write a program to print multiplication table of n using for loops in reversed order.
num=int(input("enter a number:"))

for i in range(10,0,-1):
    print(num,"x",i,"=",num*i)