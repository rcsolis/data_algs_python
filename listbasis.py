print("LISTS")
x = list()
print("empty list():", x)
x = ("this", "were", "be", "a", "tuple")
print("parse a tuple")
print(x)
x = list(x)
print(x)

print("List comprenhension:")
x = [par for par in range(100) if par%2 == 0]
print(x)

print("delete list elements")
del(x[10:])
print(x)
print("Append element")
x.append(100)
print(x)

print("Extend using for merge lists")
x = [1,3,5]
y = [100,430,213]
print(x)
print(y)
x.extend(y)
print(x)
y.extend(x)
print(y)

print("Insert element at given index")
x = [1,3,5,7]
print(x)
x.insert(2,[2,4,6])
print(x)

print("Pop last elment of list")
e = x.pop()
print(e)

print("Remove the first instance of an item")
x.remove(3)

print("Sort in place items")
x = [9,12,3,12,4,2,54,7,4,2]
print(x)
x.sort()
print(x)

print("Reversse order in list in place")
x.reverse()
print(x)
x.sort()
print(x)
print("Reversing sort in place")
x.sort(reverse=True)
print(x)