month_day = {0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31}


def is_leap(year):
    return year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)


print(is_leap(2012))