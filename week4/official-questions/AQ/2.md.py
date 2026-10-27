# Find smallest n such that a number with n repeated 7's is divisible by 2003

mod = 2003
remainder = 0

for n in range(1, 2003):   # upper bound is enough since 2003 is prime
    remainder = (remainder * 10 + 7) % mod
    if remainder == 0:
        print("Number of digits:", n)
        break

# number = 7*10n-1/9

# 777777777777777777777777777...