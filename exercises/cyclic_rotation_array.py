# Implements the rotation of elements
# An array A consisting of N integers is given.
# Rotation of the array means that each element is shifted right by one index,
# and the last element of the array is moved to the first place. F
# or example, the rotation of array A = [3, 8, 9, 7, 6] is [6, 3, 8, 9, 7]
# (elements are shifted right by one index and 6 is moved to the first place).

data = [3, 8, 9, 7, 6]
number_places = 8


def cyclic_rotation_manual(array, places):
    if places > len(array):
        return array
    if len(array) <= 1:
        return array
    rotated = [array[index] for index in range(-places, len(array) - places, 1)]
    return rotated


def cyclic_rotation_builtin(array, places):
    from collections import deque
    queue = deque(array)
    queue.rotate(places)
    return list(queue)


print(f"Original sequence: {data}")
print("Moving {0} positions".format(number_places))
print(cyclic_rotation_manual(data, number_places))
print(cyclic_rotation_builtin(data, number_places))
