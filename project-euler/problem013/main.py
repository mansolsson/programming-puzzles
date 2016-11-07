def get_first_digits_from_sum():
    sum_of_numbers = sum(read_numbers_from_file())
    return str(sum_of_numbers)[:10]


def read_numbers_from_file():
    numbers = []
    with open("numbers.txt", "r") as f:
        for line in f:
            numbers.append(int(line.replace("\n", "")))
    return numbers

if __name__ == "__main__":
    answer = get_first_digits_from_sum()
    print(answer)
