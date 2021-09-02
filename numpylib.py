import numpy as np

arr = np.array([
    [1, 2, 3],
    [4, 5, 6]
])
print(arr)
zeroarr = np.zeros((4, 4))
print(zeroarr)

onesarr = np.ones((2, 2))
print(onesarr)

arr1 = np.array([1, 2, 3])
arr2 = np.array([4, 5, 6])
arrSum = np.sum((arr1, arr2), axis=0)
print(arrSum)
arrSum = np.sum((arr1, arr2), axis=1)
print(arrSum)
# Largest value
arr = np.array([1, 100, 13, 16, 3, 89])
arrg = arr[np.argsort(arr)[::-1]]
print(arrg[0])
# Smallest value
print(arrg[-1])
# replace odd values
l = np.array([1, 2, 3, 4, 5, 6, 7, 8])
l[l % 2 == 0] = -1
print(l)
# Common items
l1 = np.array([1, 2, 3, 4, 5, 6])
l2 = np.array([2, 3, 8, 9, 10])
print(np.intersect1d(l1, l2))
