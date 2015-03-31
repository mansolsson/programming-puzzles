singleDigits = ["", "one", "two", "three", "four", "five",
                "six", "seven", "eight", "nine"]
tenDigits = ["ten", "eleven", "twelve", "thirteen", "fourteen",
             "fifteen", "sixteen", "seventeen", "eighteen", "nineteen"]
doubleDigits = ["", "", "twenty", "thirty", "fourty", "fifty",
                "sixty", "seventy", "eighty", "ninety"]
hundred = "hundred"
thousand = "thousand"


def calcLength(number):
    if number > 999:
        return fourDigit(number)
    elif number > 99:
        return threeDigit(number)
    else:
        return twoDigit(number)


def fourDigit(number):
    sum = len(singleDigits[int(str(number)[0])]) + len(thousand)
    if int(str(number)[1:]) > 99:
        return sum + threeDigit(str(number)[1:])
    else:
        sum = sum + twoDigit(str(number)[2:])
        if int(str(number)[2:]) > 0:
            sum += 3
        return sum


def threeDigit(number):
    sum = len(hundred) + len(singleDigits[int(str(number)[0])]) \
          + twoDigit(str(number)[1:])
    if int(str(number)[1:]) > 0:
        sum += 3
    return sum


def twoDigit(number):
    if int(number) < 10:
        return len(singleDigits[int(number)])
    elif int(number) < 20:
        return len(tenDigits[int(str(number)[0])])
    else:
        return len(doubleDigits[int(str(number)[0])]) + \
            len(singleDigits[int(str(number)[1])])

if __name__ == "__main__":
    sum = 0
    for i in range(1, 1001):
        sum += calcLength(i)
    print(sum)
