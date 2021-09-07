# The classic Fibonacci sequence

from math import sqrt, pow, modf

# iterative version (linear order)


def fib_iterative(number):
    a = 0
    b = 1
    for n in range(number-1):
        a, b = b, a+b
    return b

# recursion version (exponential order)


def fib_recursive(number):
    if number < 2:
        return number
    else:
        return fib_recursive(number-1) + fib_recursive(number-2)

# With explicit formula (logarithm order)


def fib_formula(number):
    if number < 2:
        return number
    else:

        p = ((1+sqrt(5))/2)
        j = ((pow(p, number)-pow((1-p), number)) / sqrt(5))
        n = modf(j)
        return int(n[1])

# Divide and conquer version ( logarithm order )


def fib_divide(number):
    if number <= 0:
        return 0
    i = number - 1
    aux1 = 0
    aux2 = 1
    a, b = aux2, aux1
    c, d = aux1, aux2
    while i > 0:
        if i%2 != 0:
            aux1 = d*b + c*a
            aux2 = (d*(b+a))+(c*b)
            a, b = aux1, aux2
        aux1 = c**2 + d**2
        aux2 = d*(2*c + d)
        c, d = aux1, aux2
        i = i // 2
    return a + b


print("Results for number 6")
print("Recursive", fib_recursive(6))
print("By Formula", fib_formula(6))
print("Iterative", fib_iterative(6))
print("Divide&Conquer", fib_divide(6))

print("Benchmark: For each one, executes it 10 times getting fib(100)")
import timeit
print(timeit.timeit(lambda: fib_recursive(100), number=10))
print(timeit.timeit(lambda: fib_formula(100), number=10))
print(timeit.timeit(lambda: fib_iterative(100), number=10))
print(timeit.timeit(lambda: fib_divide(100), number=10))
