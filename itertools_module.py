# Collections of tools to handle iterators
# some advance tools
from collections import namedtuple
import itertools
import operator
a = [1,2,3,4]
b = [10,20]
# Product: each element of the first with each element of the second
prod = itertools.product(a, b)
print(list(prod))
# We can repeat the proccess passing the repeat argument, like nested loop, for each
# value pair set the whole product
prod_repeat = itertools.product(a, b, repeat=2)
print(list(prod_repeat))

# Permutations: Return all possible orderings of an input
perm = itertools.permutations(a)
print(list(perm))
# we can specify the length of permutation
perm_l = itertools.permutations(a, 2)
print(list(perm_l))

# Combinations: Gives all the possible combinations of the data with a specified length
# with no repetition
comb = itertools.combinations(a, 3)
print(list(comb))

# Combination with replacement gives all the combinations including if repeat
comb2 = itertools.combinations_with_replacement(a, 3)
print(list(comb2))


# Accumulate: returns accumulated sums or any binary function from the data
accum = itertools.accumulate(a)
print(list(accum))
accum_mul = itertools.accumulate(a, func=operator.mul)
print(list(accum_mul))


# Groupby: Returns iterator with keys and groups from an iterable by applying a function on each one
# the key its the result of the evaluation
group = itertools.groupby(a, key=lambda x: x * 2)
for k, v in group:
    print(k, list(v))
group = itertools.groupby(a, key=lambda x: x < 3)
for k, v in group:
    print(k, list(v))
# using with objects
Person = namedtuple("Person", ["name", "age"])
people = [Person("Rafa", 35), Person("Sofi", 8),  Person("Pam", 35), Person("Emi", 15),
          Person("Irving", 32), Person("Sam", 18)]
# Identify minors
minors = itertools.groupby(people, key=lambda person: person.age <= 18)
for key, value in minors:
    print(key, list(value))
