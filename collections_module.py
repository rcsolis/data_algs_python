# Samples for using the collections module
# this contains several and useful data structures
import collections

# Counter: dict stores elements as keys and counts as values
counter_list = collections.Counter([1,3,4,2,5,7,4,3,8,2,9,1,5,7,6,8,9,2,1])
print(counter_list)
print(counter_list.items())
print(counter_list.most_common())
print(list(counter_list.elements()))
# namedtuple:  creates a object type similar like abstract
Person = collections.namedtuple("Person", ["name", "age", "job"])
rafa = Person("Rafael", 35, "Software Engineer")
print(rafa)
print(rafa.name, rafa.age, rafa.job)

# Ordereddict: Dict but remember the order of the items inserted
# from python3.7 normal dictionaries remembers the order
ordered = collections.OrderedDict()
ordered["a"] = 1
ordered["c"] = 3
ordered["b"] = 3
ordered["d"] = 4
print(ordered)


# defaultdict: similar for normal dict but with a default value for keys that
# are not been set. This take the python default value for the type that is passed
default_dict = collections.defaultdict(float)
default_dict["a"] = 1
default_dict["b"] = 2
print(default_dict)
print(default_dict["c"])


# deque: Double endend queue
queue = collections.deque()
queue.append(1)
queue.append(2)
queue.append(3)
print(queue)
queue.appendleft(99)
print(queue)
queue.pop()
print(queue)
queue.popleft()
print(queue)
queue.extend([5, 6, 7])
print(queue)
queue.extendleft([100,200,300])
print(queue)
queue.rotate(1)
print(queue)
queue.rotate(-2)
print(queue)