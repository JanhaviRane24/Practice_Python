sentence="my name is janhavi rane"
print("sentence",sentence)
count=0
c=''
for c in sentence:
    if c in "aeiou":
        count=count+1
print("numbers of vowels in sentence is:",count)
