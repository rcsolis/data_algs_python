# Get the item with no occurrences in a sequence of elements
# each element has a even number of occurrences except one value
from collections import Counter
from operator import itemgetter

array = [9, 3, 9, 3, 9, 7, 9, 7, 9, 9, 10, 2, 3, 4, 2, 4, 3]


def odd_occurences(sequence):
    counter = Counter(sequence)
    repeated = counter.most_common()
    sorted_list = sorted(list(repeated), key=itemgetter(1))
    less_common = sorted_list[0]
    return less_common[0]


print(odd_occurences(array))
