def isPalindrome(value):
    return value == value[::-1]

if __name__ == "__main__":
    largestPalindrome = 0
    for i in range(999, 100, -1):
        for y in range(i, 100, -1):
            product = i * y
            if largestPalindrome < product and isPalindrome(str(product)):
                largestPalindrome = product
    print(largestPalindrome)
