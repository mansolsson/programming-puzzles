def readNumbers():
    numbers = []
    with open("numbers.txt", "r") as f:
        for line in f:
            numbers.append(int(line.replace("\n", "")))
    return numbers

if __name__ == "__main__":
    total = sum(readNumbers())
    print(str(total)[:10])
