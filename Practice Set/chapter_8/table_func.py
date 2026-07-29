# 8. Write a python function to print multiplication table of a given number.

n=int(input("enter a number:"))
def table(num):
    print("Table of",num)
    for i in range(1,11):
        print(num,"x",i,"=",num*i)

table(n)