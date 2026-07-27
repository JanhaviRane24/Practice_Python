# 7. Write a program to find out whether a given post is talking about “Harry” or not.

post = '''
Prince Harry, Duke of Sussex, has been in the news for various reasons,
including his recent court defeat and his emotional interview where he
expressed feelings of estrangement from the Royal Family.
He has also been involved in legal battles and has been vocal about his
desire for reconciliation with his royal roots. His recent activities include a visit to his
late mother's grave and discussions about his security status.
'''

if "harry" in post.lower():
    print("Post is talking about Harry.")
else:
    print("Post is not talking about Harry.")