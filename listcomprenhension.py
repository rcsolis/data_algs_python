print("List comprenhension")

print("basic form is:  list = [transform sequence [filter] ]")

import random
import string

print("Basic using range")
under_10 = [x for x in range(10)]
print("under 10: " + str(under_10))
print("Basic usage, squares")
squares = [x**2 for x in under_10]
print("Squares: "+str(squares))

print("Basic usage, get odd numbers")
odd = [x for x in under_10 if x % 2 > 0 ]
print("Odds: ", str(odd))

print("Basic usage, get multiples of 10")
mult = [x*10 for x in under_10]
print("Mult 10: "+str(mult))

print("Basic usage, get all numbers from string")
s = "I work with more than 10 programming languages, but I love C like and currently, I use 3 or 4 languages in my projects (Python, Go, JS, Dart)"
num = [int(ch) for ch in s if ch.isdigit()]
print("List of ints: "+str(num))

print("Basic usage, get index of a list item")
s = ["Rafael", "Guille", "Emi", "Pam", "Rafa"]
print(s)
idx = [k for k,v in enumerate(s) if v == "Rafa"]
print("Index of Rafa: "+str(idx))

print("Basic usage, delete an item from a list")
print(s)
idx = [k for k in s if k != "Rafa"]
print("new list: "+str(idx))

print("Using condition before iterating")
print("Enven numbers multiplied by 10 and Odd by 5 in range 10")
l = [x*10 if x%2==0 else x*5 for x in range(10)]
print(l)

print("Iterating over 2d array and returns a linear array")
l = [ [1,2], [3,4], [5,6]]
print(l)
l = [ e for r in l for e in r]
print(l)