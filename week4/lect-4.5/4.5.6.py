# create a python code to sort the list using while loop

l = [5, 2, 8, 1, 3]
i = 0
while i < len(l):
    j = i + 1
    while j < len(l):
        if l[i] > l[j]:
            l[i], l[j] = l[j], l[i]
        j += 1
    i += 1
print(l)




# l = [5, 2, 8, 1, 3]

# i = 0
# while i < len(l):
#     l[i], l[l.index(min(l[i:]))] = min(l[i:]), l[i]
#     i += 1

# print(l)
