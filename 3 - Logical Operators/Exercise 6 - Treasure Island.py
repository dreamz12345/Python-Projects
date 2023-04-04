# Coded by Lukasz Spychala

# Game that uses if/else to progress story depending on users input.

import os
os.system ("cls")

playerChoice = None

print("Welcome to Treasure Island!\nYour mission is to find the treasure.\n")

playerChoice = input("You are at the crossroads. Would you like to go 'Left' or 'Right'? \n").lower()
if playerChoice == "right":
    print("\033[A-----{}-----".format(playerChoice).upper())
    print("\nYou stepped into a trap. Ouch!\n\nGame Over!\n")
    exit()
elif playerChoice != "left":
    print("\nWrong input. Please try again.\n")
    exit()
print("\033[A-----{}-----".format(playerChoice).upper())


playerChoice = input("\nYou are now standing in front of the river. Would you like to 'Wait' or 'Swim'? \n").lower()
if playerChoice == "swim":
    print("\033[A-----{}-----".format(playerChoice).upper())
    print("\nThere's Giant Enemy Sharks in the river. Too bad...\n\nGame Over!\n")
    exit()
elif playerChoice != "wait":
    print("\nWrong input. Please try again.\n")
    exit()
print("\033[A-----{}-----".format(playerChoice).upper())


playerChoice = input("\nOctupusFaceCapitan appears from underneath the water and offers you a ferry. "
                     "Would you like to 'Accept' or 'Decline'? \n").lower()
if playerChoice == "accept":
    print("\033[A-----{}-----".format(playerChoice).upper())
    print("\nYou became a part of the ships crew forever!\n\nGame Over!\n")
    exit()
elif playerChoice != "decline":
    print("\nWrong input. Please try again.\n")
    exit()
print("\033[A-----{}-----".format(playerChoice).upper())


playerChoice = input("\nYou remembered your pocket monster can use ability 'Fly', "
                     "it carries you over to the other side of the river.\n"
                     "You see an old Dwarvish gate that leads underground, "
                     "Would you like to 'Enter' or 'Stay'? \n").lower()
if playerChoice == "stay":
    print("\033[A-----{}-----".format(playerChoice).upper())
    print("\nYou see a beautiful falling star! Unfortunetly, it lands where u stand...\n\nGame Over!\n")
    exit()
elif playerChoice != "enter":
    print("\nWrong input. Please try again.\n")
    exit()
print("\033[A-----{}-----".format(playerChoice).upper())


playerChoice = input("\nYou see a big treasure inside the ruins, "
                     "Would you like to 'Take' the treasure or 'Leave' it? \n").lower()
if playerChoice == "leave":
    print("\033[A-----{}-----".format(playerChoice).upper())
    print("\nYou left the treasure untouched. Why would you do that?\n\nGame Over!\n")
    exit()
elif playerChoice != "take":
    print("\nWrong input. Please try again.\n")
    exit()
print("\033[A-----{}-----".format(playerChoice).upper())

print("\nYou filled your pockets with gold and escaped safely. You Win!\n\nThanks for playing Treasure Island!\n\n")

