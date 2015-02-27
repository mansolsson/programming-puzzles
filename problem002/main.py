if __name__ == "__main__":
    fib1, fib2 = 1, 2
    sum = 0
    while fib2 < 4000000:
        if fib2 % 2 == 0:
            sum += fib2
        fib1, fib2 = fib2, fib1 + fib2
    print(sum)
