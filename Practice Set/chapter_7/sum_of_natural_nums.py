# 5. Write a program to find the sum of first n natural numbers using while loop.
sum=0
num=int(input("enter the number:"))
n=num
while num>0:
    sum=sum+num
    num=num-1

print("sum of",n,"natural numbers is :" ,sum)