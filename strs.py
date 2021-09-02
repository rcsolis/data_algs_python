# Count charactes and reverse a string without slices or len
string = "RafaelChavez"

def size(data: str) -> int:
    total = 0
    for _ in data:
        total += 1
    return total

print(size(string))


# Reverse string
def reverse(data: str) -> str:
    length = size(data)
    r = ""
    for e in range(length - 1, -1, -1):
        r += data[e]
    return r

print(string[::-1])
print("".join(reversed(string)))
print(reverse(string))
