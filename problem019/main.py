def isLeapYear(year):
    return year % 4 == 0 and (year % 400 == 0 or year % 100 != 0)


if __name__ == "__main__":
    daysInMonths = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    day = 365
    nrOfSundays = 0
    sunday = 6
    daysInWeek = 7

    for year in range(1901, 2001):
        if(isLeapYear(year)):
            daysInMonths[1] = 29
        else:
            daysInMonths[1] = 28
        for daysInMonth in daysInMonths:
            day %= daysInWeek
            if day == sunday:
                nrOfSundays += 1
            day += daysInMonth
    print(nrOfSundays)
