# Coded by Lukasz Spychala

# Program that checks if the year is a leap year.

import os
os.system("cls")

print("\nWelcome to Leap Year checker.")

year = int(input("Please enter year: "))

isLeapYear = False
isDivisibleBy4 = False
isDivisibleBy100 = False
isDivisibleBy400 = False

if year % 4 == 0:
    isDivisibleBy4 = True
if year % 100 == 0:
    isDivisibleBy100 = True
if year % 400 == 0:
    isDivisibleBy400 = True

if isDivisibleBy4 == True:
    if isDivisibleBy100 == True:
        if isDivisibleBy400 == True:
            isLeapYear = True
    else:
        isLeapYear = True

if isLeapYear == True:
    print("Year {} is a leap year.".format(year))
else:
    print("Year {} is not a leap year.".format(year))





