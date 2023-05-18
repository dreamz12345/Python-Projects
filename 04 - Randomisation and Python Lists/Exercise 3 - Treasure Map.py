# Coded by Lukasz Spychala

# Program that lets user insert "x" in a matrix.
# Example input - 32 Where first digit - Column, Second digit - Row

import os
os.system("cls")

INDEX_FIX = 1 #lists indexes starts counting from 0

row1 = ["o","o","o"]
row2 = ["o","o","o"]
row3 = ["o","o","o"]
map = [row1, row2, row3]
print("{}\n{}\n{}".format(row1, row2, row3))
position = input("Where do you want to put the treasure: ")
userColumn = int(position[0]) - INDEX_FIX
userRow = int(position[1]) - INDEX_FIX
map[userRow][userColumn] = "x"
print("{}\n{}\n{}".format(row1, row2, row3))


