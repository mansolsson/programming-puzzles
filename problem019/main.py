def count_sundays_at_first_of_month():
    days_in_months = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    day = 365
    nr_of_sundays = 0
    sunday = 6
    days_in_week = 7

    for year in range(1901, 2001):
        if is_leap_year(year):
            days_in_months[1] = 29
        else:
            days_in_months[1] = 28
        for days_in_month in days_in_months:
            day %= days_in_week
            if day == sunday:
                nr_of_sundays += 1
            day += days_in_month
    return nr_of_sundays


def is_leap_year(year):
    return year % 4 == 0 and (year % 400 == 0 or year % 100 != 0)

if __name__ == "__main__":
    answer = count_sundays_at_first_of_month()
    print(answer)
