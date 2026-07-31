"""
DECORATORS IN PYTHON
--------------------

A decorator modifies the behavior of another function
without changing its original code.
"""


def my_decorator(func):


    def wrapper():

        print("Before function")


        func()


        print("After function")


    return wrapper



@my_decorator
def say_hello():

    print("Hello")



say_hello()



# -----------------------------------
# Decorator with arguments
# -----------------------------------


def login_required(func):


    def wrapper(user):

        if user == "admin":

            func(user)

        else:

            print("Access denied")


    return wrapper



@login_required
def dashboard(user):

    print("Welcome", user)



dashboard("admin")

dashboard("guest")


"""
Explanation

Decorator flow:

Before:

say_hello()

After:

my_decorator(say_hello)

@decorator is just cleaner syntax.

Real examples:

Django REST Framework:

@api_view(["GET"])
@permission_classes([IsAuthenticated])

These decorators add behavior to views.

"""