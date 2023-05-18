# Coded by Lukasz Spychala

import os
os.system("cls")

weight = input("Enter your weight (kg): ")
height = input("Enter your height (m): ")

weight = float(weight)
height = float(height)

print(type(weight))

bmi = weight / (height**2)

print(f"{bmi:.2f}")
