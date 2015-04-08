if __name__ == "__main__":
    sumOfMultiples = 0
    for multiple in range(3, 1000, 3):
        sumOfMultiples += multiple
    for multiple in range(5, 1000, 5):
        if multiple % 3 != 0:
            sumOfMultiples += multiple
    print(sumOfMultiples)
