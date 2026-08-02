def number():
    yield 1
    yield 2
    yield 3

for n in number():
    print(n)
