import math

if __name__ == "__main__":
    number = str(math.factorial(100))
    sumOfDigits = 0
    for digit in number:
        sumOfDigits += int(digit)
    print(sumOfDigits)
