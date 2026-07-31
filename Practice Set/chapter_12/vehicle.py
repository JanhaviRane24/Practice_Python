class Vehicle:
    def start(self):
        print("vehicle start")

class Car(Vehicle):
    def start(self):
        print("Start with self start button")

class Bike(Vehicle):
    def start(self):
        print("start with key")

v=[Vehicle(),Car(),Bike()]

for i in v:
    i.start()