if __name__ == "__main__":
    largestPalindrome = 0
    for i in range(999, 100, -1):
        for y in range(i, 100, -1):
            result = i * y
            if largestPalindrome < result and str(result) == str(result)[::-1]:
                largestPalindrome = result
    print(largestPalindrome)
