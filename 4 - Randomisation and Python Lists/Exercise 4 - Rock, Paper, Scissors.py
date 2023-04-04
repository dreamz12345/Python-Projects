# Coded by Lukasz Spychala

# Program that plays Rock, Paper, Scissors game with the user.

import os, random
os.system("cls")

playerChoice = input("Choose 'Rock', 'Paper' or 'Scissors'\n\n").lower()
print("\033[AYou chose:\n{}\n".format(playerChoice.upper().center(30, "-")))

if playerChoice != "rock" and playerChoice != "paper" and playerChoice != "scissors":
    print("Which is a wrong input. Please try again!\n\n")
    exit()

randomInt = random.randint(0, 2)
if randomInt == 0:
    computerChoice = "rock"
elif randomInt == 1:
    computerChoice = "paper"
elif randomInt == 2:
    computerChoice = "scissors"
print("Computer chose:\n{}\n".format(computerChoice.upper().center(30, "-")))

if playerChoice == "rock" and computerChoice == "scissors":
    print("You Win!".center(30, "-"))
elif playerChoice == "paper" and computerChoice == "rock":
    print("You Win!".center(30, "-"))
elif playerChoice == "scissors" and computerChoice == "paper":
    print("You Win!".center(30, "-"))
elif playerChoice == computerChoice:
    print("It's a Draw!".center(30, "-"))
else:
    print("You Lose!".center(30, "-"))

print("")

