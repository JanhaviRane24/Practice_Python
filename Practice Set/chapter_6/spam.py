# A spam comment is defined as a text containing following keywords: “Make a lot of
# money”, “buy now”, “subscribe this”, “click this”. Write a program to detect these spams

comment=input("enter any comments:").lower()

spam_content=["Make a lot of money", "buy now", "subscribe this", "click this"]

if spam_content[0] in comment or spam_content[1] in comment or spam_content[2] in comment or spam_content[3] in comment  :
    print("its a spam comment")
else:
    print("its not a spam comment")