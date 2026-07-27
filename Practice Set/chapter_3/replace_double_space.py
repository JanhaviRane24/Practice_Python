# 4. Replace the double space from problem 3 with single spaces.
s=input("enter a string:")
if "  " in s:
    print(s.replace("  "," "))
else:
    print("no double space found")
    print(s)