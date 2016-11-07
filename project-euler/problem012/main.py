import sys
sys.path.insert(0, '../')
import pemath


def get_first_triangle_number_with_more_divisors(number_of_divisors):
    number = 1
    while len(pemath.get_divisors(get_triangle_number(number))) < number_of_divisors + 1:
        number += 1
    return get_triangle_number(number)


def get_triangle_number(number):
    return number * (number + 1) // 2

if __name__ == "__main__":
    answer = get_first_triangle_number_with_more_divisors(500)
    print(answer)
