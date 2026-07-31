# Unpacking With the Asterisk Operators: * & **
# You are now able to use *args and **kwargs to define Python functions that take a varying number of input arguments. Let’s go a little deeper to understand something more about the unpacking operators.

# The single and double asterisk unpacking operators were introduced in Python 2. As of the 3.5 release, they have become even more powerful, thanks to PEP 448. In short, the unpacking operators are operators that unpack the values from iterable objects in Python. The single asterisk operator * can be used on any iterable that Python provides, while the double asterisk operator ** can only be used on dictionaries.

# Let’s start with an example:

# Filename:print_list.py
# my_list = [1, 2, 3]
# print(my_list)
# This code defines a list and then prints it to the standard output:

# $ python print_list.py
# [1, 2, 3]
# Note how the list is printed, along with the corresponding brackets and commas.

# Now, try to prepend the unpacking operator * to the name of your list:

# Filename:print_unpacked_list.py
# my_list = [1, 2, 3]
# print(*my_list)
# Here, the * operator tells print() to unpack the list first.

# In this case, the output is no longer the list itself, but rather the content of the list:

# $ python print_unpacked_list.py
# 1 2 3
# Can you see the difference between this execution and the one from print_list.py? Instead of a list, print() has taken three separate arguments as the input.

# Another thing you’ll notice is that in print_unpacked_list.py, you used the unpacking operator * to call a function, instead of in a function definition. In this case, print() takes all the items of a list as though they were single arguments.

# You can also use this method to call your own functions, but if your function requires a specific number of arguments, then the iterable you unpack must have the same number of arguments.

# To test this behavior, consider this script:

# Filename:unpacking_call.py
# def my_sum(a, b, c):
#     print(a + b + c)

# my_list = [1, 2, 3]
# my_sum(*my_list)
# Here, my_sum() explicitly states that a, b, and c are required arguments.

# If you run this script, you’ll get the sum of the three numbers in my_list:

# $ python unpacking_call.py
# 6
# The 3 elements in my_list match up perfectly with the required arguments in my_sum().

# Now look at the following script, where my_list has 4 arguments instead of 3:

# Filename:wrong_unpacking_call.py
# def my_sum(a, b, c):
#     print(a + b + c)

# my_list = [1, 2, 3, 4]
# my_sum(*my_list)
# In this example, my_sum() still expects just three arguments, but the * operator gets 4 items from the list. If you try to execute this script, you’ll see that the Python interpreter is unable to run it:

# $ python wrong_unpacking_call.py
# Traceback (most recent call last):
#   File "wrong_unpacking_call.py", line 6, in <module>
#     my_sum(*my_list)
# TypeError: my_sum() takes 3 positional arguments but 4 were given
# When you use the * operator to unpack a list and pass arguments to a function, it’s exactly as though you’re passing every single argument alone. This means that you can use multiple unpacking operators to get values from several lists and pass them all to a single function.

# To test this behavior, consider the following example:

# Filename:sum_integers_args_3.py
# def my_sum(*args):
#     result = 0
#     for x in args:
#         result += x
#     return result

# list1 = [1, 2, 3]
# list2 = [4, 5]
# list3 = [6, 7, 8, 9]

# print(my_sum(*list1, *list2, *list3))
# If you run this example, all three lists are unpacked. Each individual item is passed to my_sum(), resulting in the following output:

# $ python sum_integers_args_3.py
# 45
# There are other convenient uses of the unpacking operator. For example, say you need to split a list into three different parts. The output should show the first value, the last value, and all the values in between. With the unpacking operator, you can do this in just one line of code:

# Filename:extract_list_body.py
# my_list = [1, 2, 3, 4, 5, 6]

# a, *b, c = my_list

# print(a)
# print(b)
# print(c)
# In this example, my_list contains 6 items. The first variable is assigned to a, the last to c, and all other values are packed into a new list b. If you run the script, print() will show you that your three variables have the values you would expect:

# $ python extract_list_body.py
# 1
# [2, 3, 4, 5]
# 6
# Another interesting thing you can do with the unpacking operator * is to split the items of any iterable object. This could be very useful if you need to merge two lists, for instance:

# Filename:merging_lists.py
# my_first_list = [1, 2, 3]
# my_second_list = [4, 5, 6]
# my_merged_list = [*my_first_list, *my_second_list]

# print(my_merged_list)
# The unpacking operator * is prepended to both my_first_list and my_second_list.

# If you run this script, you’ll see that the result is a merged list:

# $ python merging_lists.py
# [1, 2, 3, 4, 5, 6]
# You can even merge two different dictionaries by using the unpacking operator **:

# Filename:merging_dicts.py
# my_first_dict = {"A": 1, "B": 2}
# my_second_dict = {"C": 3, "D": 4}
# my_merged_dict = {**my_first_dict, **my_second_dict}

# print(my_merged_dict)
# Here, the iterables to merge are my_first_dict and my_second_dict.

# Executing this code outputs a merged dictionary:

# $ python merging_dicts.py
# {'A': 1, 'B': 2, 'C': 3, 'D': 4}
# Remember that the * operator works on any iterable object. It can also be used to unpack a string:

# Filename:string_to_list.py
# a = [*"RealPython"]
# print(a)
# In Python, strings are iterable objects, so * will unpack it and place all individual values in a list a:

# $ python string_to_list.py
# ['R', 'e', 'a', 'l', 'P', 'y', 't', 'h', 'o', 'n']
# The previous example seems great, but when you work with these operators it’s important to keep in mind the seventh rule of The Zen of Python by Tim Peters: Readability counts.

# To see why, consider the following example:

# Filename:mysterious_statement.py
# *a, = "RealPython"
# print(a)
# There’s the unpacking operator *, followed by a variable, a comma, and an assignment. That’s a lot packed into one line! In fact, this code is no different from the previous example. It just takes the string RealPython and assigns all the items to the new list a, thanks to the unpacking operator *.

# The comma after the a does the trick. When you use the unpacking operator with variable assignment, Python requires that your resulting variable is either a list or a tuple. With the trailing comma, you have defined a tuple with only one named variable, a, which is the list ['R', 'e', 'a', 'l', 'P', 'y', 't', 'h', 'o', 'n'].


# While this is a neat trick, many Pythonistas would not consider this code to be very readable. As such, it’s best to use these kinds of constructions sparingly.


# Remove ads
# Conclusion
# You are now able to use *args and **kwargs to accept a changeable number of arguments in your functions. You have also learned something more about the unpacking operators.

# You’ve learned:

# What *args and **kwargs actually mean
# How to use *args and **kwargs in function definitions
# How to use a single asterisk (*) to unpack iterables
# How to use two asterisks (**) to unpack dictionaries
