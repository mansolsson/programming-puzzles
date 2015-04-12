import math


def get_sum_of_digits(number):
    number_as_string = str(number)
    sum_of_digits = 0
    for digit in number_as_string:
        sum_of_digits += int(digit)
    return sum_of_digits

if __name__ == "__main__":
    answer = get_sum_of_digits(math.factorial(100))
    print(answer)
