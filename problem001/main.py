if __name__ == "__main__":
    sum = 0
    for i in range(3, 1000, 3):
        sum += i
    for i in range(5, 1000, 5):
        if i % 3 != 0:
            sum += i
    print(sum)
