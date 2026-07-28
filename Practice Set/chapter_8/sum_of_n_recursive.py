# 4. Write a recursive function to calculate the sum of first n natural numbers.


def sum_n(n):
    if n==1:
        return 1
    return n + sum_n(n-1)

n=int(input("enter the number:"))


print("sum of",n,"natural numbers is :" ,sum_n(n))
