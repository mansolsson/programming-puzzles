def get_sum_of_even_fibonacci(limit):
    fibonacci1, fibonacci2 = 1, 2
    sum_of_even_fibonacci = 0
    while fibonacci2 < limit:
        if fibonacci2 % 2 == 0:
            sum_of_even_fibonacci += fibonacci2
        fibonacci1, fibonacci2 = fibonacci2, fibonacci1 + fibonacci2
    return sum_of_even_fibonacci

if __name__ == "__main__":
    answer = get_sum_of_even_fibonacci(4000000)
    print(answer)
