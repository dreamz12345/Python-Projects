import os

def clear_screen():
    """Clear the console."""
    os.system("cls")

def is_leap_year(year):
    """Takes a year and checks if its a leap year, then 
    returns 'True' or 'False' bool."""
    is_leap_year = False
    is_divisible_by_4 = False
    is_divisible_by_100 = False
    is_divisible_by_400 = False

    if year % 4 == 0:
        is_divisible_by_4 = True
    if year % 100 == 0:
        is_divisible_by_100 = True
    if year % 400 == 0:
        is_divisible_by_400 = True

    if is_divisible_by_4 == True:
        if is_divisible_by_100 == True:
            if is_divisible_by_400 == True:
                is_leap_year = True
        else:
            is_leap_year = True

    return is_leap_year

def number_of_days(year, month):
    """Takes a year and month then returns number of days in that month."""
    days_in_month = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    if is_leap_year(year) == True:
        days_in_month[1] = 29
    return days_in_month[month - 1]


clear_screen()
year = int(input("Please enter year: "))
month = int(input("Please enter month: "))
days = number_of_days(year=year, month=month)
print(f"In year: {year}, month: {month} "
          f"there's {days} days.")