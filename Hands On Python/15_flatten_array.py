'''
print flat single array for the multiple nested arrays:

l = [1, 2, [5, 4, 5, [6, 54, 543]]]
'''

## Solution 1 - To print every single item flat (even inside nested lists), you can use recursion:

def print_flat(arr):
    for item in arr:
        if isinstance(item, (list, tuple)):  # check both list and tuple
            print_flat(item)
        else:
            print(item)

l = [1, 2, [5, 4, 5, [6, 54, 543]]]
print_flat(l)
t = (1, 2, (5, 4, 5, (6, 54, 543)))
print_flat(t)

## Solution 2 - If you want it all in one line as a single flat list, you can collect items in a list like this:

def flatten(arr):
    flat_list = []
    for item in arr:
        if isinstance(item, (list, tuple)):
            flat_list.extend(flatten(item))
        else:
            flat_list.append(item)
    return tuple(flat_list)

l = [1, 2, [5, 4, 5, [6, 54, 543]]]
print(flatten(l))
t = (1, 2, (5, 4, 5, (6, 54, 543)))
print(flatten(t))
