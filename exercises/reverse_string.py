# Several ways to reverse a string

test = "Rafael Chavez Solis"


def using_slices(string: str) -> str:
    return string[::-1]


def using_reversed(string: str) -> str:
    return "".join(reversed(string))


def using_range(string: str) -> str:
    rs = ""
    for i in range(len(string)-1, -1, -1):
        rs += string[i]
    return rs


print(test)
print("Using Slices:", using_slices(test))
print("Using Reversed:", using_reversed(test))
print("Using Range:", using_range(test))
