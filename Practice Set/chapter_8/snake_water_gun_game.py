# Project 1 : Snake Water Gun Game
# We all have played snake, water gun game in our childhood. If you havenʼt,
# google the rules of this game and write a python program capable of playing
# this game with the userimport random
import random

choices = ["snake", "water", "gun"]

computer = random.choice(choices)
player = input("Enter your choice (snake/water/gun): ").lower()

print("Computer chose:", computer)

if player not in choices:
    print("Invalid choice")
elif player == computer:
    print("Draw")
elif (player == "snake" and computer == "water") or \
     (player == "water" and computer == "gun") or \
     (player == "gun" and computer == "snake"):
    print("You win!")
else:
    print("Computer wins!")










"""
The rules are: Snake drinks Water (Snake wins), Water drowns Gun (Water wins), and Gun kills Snake (Gun wins). Same choices result in a draw.
Detailed Rules
Based on multiple authoritative sources, the Snake_Water_Gun game follows these outcomes:

✅ Winning Conditions
Snake vs Water → Snake wins (Snake drinks Water) 
Water vs Gun → Water wins (Water douses/drowns Gun) 
+1
Gun vs Snake → Gun wins (Gun shoots Snake) 
+1
✅ Draw Condition
Same choice by both players → Draw 
Summary Table
Player 1	Player 2	Winner	Reason
Snake	Water	Snake	Drinks water
Water	Gun	Water	Douses gun
Gun	Snake	Gun	Shoots snake
Same	Same	Draw	Identical choices
#These rules form the complete logic of the Snake_Water_Gun game, a variation of Rock_Paper_Scissors.

"""