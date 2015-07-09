if __name__ == "__main__":
    value = 0
    for i in range(1, 1001):
        value += i ** i
    print(str(value)[-10:])
