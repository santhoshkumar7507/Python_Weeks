# create a python code to sort the list using for loop


l = [9, 3, 7, 1, 6, 3, 4]

for i in range(len(l)):
    for j in range(len(l) - 1 - i):
        if l[j] > l[j + 1]:
            l[j], l[j + 1] = l[j + 1], l[j]

print(l)
