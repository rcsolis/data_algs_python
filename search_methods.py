# BINARY SEARCH
# Custom/Manual implementation
# Iterative implementation
def loop_binary_search(data, items):
    first = 0
    last = len(items) - 1
    while first <= last:
        middle = first + (last-first) // 2
        if items[middle] == data:
            return True
        elif items[middle] > data:
            last = middle - 1
        else:
            first = middle + 1
    return False
# Recursive implementation
def recursive_binary_search(data, items, first, last):    
    if first > last:
        return False
    else:
        middle = first + (last-first) // 2
        if items[middle] == data:
            return True
        elif items[middle] > data:
            return recursive_binary_search(data, items, first, middle-1)
        else:
            return recursive_binary_search(data, items, middle+1, last)
    
# main method of binary search
def binary_search(data, items, type="iterative"):
    array = sorted(items)
    if len(array) == 0:
        return False
    elif len(array) == 1:
        return True if array[0] == data else False
    else:
        if type == "iterative":
            return loop_binary_search(data, array)
        else:
            return recursive_binary_search(data, array, 0, len(array)-1)
    
# TEST BINARY SEARCH
sequence = [100,130,213,12,234,25,12,43]
print(f"Searching (iterative) for 25: {True if binary_search(25, sequence) else False}")
print(f"Searching (iterative) for 50: {True if binary_search(50, sequence) else False}")
print(f"Searching (recursive) for 25: {True if binary_search(25, sequence, type='recursive') else False}")
print(f"Searching (recursive) for 50: {True if binary_search(50, sequence, type='recursive') else False}")

# Using bisect module
import bisect

def bisect_binary_search(data, items):
    array = sorted(items)
    # find the index of the target element at the left side
    # if its duplicated, returns the leftmost index
    leftmost  =   bisect.bisect_left(array, data)
    # find the index of the target elment at the right side
    # gives the index to the position to insert the element
    rightmost =   bisect.bisect_right(array, data)
    # if left and right are the same, the element not found
    if leftmost == rightmost:
        return False, leftmost, rightmost
    return True, leftmost, rightmost

res = bisect_binary_search(25, sequence)
print(f"Searching (bisect) for 25: {res}")
res = bisect_binary_search(50, sequence)
print(f"Searching (bisect) for 50: {res}")


