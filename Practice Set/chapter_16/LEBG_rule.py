
# Python follows the LEGB rule to resolve variable names. LEGB stands for:

# L – Local
# E – Enclosing
# G – Global
# B – Built-in
# Python searches for a variable in this order until it is found.

x = "Global"

def outer_func():
    x = "Enclosing"

    def inner_func():
        x = "Local"
        print(x)

    inner_func()

outer_func()