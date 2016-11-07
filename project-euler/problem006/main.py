def get_sum_square_difference(limit):
    sum_of_squares, square_of_sum = 0, 0
    for i in range(1, limit + 1):
        sum_of_squares += i ** 2
        square_of_sum += i
    square_of_sum **= 2
    return square_of_sum - sum_of_squares

if __name__ == "__main__":
    answer = get_sum_square_difference(100)
    print(answer)
