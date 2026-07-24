"""
POLYMORPHISM IN PYTHON
----------------------

Polymorphism means:
"One interface, many forms"

Different classes can have the same method name,
but each class provides its own implementation.
"""


class Dog:

    def sound(self):
        print("Dog says: Bark")


class Cat:

    def sound(self):
        print("Cat says: Meow")


class Cow:

    def sound(self):
        print("Cow says: Moo")


# Same function works with different objects

def make_sound(animal):

    animal.sound()


dog = Dog()
cat = Cat()
cow = Cow()


make_sound(dog)
make_sound(cat)
make_sound(cow)



# ---------------------------------------------
# Method overriding example
# ---------------------------------------------

class Shape:

    def area(self):
        print("Area calculation")


class Circle(Shape):

    def area(self):
        print("Area of circle = πr²")


class Rectangle(Shape):

    def area(self):
        print("Area of rectangle = length × width")


circle = Circle()
rectangle = Rectangle()


circle.area()
rectangle.area()

"""
Explanation:

Polymorphism allows the same method name to behave differently depending on the object.

Example:

dog.sound()
cat.sound()

Both use:

sound()

but produce different outputs.

Interview Answer:

Different classes can define methods with the same name, but each class implements them differently. Python decides which method to execute based on the object's actual class.
"""