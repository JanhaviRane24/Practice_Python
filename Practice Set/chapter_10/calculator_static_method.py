# 4. Add a static method in problem 2, to greet the user with hello.
# 2. Write a class “Calculator” capable of finding square, cube and square root of a number.
class Calculator:
    def __init__(self,n):
        self.n=n

    def square(self):
        sq=self.n**2
        return sq

    def cube(self):
        cb=self.n**3
        return cb

    def square_root(self):
         sqr=int(self.n**0.5)
         return sqr
    
    @staticmethod
    def greet():
        print("Hello")

c=Calculator(4)
c.greet()
print("square:",c.square())
print("cube:",c.cube())
print("square root:",c.square_root())

    