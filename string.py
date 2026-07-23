# string.py

text = "Python Programming"

print("Original:", text)
print("Uppercase:", text.upper())
print("Lowercase:", text.lower())
print("Title:", text.title())
print("Length:", len(text))
print("Replace:", text.replace("Python", "Java"))
print("Split:", text.split())
print("First Character:", text[0])

name = "Rahul"
age = 21

print(f"My name is {name} and I am {age} years old.")


# strings_methods.py

# String creation

text = "  Python Programming  "

print("Original String:", text)


# Indexing

print("\nIndexing:")
print("First Character:", text[0])
print("Last Character:", text[-1])


# String slicing string[start:stop:step]

word = "Python"

print("\nSlicing:")
print("Original:", word)
print("From index 0 to 3:", word[0:4])
print("Reverse String:", word[::-1])
print("Every second character:", word[::2])


# String Methods

print("\nString Methods:")

name = "python programming"

print("Upper:", name.upper())
print("Lower:", name.lower())

print("Strip:", text.strip())

print("Split:", name.split())

words = ["Python", "is", "easy"]
print("Join:", " ".join(words))

print("Find:", name.find("programming"))

print("Replace:", name.replace("Python", "Java"))

print("Starts With:", name.startswith("python"))

print("Ends With:", name.endswith("ming"))

print("Count:", name.count("p"))


# Reverse a string

print("\nReverse String:")

s = "hello"

print(s[::-1])


# Check palindrome

print("\nPalindrome Check:")

def is_palindrome(s):
    return s == s[::-1]


print(is_palindrome("madam"))
print(is_palindrome("hello"))


# Count vowels

print("\nCount Vowels:")

def count_vowels(s):
    return sum(1 for ch in s.lower() if ch in "aeiou")


print(count_vowels("Python Programming"))


# Count words

print("\nCount Words:")

def count_words(s):
    return len(s.split())


sentence = "Python is a powerful programming language"

print(count_words(sentence))


# Difference between find() and index()

print("\nFind vs Index:")

sample = "Python"

print("find:", sample.find("z"))

# print(sample.index("z")) 
# This will raise ValueError


# String immutability example

print("\nString Immutability:")

original = "Hello"

new_string = original.replace("Hello", "Hi")

print("Original:", original)
print("New String:", new_string)
