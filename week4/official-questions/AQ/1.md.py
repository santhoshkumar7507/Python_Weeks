# class should have numbers which are not perfect squares. Do you observe any pattern?

x = int(input("Enter the number :"))
count = 0
for i in range(1,x+1):
    if i%x==0:
        count += 1
print(count)

if (x**0.5) * (x**0.5) == x:
    print("Perfect")
else:
    print("Not")


# | Number | Multiply | Perfect Square? |
# | -----: | :------: | :-------------: |
# |      1 |   1 × 1  |      ✅ Yes      |
# |      4 |   2 × 2  |      ✅ Yes      |
# |      9 |   3 × 3  |      ✅ Yes      |
# |     16 |   4 × 4  |      ✅ Yes      |
# |     25 |   5 × 5  |      ✅ Yes      |
# |     36 |   6 × 6  |      ✅ Yes      |


