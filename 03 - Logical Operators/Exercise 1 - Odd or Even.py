# Coded by Lukasz Spychala

# Program checks if the number is Odd or Even.

import os
os.system("cls")

print("Welcome to Odd or Even number tester.")
number = int(input("Please write your number: "))

numberModulo = number % 2

if numberModulo == 0:
    print("Your number is even.")
else:
    print("Your number is odd")