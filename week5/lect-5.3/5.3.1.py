# create a function obvious_sort() that takes a list as input and returns an ascending ordered list as output

def obvious_sort(a):
    for i in range(len(a)):
        for j in range(i+1, len(a)):
            if a[i] > a[j]:
                a[i], a[j] = a[j], a[i]
    return a
print(obvious_sort([5, 2, 8, 1]))
# [1, 2, 5, 8]