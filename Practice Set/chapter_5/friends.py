# 6. Create an empty dictionary. Allow 4 friends to enter their favorite language as value and use key as their names. Assume that the names are unique.

# Create an empty dictionary
friends = {}

# Take input from 4 friends
for i in range(4):
    name = input("Enter your name: ")
    language = input("Enter your favorite language: ")
    friends[name] = language

# Display the dictionary
print("\nFavorite Languages:")
print(friends)


#7. If the names of 2 friends are same; what will happen to the program in problem 6?

# If the names of 2 friends are the same, the program will not give an error. 
# Instead, the second friend's favorite language will replace the first friend's favorite language because dictionary keys must be unique.

# output:
# Enter your name: tanvi
# Enter your favorite language: marathi
# Enter your name: sanika
# Enter your favorite language: punjabi
# Enter your name: tanvi
# Enter your favorite language: urdu
# Enter your name: rini
# Enter your favorite language: latin

# Favorite Languages:
# {'tanvi': 'urdu', 'sanika': 'punjabi', 'rini': 'latin'}

# 8. If languages of two friends are same; what will happen to the program in problem 6?

# Answer: Nothing unusual will happen. The program will work normally.

# In a dictionary:

# Keys (friend names) must be unique.
# Values (favorite languages) can be the same.

# output:
# Enter your name: tanu
# Enter your favorite language: urdu
# Enter your name: janu
# Enter your favorite language: urdu
# Enter your name: saru
# Enter your favorite language: hindi
# Enter your name: piyu
# Enter your favorite language: marathi

# Favorite Languages:
# {'tanu': 'urdu', 'janu': 'urdu', 'saru': 'hindi', 'piyu': 'marathi'}