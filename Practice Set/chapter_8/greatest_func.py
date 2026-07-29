# 1. Write a program using functions to find greatest of three numbers.

def greatest(num1,num2,num3):
    if num1>=num2 and num1>=num3:
        print(num1,"is the greatest")
    elif num2>=num1 and num2>=num3:
        print(num2,"is the greatest")
    else:
        print(num3,"is the greatest")



n1=int(input("enter 1 number:"))
n2=int(input("enter 2 number:"))
n3=int(input("enter 3 number:"))

greatest(n1,n2,n3)