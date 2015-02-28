divisors = [19, 18, 17, 16, 15, 14, 13, 12, 11]


def isDivisableByAll(number):
    for divisor in divisors:
        if number % divisor != 0:
            return False
    return True

if __name__ == "__main__":
    number = 20
    while not isDivisableByAll(number):
        number += 20
    print(number)
