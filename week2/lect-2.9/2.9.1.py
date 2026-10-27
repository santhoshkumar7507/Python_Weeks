# find whether the given number is even or odd

# number=int(input("Enter the number:"))
# if number % 2 ==0:
#     print("Even")
# else:
#     print("odd")

# number=int(input("ENter the number:"))
# a=number % 10

# if a==0:
#     print(0)
# elif a ==5:
#     print(5)
# else:
#     print("other")

mark=int(input("Enter the mark:"))

if mark<0 or mark >100:
    print("invalid")

elif mark>90:
    print("A")
elif mark >80:
    print("B")
elif mark>70:
    print("C")
elif mark>60:
    print("D")

else:
    print("invalid ")
