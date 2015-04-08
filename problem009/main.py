import math


def findPythagoreanTriplet():
    for a in range(1, 333):
        for b in range(a + 1, math.floor((1000 - a) / 2)):
            c = 1000 - a - b
            if a ** 2 + b ** 2 == c ** 2:
                return a * b * c
    return 0

if __name__ == "__main__":
    print(findPythagoreanTriplet())
