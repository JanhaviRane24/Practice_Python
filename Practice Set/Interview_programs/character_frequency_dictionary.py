sentence="my name is janhavi rane"
print("sentence",sentence)

frequency={}
count=0
for ch in sentence:
    if ch not in frequency:
        frequency[ch] = 1
    else:
        frequency[ch] += 1

print(frequency)

