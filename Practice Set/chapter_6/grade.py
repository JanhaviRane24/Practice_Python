# # 6. Write a program to calculate the grade of a student from his marks from the following scheme
# 90 – 100 => Excellent
# 80 – 90 => A
# 70 – 80 => B
# 60 – 70 => C
# 50 – 60 => D
# <50 => F

marks = int(input("Enter your marks: "))

if marks < 0 or marks > 100:
    print("Invalid marks")
elif marks >= 90:
    print("Excellent grade")
elif marks >= 80:
    print("A grade")
elif marks >= 70:
    print("B grade")
elif marks >= 60:
    print("C grade")
elif marks >= 50:
    print("D grade")
else:
    print("F grade")