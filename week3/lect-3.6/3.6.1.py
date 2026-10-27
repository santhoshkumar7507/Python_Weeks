# take a number as input and find the sum of numbers from 1 to that number

n = int(input("Enter the number :")) #50
sum = 0

for i in range(1,n+1):
    sum = sum + i
print(sum)