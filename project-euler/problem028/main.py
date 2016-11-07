def get_diagonal_digits_sum(square_height):
    diagonal_numbers = [1]
    for height in range(3, square_height + 1, 2):
        diagonal_numbers.append(diagonal_numbers[-1] + (height - 1))
        diagonal_numbers.append(diagonal_numbers[-1] + (height - 1))
        diagonal_numbers.append(diagonal_numbers[-1] + (height - 1))
        diagonal_numbers.append(diagonal_numbers[-1] + (height - 1))
    return sum(diagonal_numbers)

if __name__ == "__main__":
    answer = get_diagonal_digits_sum(1001)
    print(answer)