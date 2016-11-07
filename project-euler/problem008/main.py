def find_largest_product_of_adjacent_digits(nr_of_adjacent):
    digits = read_digits_from_file()
    largest_product = 0
    for i in range(0, len(digits) - nr_of_adjacent):
        product = calc_product_of_digits(digits[i:i + nr_of_adjacent])
        if largest_product < product:
            largest_product = product
    return largest_product


def read_digits_from_file():
    with open("numbers.txt", "r") as file:
        digits = file.read()
    return digits.replace("\n", "")


def calc_product_of_digits(digits):
    product = 1
    for digit in digits:
        product *= int(digit)
    return product


if __name__ == "__main__":
    answer = find_largest_product_of_adjacent_digits(13)
    print(answer)
