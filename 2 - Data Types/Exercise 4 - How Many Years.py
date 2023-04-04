# Coded by Lukasz Spychala

import os
os.system("cls")

userAge = input("How old are you? ")

userAgeAsInt = int(userAge)

YOU_ARE_OLD = 90
DAYS_IN_YEAR = 365
WEEKS_IN_YEAR = 52
MONTHS_IN_YEAR = 12

yearsLeft = YOU_ARE_OLD - userAgeAsInt
daysLeft = yearsLeft * DAYS_IN_YEAR
weeksLeft = yearsLeft * WEEKS_IN_YEAR
monthsLeft = yearsLeft * MONTHS_IN_YEAR

print(f"You have {daysLeft} days or {weeksLeft} weeks"
      f" or {monthsLeft} months left until you are {YOU_ARE_OLD} years old.")



