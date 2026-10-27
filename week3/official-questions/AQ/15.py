# Write a code to accept a string as input and determine if it is a palindrome or not.

s = input("Enter the Name :")
rev = ""

for i in s:
    rev = i + rev
print(rev)
print()

if s == rev:
    print("Palindrome")
else:
    print("Not Palindrome")