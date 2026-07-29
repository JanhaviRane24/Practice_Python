# 2. Write a class “Calculator” capable of finding square, cube and square root of a number.
class Calculator:

    def square(self,num):
        sq=num**2
        return sq

    def cube(self,num):
        cb=num**3
        return cb

    def square_root(self,num):
         sqr=int(num**0.5)
         return sqr

c=Calculator()
print("square:",c.square(5))
print("cube:",c.cube(2))
print("square root:",c.square_root(16))

    