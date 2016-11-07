def get_largest_palindrome():
    largest_palindrome = 0
    for i in range(999, 100, -1):
        for y in range(i, 100, -1):
            product = i * y
            if largest_palindrome < product and is_palindrome(str(product)):
                largest_palindrome = product
    return largest_palindrome


def is_palindrome(value):
    return value == value[::-1]

if __name__ == "__main__":
    answer = get_largest_palindrome()
    print(answer)
