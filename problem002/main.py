if __name__ == "__main__":
    fib1, fib2 = 1, 2
    sumOfEvenFib = 0
    while fib2 < 4000000:
        if fib2 % 2 == 0:
            sumOfEvenFib += fib2
        fib1, fib2 = fib2, fib1 + fib2
    print(sumOfEvenFib)
