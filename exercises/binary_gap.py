# Implementation of Binary Gap function

data = [9, 15, 20, 32, 333, 529, 1041]


def binary_gap(number: int) -> int:
    """
    Creates a binary conversion of the number received and
    search for the most greatest binary gap (continue sequence of 0)
    :param number: Number to evaluate
    :return: number: Returns the maximum binary gap size
    """
    binary = bin(number).replace("0b", "")
    sequence = list(binary)
    # Search if has almost one 0
    if "0" not in sequence:
        return 0

    start = sequence[0]
    maximum = 0
    counter = 0
    # Loop trough the sequence
    for el in sequence:
        current = el
        if current == "1":
            if start == "1":
                # Its a gap
                if counter >= maximum:
                    maximum = counter
                counter = 0
            else:
                start = current
                counter += 1
        else:
            if start == "1":
                counter += 1
    return maximum


for i in range(len(data)):
    print(binary_gap(data[i]))
