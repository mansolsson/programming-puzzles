def get_largest_product_in_grid():
    matrix = read_matrix_from_file()
    largest_product = largest_product_horizontal(matrix)

    result = largest_product_vertical(matrix)
    if result > largest_product:
        largest_product = result

    result = largest_product_diagonal_right(matrix)
    if result > largest_product:
        largest_product = result

    result = largest_product_diagonal_left(matrix)
    if result > largest_product:
        largest_product = result

    return largest_product


def read_matrix_from_file():
    matrix = []
    with open("numbers.txt", "r") as f:
        for line in f:
            matrix.append(line.replace("\n", "").split(" "))
    return matrix


def largest_product_horizontal(matrix):
    largest_product = 0
    for line in matrix:
        for index in range(0, len(line) - 3):
            product = int(line[index]) * int(line[index + 1]) * \
                int(line[index + 2]) * int(line[index + 3])
            if largest_product < product:
                largest_product = product
    return largest_product


def largest_product_vertical(matrix):
    largest_product = 0
    for row in range(0, len(matrix[0])):
        for column in range(0, len(matrix) - 3):
            product = int(matrix[column][row]) * \
                int(matrix[column + 1][row]) * \
                int(matrix[column + 2][row]) * \
                int(matrix[column + 3][row])
            if largest_product < product:
                largest_product = product
    return largest_product


def largest_product_diagonal_right(matrix):
    largest_product = 0
    for row in range(0, len(matrix[0]) - 3):
        for column in range(0, len(matrix) - 3):
            product = int(matrix[column][row]) * \
                int(matrix[column + 1][row + 1]) * \
                int(matrix[column + 2][row + 2]) * \
                int(matrix[column + 3][row + 3])
            if largest_product < product:
                largest_product = product
    return largest_product


def largest_product_diagonal_left(matrix):
    largest_product = 0
    for row in range(0, len(matrix[0]) - 3):
        for column in range(len(matrix) - 1, 2, -1):
            product = int(matrix[column][row]) * \
                int(matrix[column - 1][row + 1]) * \
                int(matrix[column - 2][row + 2]) * \
                int(matrix[column - 3][row + 3])
            if largest_product < product:
                largest_product = product
    return largest_product

if __name__ == "__main__":
    answer = get_largest_product_in_grid()
    print(answer)
