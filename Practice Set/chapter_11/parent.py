# 1. Simple Inheritance
# Create a Person class with:name,age
# Create a Student class that inherits from Person and adds: roll_no, Print all details.
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age


class Student(Person):
    def __init__(self, name, age, roll_no):
        super().__init__(name, age)
        self.roll_no = roll_no

    def display(self):
        print("Name:", self.name)
        print("Age:", self.age)
        print("Roll No:", self.roll_no)


# Create object
s = Student("Tanu", 20, 101)

# Print details
s.display()


