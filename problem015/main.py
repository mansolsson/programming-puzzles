import math

if __name__ == '__main__':
    a, b = 20, 20
    result = math.factorial(a + b) // \
        (math.factorial((a + b) - a) * math.factorial(a))
    print(result)
