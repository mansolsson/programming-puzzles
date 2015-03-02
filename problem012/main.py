import math


def getNrOfDivisors(number):
    nrOfDivisors = 0
    if number % 2 == 0:
        inc = 1
    else:
        inc = 2

    stop = number + 1
    i = 1
    while i <= stop:
        if number % i == 0:
            stop = number / i
            if stop == i:
                nrOfDivisors += 1
            else:
                nrOfDivisors += 2
        i += inc

    return nrOfDivisors


def getTriangleNumber(n):
    return math.floor(n * (n + 1) / 2)


if __name__ == "__main__":
    n = 1
    while getNrOfDivisors(getTriangleNumber(n)) < 501:
        n += 1
    print(getTriangleNumber(n))
