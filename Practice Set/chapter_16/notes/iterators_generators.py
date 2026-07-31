"""
ITERATORS AND GENERATORS
------------------------

Iterator:
Object that implements:
__iter__()
__next__()

Generator:
A simpler way to create iterators using yield.
"""


# --------------------------------
# Iterator Example
# --------------------------------


numbers = [10,20,30]


iterator = iter(numbers)


print(next(iterator))
print(next(iterator))
print(next(iterator))



# --------------------------------
# Custom Iterator
# --------------------------------


class Count:

    def __init__(self,max):

        self.max = max
        self.current = 1


    def __iter__(self):

        return self


    def __next__(self):

        if self.current <= self.max:

            value = self.current
            self.current += 1

            return value

        else:

            raise StopIteration



counter = Count(5)


for num in counter:

    print(num)



# --------------------------------
# Generator Example
# --------------------------------


def count_up_to(n):

    i = 1

    while i <= n:

        yield i

        i += 1



for value in count_up_to(5):

    print(value)

"""
Explanation
Iterator

An iterator remembers its current position.

Uses:

iter()
next()
Generator

Generator uses:

yield

Instead of storing all values:

[1,2,3,4,5]

it produces:

1
then
2
then
3

one at a time.

yield vs return
return	yield
Ends function	Pauses function
Gives one final value	Produces multiple values
Memory intensive	Memory efficient
"""