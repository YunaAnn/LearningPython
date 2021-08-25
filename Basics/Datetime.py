import datetime


def is_valid_date(year, month, day):
    # returns True if year-month-day is a valid date
    #  returns False if date is invalid
    try:
        datetime.date(year, month, day)
    except ValueError:
        return False
    return True


def days_in_month(year, month):
    # returns the number of days in the input month
    if datetime.MINYEAR <= year <= datetime.MAXYEAR and 0 < month < 13:
        if month == 12:
            diff = datetime.date(year + 1, 1, 1) - datetime.date(year, month, 1)
        else:
            diff = datetime.date(year, month + 1, 1) - datetime.date(year, month, 1)
        return diff.days
    else:
        return 'Error: Invalid month or/and year'


def days_between(year1, month1, day1, year2, month2, day2):
    # returns the number of days from the 1st date to 2nd date
    # returns 'Error: Invalid date(s)' if either date is invalid
    # returns 'Error: the 2nd date is before the 1st date' if the 2nd date is before 1st date
    if not is_valid_date(year1, month1, day1) or not is_valid_date(year2, month2, day2):
        return 'Error: Invalid date(s)'
    date1 = datetime.date(year1, month1, day1)
    date2 = datetime.date(year2, month2, day2)
    if date2 < date1:
        return 'Error: the 2nd date is before the 1st date'
    else:
        return (date2 - date1).days


def age_in_days(year, month, day):
    # returns the age of a person with the input birthday as of today
    # or returns 'Error: Invalid date or the input date is in the future' if data is invalid
    today = datetime.date.today()
    if not is_valid_date(year, month, day) or today < datetime.date(year, month, day):
        return 'Error: Invalid date or the input date is in the future'
    else:
        person_age = datetime.date(year, month, day)
        return (today - person_age).days


if __name__ == '__main__':
    print('Check if date is valid')
    print('1999-12-31')
    print(is_valid_date(1999, 12, 31))                  # Output: True
    print('2000-12-32')
    print(is_valid_date(1999, 12, 32))                  # Output: False
    print('==========================')
    print('Days in month')
    print('inputs (year, month) -> (1999, 12)')
    print(days_in_month(1999, 12))                      # Output: 31
    print('inputs (year, month) -> (19999, 25)')
    print(days_in_month(19999, 25))                     # Output: Error: Invalid month or/and year
    print('==========================')
    print('Days between')
    print('Dates: 2000-1-1, 1999-12-31')
    print(days_between(2000, 1, 1, 1999, 12, 31))      # Output: Error: the 2nd date is before the 1st date
    print('Dates: 1999-12-31, 2000-1-1')
    print(days_between(1999, 12, 31, 2000, 1, 1))      # Output: 1
    print('Dates: 1999-12-33, 2000-1-1')
    print(days_between(1999, 12, 33, 2000, 1, 1))      # Output: Error: Invalid date(s)
    print('==========================')
    print('Age in days')
    print('Today', datetime.date.today())
    print('Birthday date: 2000-1-1')
    print(age_in_days(2000, 1, 1))      # Output: 7907 (Today:2021-08-25)
    print('Dates: 1999-12-31, 2000-1-1')
    print(age_in_days(3000, 1, 1))      # Output: Error: Invalid date or the input date is in the future
    print('==========================')
