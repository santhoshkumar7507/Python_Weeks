# Write a program to print the Fibonacci series of n terms where n is always greater than or equal to 2.

n=int(input("Enter the numberr :")) #5
a=0
b=1
print(a)  #0
print(b)  #1

for i in range(2,n): #2 3 4
    c=a+b
    print(c)   #1 #2 #3
    a=b
    b=c
    