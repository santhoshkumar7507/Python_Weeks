'''
create three functions that take a list as input 
1) to return the first element of the list
2) to return the last element of the list
3) to return the sum of values returned from the above two functions 
'''
# 1. Return the first element
def first_element(numbers):
    return numbers[0]


# 2. Return the last element
def last_element(numbers):
    return numbers[-1]


# 3. Add the first and last elements
def sum_first_last(numbers):
    return first_element(numbers) + last_element(numbers)


# Test
numbers = [10, 20, 30, 40, 50]

print(first_element(numbers))     # 10
print(last_element(numbers))      # 50
print(sum_first_last(numbers))    # 60