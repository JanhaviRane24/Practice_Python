# 6. Write a program to calculate the factorial of a given number using for loop.
num=int(input("enter the number:"))
fact=1
for i in range(1,num+1):
    fact=fact*i
print("factorial of",num,"is:",fact)