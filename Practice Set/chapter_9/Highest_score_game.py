# 2. The game() function in a program lets a user play a game and returns the score as an
# integer. You need to read a file ‘Hi-score.txtʼ which is either blank or contains the previous
# Hi-score. You need to write a program to update the Hi-score whenever the game()
# function breaks the Hi-score
def game():
    return 100      # Example score

score = game()

path = "C:/Users/ranej/OneDrive/Desktop/Practice_Python/Practice Set/chapter_9/Hi-score.txt"

with open(path, "r") as f:
    high_score = f.read()

if high_score == "":
    high_score = 0
else:
    high_score = int(high_score)

if score > high_score:
    with open(path, "w") as f:
        f.write(str(score))

    print("Hi-score updated!")
else:
    print("Hi-score not broken")