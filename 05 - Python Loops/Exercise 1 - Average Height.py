# Coded by Lukasz Spychala

# Program that calculates average height of students.
# Program must use for loop 

import os
os.system("cls")

studentHeights = input("Input a list of heights: ").split()
for n in range(0, len(studentHeights)):
    studentHeights[n] = int(studentHeights[n])

sumHeight = 0
numberOfPeople = 0

for height in studentHeights:
    sumHeight += height
    numberOfPeople += 1

averageHeight = round(sumHeight / numberOfPeople)
print(averageHeight)