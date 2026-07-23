# tuple.py

colors = ("Red", "Green", "Blue", "Yellow")

print("Tuple:", colors)
print("First Color:", colors[0])
print("Last Color:", colors[-1])
print("Length:", len(colors))

for color in colors:
    print(color)

print("Index of Green:", colors.index("Green"))
print("Count of Red:", colors.count("Red"))
