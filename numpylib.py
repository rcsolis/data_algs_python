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
