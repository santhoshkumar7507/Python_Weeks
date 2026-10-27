import random

l = []

# Create 30 random numbers
for i in range(30):
    l.append(random.randint(1, 365))

l.sort()

print("📅 Generated Numbers:")
print(l)

flag = 0

# Check for repetition
for i in range(len(l) - 1):
    if l[i] == l[i + 1]:
        print(f"\n⚠️ Repeated Number Found: {l[i]}")
        flag = 1
        break

if flag == 0:
    print("\n✅ There is no repetition.")