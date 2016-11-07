import sys
sys.path.insert(0, "../")
import pemath


def get_sum_of_primes_below(limit):
    primes = [2]
    while primes[-1] < limit:
        primes.append(pemath.find_next_prime(primes))
    return sum(primes[:-1])

if __name__ == "__main__":
    answer = get_sum_of_primes_below(2000000)
    print(answer)
