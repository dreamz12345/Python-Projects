# Coded by Lukasz Spychala

# Program that prints numbers from 1 to 100 but if number is divisible
# by 3 it prints "Fizz", by 5 it prints "Buzz" and by 3 and 5 at the same
# time it prints "FizzBuzz"

import os
os.system("cls")

for number in range(1, 101):
    if number % 3 == 0 and number % 5 == 0:
        print("FizzBuzz")
    elif number % 5 == 0:
        print("Buzz")
    elif number % 3 == 0:
        print("Fizz")
    else:
        print(number)


