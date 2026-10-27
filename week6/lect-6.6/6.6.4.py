d={0:0,1:1,2:4,3:9,4:16}


# print a list of keys
keys = []

for key in d:
    keys.append(key)

print(keys)
# print a list of values
values = []

for value in d.values():
    values.append(value)

print(values)
# print a list of items
items = []

for item in d.items():
    items.append(item)

print(items)
# what is the datatype of the entries in the items tuple?
for item in d.items():
    print(type(item))