def readMatrix():
    matrix = []
    with open("numbers.txt", "r") as f:
        for line in f:
            matrix.append(line.replace("\n", "").split(" "))
    return matrix


def largestProductHorizontal(matrix):
    largestProduct = 0
    for line in matrix:
        for index in range(0, len(line) - 3):
            product = int(line[index]) * int(line[index + 1]) * \
                int(line[index + 2]) * int(line[index + 3])
            if largestProduct < product:
                largestProduct = product
    return largestProduct


def largestProductVertical(matrix):
    largestProduct = 0
    for row in range(0, len(matrix[0])):
        for column in range(0, len(matrix) - 3):
            product = int(matrix[column][row]) * \
                int(matrix[column + 1][row]) * \
                int(matrix[column + 2][row]) * \
                int(matrix[column + 3][row])
            if largestProduct < product:
                largestProduct = product
    return largestProduct


def largestProductDiagonalRight(matrix):
    largestProduct = 0
    for row in range(0, len(matrix[0]) - 3):
        for column in range(0, len(matrix) - 3):
            product = int(matrix[column][row]) * \
                int(matrix[column + 1][row + 1]) * \
                int(matrix[column + 2][row + 2]) * \
                int(matrix[column + 3][row + 3])
            if largestProduct < product:
                largestProduct = product
    return largestProduct


def largestProductDiagonalLeft(matrix):
    largestProduct = 0
    for row in range(0, len(matrix[0]) - 3):
        for column in range(len(matrix) - 1, 2, -1):
            product = int(matrix[column][row]) * \
                int(matrix[column - 1][row + 1]) * \
                int(matrix[column - 2][row + 2]) * \
                int(matrix[column - 3][row + 3])
            if largestProduct < product:
                largestProduct = product
    return largestProduct

if __name__ == "__main__":
    matrix = readMatrix()
    answer = 0

    result = largestProductHorizontal(matrix)
    if result > answer:
        answer = result

    result = largestProductVertical(matrix)
    if result > answer:
        answer = result

    result = largestProductDiagonalRight(matrix)
    if result > answer:
        answer = result

    result = largestProductDiagonalLeft(matrix)
    if result > answer:
        answer = result

    print(answer)
