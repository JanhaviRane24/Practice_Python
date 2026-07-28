# 6. Write a python function which converts inches to cms.
i=float(input("enter length in inches:"))

def centimeter(inch):
    cm=inch*2.54
    return cm

print("Length in centimeter is :",centimeter(i))