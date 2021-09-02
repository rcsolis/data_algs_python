print("TUPLES AND SETS")
print("Create an empty tuple")
x = tuple()
print(x)
print("Create a tuple with values")
x = (1,2,3)
x = 1,2,3
print(x)
print("Create a 1 element tuple")
x = 1,
print(x)
print("Parse a list to a typle")
x = [1,2,4,5,8,12,9,3]
print(x, type(x))
x = tuple(x)
print(x, type(x))
print("TUPLES ARE INMUTABLE, but members could be mutable")
y = (1,[4,2,5,],6, 7)
print(y)
print("Del on mutable member")
del y[1][2]
print(y)
print("adding element on mutable member")
y[1].append(3)
print(y)
print("For 'adding' items to a tuple, use concatenation")
x = 3,
print(x, type(x))
print(y, type(y))
x += y
print(x, type(x))

print("SETS - {}")
print("Store no duplicate items, can use math set ops and are Unordered sequence")
del y
del x
print("If you repeat elements, python sets deleteing and preserve only one, {2,5,2,1,7,3,2,4,3,1,6}")
s = {2,5,2,1,7,3,2,4,3,1,6}
print(s)
print("Parse list as set")
l = [1,9,12,25,3,2,4,5,7,6,3,1,3,5,8]
print(l, type(l))
s = set(l)
del l
print(s, type(s))

print("Adding element")
s.add(10)
print(s, type(s))
print("Remove element")
s.remove(3)
print(s, type(s))
print("lenght of set")
print(s, len(s), type(s))
print("check membership")
print(s, 10, 10 in s, type(s))
print("Pop extract a random item for the set")
print(s, s.pop(), s)
print("Clear the set")
print(s, s.clear(), s)
print("*SETS ARE UNORDERED")
l = [99,87,18,23,75,19,100,18,38,47]
print(l, type(l))
s = set(l)
print(s, type(s))
l = list(s)
print(l, type(l))

print("SET MATHS")
s1 = set([1,2,3])
s2 = set([4,5,6,3])
print(s1, type(s1))
print(s2, type(s2))
print("Intersection AND (only items in both): set & set")
print(s1 & s2)
print("Union OR (create a new set with all values): set | set")
print(s1 | s2)
print("Symmetric difference XOR (remove shared elements): set ^ set")
print(s1 ^ s2)
print("Difference (in first set but not in second set) s -s")
print(s1-s2)
print("Subsets ( second set contains firts set) s <= s")
print(s1<=s2)
print("Supersets ( first set contains second set) s >= s")
print(s1>=s2)
