sentence = "Strings, lists and tuples"
print("Accessing index 4: " + sentence[4])
print("Slices [inclusive:exclusive:step]")
print(" [2:5] = " + sentence[2:5])
print(" [3:] = " + sentence[3:])
print(" [:] = " + sentence[:])
print(" [:20:2] = " + sentence[:20:2])
print(" [::2] = " + sentence[::2])
print("Reverse string (for)")
reverse = ""
for x in range(len(sentence)):
    x+=1    
    reverse+=sentence[-x]
print(reverse)
print("Reverse string (slice)")
print(sentence[::-1])

print("Combine/Merge")
x = "combine"+ "Strings"
print(x)
x = ["combine", "elements"] + ["in a list"]
print(x)
x = ("Combine", "or merge") + ("tuples",)
print(x)

print("Multiply elements")
x = "bugs," * 3
print(x)
x = [1,2,3] * 3
print(x)
x = (1,2,3) * 3
print(x)

print("Membership of elements")
x = "my custom bug"
print("'bug' is in :"+x)
print( "bug" in x )
x = ["members","of","list"]
print("'tuple' is in list:")
print(x)
print("tuple" in x)
x = ("members","of","list")
print("'of' is in tuple:")
print(x)
print("of" in x)

print("Iteration on items")
for item in x:
    print(item)
print("using enumerate")
for index, item in enumerate(x):
    print(index, item)
print("Number of items:" + str(len(x)))

print("using min:")
print(x)
x = [13,22,32,56,23,21,34]
print(min(x))
x = ["pame", "rafa", "sam"]
print(x)
print(min(x))
print("using max:")
x = [13,22,32,56,23,21,34]
print(x)
print(max(x))
x = ["pame", "rafa", "sam"]
print(x)
print(max(x))

print("Sum of sequence(numbers)")
x = [10,20,40,20]
print(x)
print(sum(x))
print(sum(x[-3:]))

print("Sorting")
print(x)
print(sorted(x))
x = ["Rafa", "Emi", "pam", "silvia", "Guille", "Sam", "sofi"]
print(x)
print(sorted(x))

print("Sort by second letter")
x = ("Rafae", "Pame", "Sofi", "silvia", "emi", "guille", "oscar")
print(x)
print( sorted(x, key= lambda el: el[1]) )


print("Count items in sequence")
x = "Rafael"
print(x)
print("counting 'a'")
print(x.count('a'))
print("First occurrence (word 'want')")
x = "I want to work with python and I want to learn more"
print(x)
print(x.index("want"))
x = x.split(" ")
print(x)
print(x.index("want"))

print("unpacking elements:")
x = ["This", "is", "python"]
print(x)
a, b, c = x
print(a, b, c)