keys = ['a', 'b', 'c', 'd', 'e']
values = [1, 2, 3, 4, 5]
d = {k: v for k, v in zip(keys, values)}
print(d)