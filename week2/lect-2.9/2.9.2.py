num = int(input("Enter a number: "))

last_digit = abs(num) % 10

if last_digit == 0:
    print("0")
elif last_digit == 5:
    print("5")
else:
    print("Other")