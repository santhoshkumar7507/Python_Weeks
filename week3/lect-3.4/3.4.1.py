n = int(input("Enter the number :"))

if n<0:
    print("Not Defined")
elif n == 0:
    print(1)
else:
    fact =1
    number = 1

    while number <=n:
        fact = fact * number 
        number = number +1
    print(fact)