def readDigits():
    digits = ""
    with open("numbers.txt", "r") as f:
        for line in f:
            digits += line
    return digits.replace("\n", "")


def calcProductOfDigits(digits):
    product = 1
    for digit in digits:
        product *= int(digit)
    return product


if __name__ == "__main__":
    greaterProduct = 0
    digits = readDigits()
    nrOfAdjecentDigits = 13
    for i in range(0, len(digits) - nrOfAdjecentDigits):
        product = calcProductOfDigits(digits[i:i + nrOfAdjecentDigits])
        if greaterProduct < product:
            greaterProduct = product
    print(greaterProduct)
