import math


def get_divisors(number):
    if number == 1:
        return [1]
    if number % 2 == 0:
        inc = 1
    else:
        inc = 2

    divisors = []
    stop = number // 2
    possible_divisor = 1
    while possible_divisor < stop:
        if number % possible_divisor == 0:
            divisors.append(possible_divisor)
            stop = number // possible_divisor
            if stop != possible_divisor:
                divisors.append(stop)
        possible_divisor += inc
    return divisors


def get_prime_factors(number):
    found_primes = [2]
    prime_factors = []
    remainder = number
    while remainder > 1:
        prime_factor = _find_next_prime_factor(remainder, found_primes)
        remainder //= prime_factor
        prime_factors.append(prime_factor)
    return prime_factors


def _find_next_prime_factor(number, found_primes):
    limit = math.ceil(math.sqrt(number))
    for prime in found_primes:
        if prime > limit:
            return number
        elif number % prime == 0:
            return prime

    prime_factor_found = False
    while not prime_factor_found:
        prime = find_next_prime(found_primes)
        found_primes.append(prime)
        if prime > limit:
            return number
        elif number % prime == 0:
            return prime


def find_next_prime(found_primes):
    number = found_primes[-1]
    if number % 2 == 0:
        number += 1
    else:
        number += 2

    prime_found = _is_new_prime(number, found_primes)
    while not prime_found:
        number += 2
        prime_found = _is_new_prime(number, found_primes)

    return number


def _is_new_prime(number, found_primes):
    limit = math.ceil(math.sqrt(number))
    for prime in found_primes:
        if prime > limit:
            return True
        elif number % prime == 0:
            return False
    return True


def lcm(numbers):
    prime_factor_occurrences = {}
    for number in numbers:
        prime_factors = get_prime_factors(number)
        for prime_factor in prime_factors:
            occurrences = prime_factors.count(prime_factor)
            key = str(prime_factor)
            if key not in prime_factor_occurrences or prime_factor_occurrences[key] < occurrences:
                prime_factor_occurrences[key] = occurrences

    least_common_multiplier = 1
    for key in prime_factor_occurrences.keys():
        occurrences = prime_factor_occurrences[key]
        least_common_multiplier *= (int(key) ** occurrences)
    return least_common_multiplier
