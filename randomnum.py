import random

items = [1, 4, 9, 3, 7, 2, 0, 8, 5]
print(items)
# Random choice from list
rnum = random.choice(items)
print(rnum)
rnum = random.choices(items)
print(rnum)
# Random shuffle
random.shuffle(items)
print(items)

print(random.randint(0, 100))
print(random.randrange(0, 50, 5))