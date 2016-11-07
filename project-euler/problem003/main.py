import sys
sys.path.insert(0, '../')
import pemath


def get_largest_prime_factor(number):
    prime_factors = pemath.get_prime_factors(number)
    return max(prime_factors)

if __name__ == "__main__":
    answer = get_largest_prime_factor(600851475143)
    print(answer)
