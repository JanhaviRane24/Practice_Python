class Employee:
    def __init__(self):
        self.sal = 50000

    @property
    def salary(self):
        return self.sal
    @salary.setter
    def salary(self,value):
        self.sal=value

e = Employee()
print(e.salary)
e.salary = 45000
print(e.salary)