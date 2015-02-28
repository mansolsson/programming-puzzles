if __name__ == "__main__":
    sumOfSquares, squareOfSum = 0, 0
    for i in range(1, 101):
        sumOfSquares += i ** 2
        squareOfSum += i
    squareOfSum = squareOfSum ** 2
    print(squareOfSum - sumOfSquares)
