import sys
sys.path.insert(0, '../')
import pemath


def find_nth_prime(n):
    primes = [2]
    for i in range(1, n):
        primes.append(pemath.find_next_prime(primes))
    return primes[-1]

if __name__ == "__main__":
    answer = find_nth_prime(10001)
    print(answer)
