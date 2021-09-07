# Lamba function is a one line anonymous function (without name)
# Define unsing lambda keyword
square = lambda x: x ** 2
print(square(2))

mult = lambda x, y: x ** y
print(mult(2, 4))

# Sorted method
persons = [("Rafael", 35), ("Emi", 15), ("Sof", 8), ("Sam", 20)]
sort_people = sorted(persons)
print(sort_people)
age_sort_people = sorted(persons, key=lambda x: x[1])
print(age_sort_people)

# Map method: Transforms each element whit a function
persons_map = map(lambda x: (x[0].upper(), x[1]), persons)
print(list(persons_map))

# Filter method: Returns all the elements that the function provided evaluates
# to True, the function always must returns true or false
persons_minors = filter(lambda x: x[1] < 18, persons)
print(list(persons_minors))

# Reduce method: Repeatedly applies the function to the elements and returns
# a single value
from functools import reduce
average_age = reduce(lambda x, y: x+y[1], persons, 0) // len(persons)
print(average_age)
