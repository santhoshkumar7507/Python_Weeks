# predict the output

# l=[2,6,1,50,3,7,5]
# l.reverse()
# print(l)

n = int(input("Enter the number :"))
num = n 
rev = 0

while n > 0:
    digit = n % 10 #123   3  2 1 0
    rev = rev * 10 + digit #321   
    n = n // 10 #12 #1 1
print(rev)

if rev == num:
    print("Palindrome")
else:
    print("Not Palindrome")
