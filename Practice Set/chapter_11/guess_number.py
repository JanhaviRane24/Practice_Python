# Project 2 : The Perfect Guess

#  We are going to write a program that generates a random number and asks the user to
# guess it.
# If the playerʼs guess is higher than the actual number, the program displays “Lower
# number please” .
# Similarly, if the userʼs guess is too low, the program prints “Higher number please” .
# When the user guesses the correct number, the program displays the number of
# guesses the player used to arrive at the number.
# HINT
# import random


import random

computer=random.randint(1,10)

for i in range(10):
    user=int(input("Guess a number between(1,10):"))
    if user>computer:
        print("Lower number please")
    elif user<computer:
        print("higher number please")
    elif user==computer:
        print("guess is correct")
        print("no of attempts",i+1)
        break
else:
    print("Sorry! You have used all 10 attempts.")
    print("The correct number was:", computer)