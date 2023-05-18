# Coded by Lukasz Spychala

# Program that finds the highest number in a list of numbers 
# created by the user. Usage of max() function is forbidden.
# Program must use for loop.

import os
os.system("cls")

# studentScores = [78, 65, 89, 86, 55, 91, 64, 89]
studentScores = input("Input a list of scores: ").split()
for n in range(0, len(studentScores)):
    studentScores[n] = int(studentScores[n])

highestScore = 0

for score in studentScores:
    if highestScore < score:
        highestScore = score

print(f"The highest score is: {highestScore}")