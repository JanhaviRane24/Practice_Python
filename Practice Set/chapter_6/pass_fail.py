# 2. Write a program to find out whether a student has passed 
# or failed if it requires a total of
# 40% and at least 33% in each subject to pass. Assume 3 subjects and take marks as an
# input from the user.
print("enter subject marks out of 100")
sub1=int(input("enter 1 subject marks:"))
sub2=int(input("enter 2 subject marks:"))
sub3=int(input("enter 3 subject marks:"))

total=(sub1+sub2+sub3)
percentage=(total/300)*100


if percentage>=40 and sub1>=33 and sub2>=33 and sub3>=33:
    print("student has passed")
else:
    print("student has failed")