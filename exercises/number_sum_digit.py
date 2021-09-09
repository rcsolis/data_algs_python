# for a given number N guess the number X for that the sum of the digits of X
# it is twice the sum of the digits of N

# Get the sum of the digits
def sum_digits(num):
    if num < 10:
        return num
    int_part = num // 10
    total = mod = num % 10
    while int_part > 0:
        mod = int_part % 10
        int_part = int_part // 10
        total += mod
    return total

# gues the number
def guess_number(N):
    goal = sum_digits(N) * 2
    numbers = []
    counter = 0
    i = 0
    # get the first 10 results
    while counter < 100:
        sd = sum_digits(i)
        if sd == goal:
            numbers.append(i)
            counter += 1
        i += 1
    # return the smallest
    return min(numbers)


def solution(N):
    X = guess_number(N)
    print(f"the sum of the digits of {X} = {sum_digits(X)} its equal to the double of the sum of the digits of {N} that is " \
            f"{sum_digits(N) * 2}")


N = input("enter the number:")
solution(int(N))
