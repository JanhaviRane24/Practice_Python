x = "awesome"

def myfunc():
  print("Python is " + x)

myfunc()


#Normally, when you create a variable inside a function, 
# that variable is local, and can only be used inside that function.

#To create a global variable inside a function, you can use the global keyword.
#Also, use the global keyword if you want to change a global variable inside a function.


def myfunc():
  global x
  x = "fantastic"

myfunc()

print("Python is " + x)

#To change the value of a global variable inside a function, 
# refer to the variable by using the global keyword:


x = "awesome"

def myfunc():
  global x
  x = "fantastic"

myfunc()

print("Python is " + x)
