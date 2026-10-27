## write a python code to print the minimum element of the list, using for loop


l = [1,44,22,11,23,36,49,28,31,8,54,54]

minimum = l[0]

for i in l:
    if i < minimum:
        minimum = i

print("Minimum element:", minimum)



