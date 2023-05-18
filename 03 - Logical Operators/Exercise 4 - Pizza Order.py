# Coded by Lukasz Spychala

# Program that allows user to select pizza size and extra ingridients
# and calculates total bill for them.

import os
os.system("cls")

SMALL_PIZZA = 15
MEDIUM_PIZZA = 20
LARGE_PIZZA = 25
S_PEPPERONI = 2
M_L_PEPPERONI = 3
EXTRA_CHEESE = 1

pizzaSize = None
addExtra = None
totalBill = 0

print("Welcome to Automatic Pizza Order.")

pizzaSize = input("What size pizza do you want to order?(S, M, L): ")
if pizzaSize == "S":
    totalBill = totalBill + SMALL_PIZZA
elif pizzaSize == "M":
    totalBill = totalBill + MEDIUM_PIZZA
elif pizzaSize == "L":
    totalBill = totalBill + LARGE_PIZZA
else:
    print("Wrong input, Please try again.")
    exit()

addExtra = input("Would you like additional pepperoni?(Y or N): ")
if addExtra == "Y":
    if pizzaSize == "S":
        totalBill = totalBill + S_PEPPERONI
    elif pizzaSize == "M" or "L":
        totalBill = totalBill + M_L_PEPPERONI
elif addExtra not in ("Y", "N"):
    print("Wrong input, Please try again.")
    exit()
addExtra = None

addExtra = input("Would you like additional cheese?(Y or N): ")
if addExtra == "Y":
    totalBill = totalBill + EXTRA_CHEESE
elif addExtra != "Y" and "N":
    print("Wrong input, Please try again.")
    exit()
addExtra = None

print("Your total bill is: ${}".format(totalBill))
