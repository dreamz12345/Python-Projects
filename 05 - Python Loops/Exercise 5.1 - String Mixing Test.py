# Coded by Lukasz Spychala

# Simple test to see weather or not .replace() will
# reduce the length of a string. Functionality needed for mixing module
# in Random Password Generator

import os
os.system("cls")

string = "abcdefgh"
print(string)
print(len(string))

charToBeReplaced = string[3]
string = string.replace(charToBeReplaced, "", 1)

print(string)
print(len(string))


