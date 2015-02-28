import math

primes = [2]


def findAllPrimeFactors(number):
    factors = []
    remainder = number
    while remainder > 1:
        primeFactor = findNextPrimeFactor(remainder)
        remainder = remainder / primeFactor
        factors.append(primeFactor)
    return factors


def findNextPrimeFactor(number):
    limit = math.ceil(math.sqrt(number))
    for prime in primes:
        if prime > limit:
            return int(number)
        elif number % prime == 0:
            return prime

    primeFactorFound = False
    while not primeFactorFound:
        prime = findNextPrime()
        primes.append(prime)
        if prime > limit:
            return int(number)
        elif number % prime == 0:
            return prime


def findNextPrime():
    number = primes[len(primes) - 1]
    if number % 2 == 0:
        number += 1
    else:
        number += 2

    primeFound = isNewPrime(number)
    while not primeFound:
        number += 2
        primeFound = isNewPrime(number)

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
    print(max(findAllPrimeFactors(600851475143)))
