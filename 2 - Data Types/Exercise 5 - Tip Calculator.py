# Coded by Lukasz Spychala

import os
os.system("cls")

print("Welcome to the Tip Calculator.")
bill = float(input("What was the total bill? $"))
tip = int(input("What percentage tip would you like to give? 10, 12, 15? "))
numberOfPeople = int(input("How many people to split the bill? "))

tipPercentage = tip * 0.01
billWithTip = bill + (bill * tipPercentage)
billForEachPerson = billWithTip / numberOfPeople

billForEachPersonStr = "{:.2f}".format(billForEachPerson)
print(f"Each person should pay: ${billForEachPersonStr}")



