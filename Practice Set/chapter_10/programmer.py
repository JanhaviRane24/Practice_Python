# 1. Create a class “Programmer” for storing information of few programmers working at
# Microsoft.

class Programmer:
    company="Microsoft"
    def __init__(self,id,name,department,salary):
        self.id=id
        self.name=name
        self.department=department
        self.salary=salary

    def details(self):
        print("Employee Id",self.id)
        print("Employee Name",self.name)
        print("Employee Company",self.company)
        print("Employee Department",self.department)
        print("Employee Salary",self.salary)


p=Programmer(1,"Sanika","Development","650000")
p.details()

p2=Programmer(2,"Manuja","IT","450000")
p2.details()


p3=Programmer(3,"Tara","Testing","730000")
p3.details()


p4=Programmer(4,"Robin","Dev OPS","780000")
p4.details()