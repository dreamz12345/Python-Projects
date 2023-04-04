# Coded by Lukasz Spychala

# Program that adds all even numbers, starting from 2 to 100 

import os
os.system("cls")

sumOfNumbers = 0
for number in range(2, 101, 2):
    sumOfNumbers += number
print(f"Sum of numbers = {sumOfNumbers}")