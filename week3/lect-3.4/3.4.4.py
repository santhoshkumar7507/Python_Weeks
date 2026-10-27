num=int(input()) #123
n=num
reverse=0

while num>0: #123 #12 1
    digits=num%10 #3 /2  /1
    reverse=reverse*10+digits #3 /32 /321
    num=num//10# 12  / 1
    
print(reverse)

if n == reverse:
    print("palindrome")
else:
    print("not a palindrome")

s="hello world"
print(s[::-1])
