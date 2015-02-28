import math

primes = [2]


def findNextPrime():
    number = primes[-1]
    if number % 2 == 0:
        number += 1
    else:
        number += 2
    while not isNewPrime(number):
        number += 2
    return number


def isNewPrime(number):
    limit = math.ceil(math.sqrt(number))
    for prime in primes:
        if prime > limit:
            return True
        elif number % prime == 0:
            return False
    return True

if __name__ == "__main__":
    for i in range(1, 10001):
        primes.append(findNextPrime())
    print(primes[-1])
