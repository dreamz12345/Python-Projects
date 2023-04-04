# Coded by Lukasz Spychala

# Program that simulates flipping coin. (Heads of Tails)

import os, random
os.system("cls")

coin = random.randint(0, 1)

print(coin)

if coin == 0:
    print("Heads\n")
else:
    print("Tails\n")