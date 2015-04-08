import math

divisors = [20, 19, 18, 17, 16, 15, 14, 13, 12, 11]


primes = [2]


def findAllPrimeFactors(number):
    factors = []
    remainder = number
    while remainder > 1:
        primeFactor = findNextPrimeFactor(remainder)
        remainder //= primeFactor
        factors.append(primeFactor)
    return factors


def findNextPrimeFactor(number):
    limit = math.ceil(math.sqrt(number))
    for prime in primes:
        if prime > limit:
            return number
        elif number % prime == 0:
            return prime

    primeFactorFound = False
    while not primeFactorFound:
        prime = findNextPrime()
        primes.append(prime)
        if prime > limit:
            return number
        elif number % prime == 0:
            return prime


def findNextPrime():
    number = primes[-1]
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
    d = {}
    for divisor in divisors:
        factors = findAllPrimeFactors(divisor)
        for factor in factors:
            occurences = factors.count(factor)
            key = str(factor)
            if key not in d or d[key] < occurences:
                d[key] = occurences

    lcm = 1
    for key in d.keys():
        occurences = d[key]
        lcm *= (int(key) ** occurences)
    print(lcm)
