# Coded by Lukasz Spychala

# Program that creates list of names based on user input and then
# randomly selects one name from that list. 

import os, random
os.system("cls")

INDEX_FIX = 1 #lists indexes starts counting from 0

listOfNames = input("Please write names separeted by \", \": ").split(", ")
randomNumber = random.randint(0, len(listOfNames) - INDEX_FIX)
print("{} is going to buy the meal today!".format(listOfNames[randomNumber]))



