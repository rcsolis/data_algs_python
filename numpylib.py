# Samples of numpy
import numpy as np

print(np.__version__)
a = np.array([1, 2, 3])
print("Prints the array", a)
print("Shape of the array:", a.shape)
print("Type of element:", a.dtype)
print("Bit size of element:", a.itemsize)
print("Dimension:", a.ndim)
print("Total elements:", a.size)
print("First element:", a[0])
a[0] = 10
print("First element (updated):", a[0])

b = a * np.array([2, 0, 2])
print("Multiply arrays (same dimension):", b)

print("Differents with native lists")
plist = [1, 2, 3]
array = np.array(plist)
print("Python List:", plist)
print("NP array:", array)

print("Appending elements")
plist.append(4)
array = np.append(array, 4)
print("Python List:", plist)
print("NP array:", array)

print("+ operator")
plist = [1, 2, 3]
array = np.array(plist)
plist = plist + [4]
array = array + [4]
print("Python List:", plist)
print("NP array:", array)

print("* operator")
plist = [1, 2, 3]
array = np.array(plist)
plist = plist * 4
array = array * 4
print("Python List:", plist)
print("NP array:", array)

print("+ operator")
plist = [1, 2, 3]
array = np.array(plist)
plist = plist + [4]
array = array + [4]
print("Python List:", plist)
print("NP array:", array)

print("Apply sqrt to each element")
array = np.array([1, 2, 3, 4])
print("NP array:", array)
array = np.sqrt(array)
print("NP array:", array)

print("DOT PRODUCT")
l1 = [1, 2, 3]
l2 = [4, 5, 6]
dotpy = 0
for i in range(len(l1)):
    dotpy += l1[i] * l2[i]
print("In python:", dotpy)
np1 = np.array(l1)
np2 = np.array(l2)
dotnp = np.dot(np1, np2)
print("In NP (dot func):", dotnp)
dotnp = np1 * np2
dotnp = np.sum(dotnp)
print("In NP (using *):", dotnp)
dotnp = np1 @ np2
print("In NP (using @):", dotnp)

print("Multidimentional arrays:")
ma = np.array([[1, 2], [3, 4], [5, 6]])
print(ma, ma.shape)
print("first element: [row=0,col=0]", ma[0, 0])
print("slices")
print("All rows column 0", ma[:, 0])
print("All columns row 0", ma[0, :])
print("Transpose:", ma, ma.T)

bool_idx = ma > 2
print("Evaluate bool index(test elements)", bool_idx)
print("Getting elements with bool index:", ma[bool_idx])
ss = np.where(ma > 2, ma, -1)
print("Getting same size array with bool index(put -1 if false):", ss)

ma = np.array([10, 19, 30, 40, 61])
print(ma)
ima = [0, 2, 4]
print("getting elements using python list", ma[ima])
evens = np.argwhere(ma % 2 == 0).flatten()
print("Getting evens:", ma[evens])

ma = np.arange(1, 7)
print(ma)
mab = ma.reshape((2, 3))
print("Reshape in 2 rows and 3 cols:", mab)
print("Reshape using newaxis:")
mab = ma[np.newaxis, :]
print(mab, mab.shape)
mab = ma[:, np.newaxis]
print(mab, mab.shape)

print("Concatenation")
ma = np.array([[1, 2], [3, 4]])
print(ma)
mb = np.array([[5, 6], [7, 8]])
print(mb)
mc = np.concatenate((ma, mb))
print(mc)
mc = np.concatenate((ma, mb), axis=None)
print(mc)
mc = np.concatenate((ma, mb), axis=1)
print(mc)
mc = np.concatenate((ma, mb.T), axis=1)
print(mc)
print("hstack, vstack:")
ma = np.array([1, 2, 3])
mb = np.array([4, 5, 6])
print(np.hstack((ma, mb)))
print(np.vstack((ma, mb)))

print("BROADCASTING ( arrays of different shapes )")
ma = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12]])
mb = np.array([1, 0, -1])
print(ma, "+", mb)
mc = ma + mb
print(mc)
print("Some DS common functions:")
ma = np.array([[1, 2, 3, 4, 5, 6, 7, 8, 9], [11, 12, 13, 14, 15, 16, 17, 18, 19]])
print(ma)
print("Calculates total sum:", ma.sum())
print("Calculates sum columns:", ma.sum(axis=0))
print("Calculates sum rows:", ma.sum(axis=1))
print("Calculates total mean:", ma.mean())
print("Calculates mean per col:", ma.mean(axis=0))
print("Calculates mean per row:", ma.mean(axis=1))
print("Calculates variants:", ma.var())
print("Calculates standard deviation:", ma.std())
print("Minumum:", ma.min())
print("Minumum row:", ma.min(axis=0))
print("Minumum cols:", ma.min(axis=1))
print("Maximum:", ma.max())
print("Maximum row:", ma.max(axis=0))
print("Maximum col:", ma.max(axis=1))

print("COPYING")
ma = np.array([1, 2, 3])
print(ma)
print("Using = (reference like pointers)")
mb = ma
mb[0] = 42
print(mb)
print(ma)
print("Using copy to duplicate")
ma = np.array([1, 2, 3])
mb = ma.copy()
print(mb)
print(ma)

print("Generating arrays")
mz = np.zeros((3, 3))
print("ZEROS (3,3):", mz)
mo = np.ones((3, 3))
print("ONES (3,3):", mo)
mc = np.full((3, 3), 8.0)
print("Custom (3,3):", mc)

print("IDENTITY MAT:", np.eye(3))

print("Arange:", np.arange(10))
print("With step:", np.arange(0, 10, 2))
print("Using linsapce to get a N elements equally spaced:", np.linspace(0, 10, 5))

print("RANDOM NUMBERS")
r = np.random.random((3, 2))
print("Between 0-1", r)
r = np.random.randn(3, 2)
print("Normal/Gaussian (mean=0, var=1)", r)

r = np.random.randint(3, 10, size=(2, 2))
print("Random integers with shape", r)

r = np.random.choice(5, size=10)
print("Random one dim array of size 10 with numbers between 0 and 5", r)
r = np.random.choice([-3, -6, 7], size=5)
print("Random one dim array of size 10 with numbers in list:", r)

print("Compare values")
a = np.array([[1, 2], [3, 4]])
b = np.array([[1, 2], [3, 4]])
print("Using == might cause errors:", a == b)
print("Correct is using allclose:", np.allclose(a, b))

print("LINEAR ALGEBRA MODULE")
a = np.array([[1, 2], [3, 4]])
eigenvalues, eigenvectors = np.linalg.eig(a)
print("EigenValues:", eigenvalues, "EigenVectors:", eigenvectors)

print("Solving x + y = 2200 and 1.5x + 4y = 5050")
print("Using inv and dot")
A = np.array([
    [1, 1],
    [1.5, 4.0]
])
b = np.array([2200, 5050])
x = np.linalg.inv(A).dot(b)
print(x)
print("Second way using solve:")
x = np.linalg.solve(A, b)
print(x)

print("Loading CSV")
data = np.loadtxt('sample.csv', delimiter=",", dtype=int)
print(data)
