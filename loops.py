# loops.py

print("For Loop")
for i in range(1, 6):
    print(i)

print("\nWhile Loop")
count = 1
while count <= 5:
    print(count)
    count += 1

print("\nEven Numbers")
for i in range(2, 11, 2):
    print(i)

print("\nBreak Example")
for i in range(1, 10):
    if i == 5:
        break
    print(i)

print("\nContinue Example")
for i in range(1, 6):
    if i == 3:
        continue
    print(i)
