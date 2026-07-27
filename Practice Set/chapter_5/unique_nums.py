# 2. Write a program to input eight numbers from the user and display all the unique numbers (once).


num=[]
print("Enter 8 numbers")
for i in range(9):
    n=input("enter a fruit name:")
    num.append(n)

num2=set(num)
print("unique numbers",num2)