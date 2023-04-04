# Coded by Lukasz Spychala

# Program that calculates compatibilty 
# between two people based on their names.

import os
os.system ("cls")

trueSum = 0
loveSum = 0
loveScore = 0

print("Welcome to Love Calculator")

nameOne = input("Please enter first name: ").lower()
nameTwo = input("Please enter second name: ").lower()

trueSum += nameOne.count("t") + nameTwo.count("t")
trueSum += nameOne.count("r") + nameTwo.count("r")
trueSum += nameOne.count("u") + nameTwo.count("u")
trueSum += nameOne.count("e") + nameTwo.count("e")

loveSum += nameOne.count("l") + nameTwo.count("l")
loveSum += nameOne.count("o") + nameTwo.count("o")
loveSum += nameOne.count("v") + nameTwo.count("v")
loveSum += nameOne.count("e") + nameTwo.count("e")

loveScore = int(str(trueSum) + str(loveSum))

if loveScore < 10 or loveScore > 90:
    print("Your score is {}%, you go together like cola and mentos.".format(loveScore))
elif loveScore > 40 and loveScore < 50:
    print("Your score is {}%, you are alright together.".format(loveScore))
else:
    print("Your score is {}%".format(loveScore))
