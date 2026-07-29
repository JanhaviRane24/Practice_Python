num=12345
n=num
rev=0
while n>0:
    rev=(rev*10)+(n%10)
    n=n//10
print("original number:",num)
print("Reverse number:",rev)

if num==rev:
    print("palindrome")
else:
    print("not a palindrome")


s="mom"
if s==s[::-1]:
    print("palindrome")
else:
    print("not a palindrome")