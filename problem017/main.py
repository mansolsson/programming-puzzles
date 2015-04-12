single_digits = ["", "one", "two", "three", "four", "five",
                 "six", "seven", "eight", "nine"]
ten_digits = ["ten", "eleven", "twelve", "thirteen", "fourteen",
              "fifteen", "sixteen", "seventeen", "eighteen", "nineteen"]
double_digits = ["", "", "twenty", "thirty", "fourty", "fifty",
                 "sixty", "seventy", "eighty", "ninety"]
hundred = "hundred"
thousand = "thousand"


def number_letter_count(limit):
    length = 0
    for i in range(1, limit):
        length += calc_length(i)
    return length


def calc_length(number):
    if number > 999:
        return four_digit(number)
    elif number > 99:
        return three_digit(number)
    else:
        return two_digit(number)


def four_digit(number):
    length = len(single_digits[int(str(number)[0])]) + len(thousand)
    if int(str(number)[1:]) > 99:
        return length + three_digit(str(number)[1:])
    else:
        length += two_digit(str(number)[2:])
        if int(str(number)[2:]) > 0:
            length += 3
        return length


def three_digit(number):
    length = len(hundred) + len(single_digits[int(str(number)[0])]) + two_digit(str(number)[1:])
    if int(str(number)[1:]) > 0:
        length += 3
    return length


def two_digit(number):
    if int(number) < 10:
        return len(single_digits[int(number)])
    elif int(number) < 20:
        return len(ten_digits[int(str(number)[0])])
    else:
        return len(double_digits[int(str(number)[0])]) + \
            len(single_digits[int(str(number)[1])])

if __name__ == "__main__":
    answer = number_letter_count(1001)
    print(answer)
