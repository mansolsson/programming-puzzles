def get_fibonacci_term_with_number_of_digits(nr_of_digits):
    term = 1
    fib1, fib2 = 1, 1
    while len(str(fib1)) < nr_of_digits:
        fib1, fib2 = fib2, fib1 + fib2
        term += 1
    return term

if __name__ == "__main__":
    answer = get_fibonacci_term_with_number_of_digits(1000)
    print(answer)
