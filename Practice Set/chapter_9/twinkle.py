# 1. Write a program to read the text from a given file ‘poems.txtʼ and find out whether it
# contains the word ‘twinkleʼ.

# import os

# print(os.getcwd())
# # print(os.listdir())
# import os

# print(os.listdir("Practice Set"))

with open("C:/Users/ranej/OneDrive/Desktop/Practice_Python/Practice Set/chapter_9/poems.txt","r") as f:
    content=f.read().lower()
    if "twinkle" in content:
        print("Twinkle is present in poems")
    else:
        print("Twinkle is not present in poems")

