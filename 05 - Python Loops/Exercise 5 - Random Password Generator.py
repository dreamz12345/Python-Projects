# Coded by Lukasz Spychala

# Program that creates safe random password.
# Password length, amount of numbers and amount of symbols are set by the user.

import os, random
os.system("cls")

print("Welcome to password generator!")

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 
           'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 
           'u', 'v', 'w', 'x', 'y', 'z',
           'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 
           'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 
           'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '@', '#', '$', '%', '^', '&', '*', '(', ')']
password = ""
passwordMixed = ""

passwordLength = int(input("How long do you want your password to be?: "))
amountOfNumbers = int(input("How many numbers do you want in your password?: "))
amountOfSymbols = int(input("How many symbols do you want in your password?: "))
amountOfLetters = passwordLength - (amountOfNumbers + amountOfSymbols)

for loop in range(0, amountOfLetters):
    randomNumber = random.randint(0, len(letters) - 1)
    password += letters[randomNumber]

for loop in range(0, amountOfNumbers):
    randomNumber = random.randint(0, len(numbers) - 1)
    password += numbers[randomNumber]

for loop in range(0, amountOfSymbols):
    randomNumber = random.randint(0, len(symbols) - 1)
    password += symbols[randomNumber]

print(f"\n{password} - Password before mixing.")

for loop in range(0, passwordLength):
    randomNumber = random.randint(0, len(password) - 1)
    passwordMixed += password[randomNumber]
    password = password.replace(password[randomNumber], '', 1)

print(f"\n{passwordMixed} - Password after mixing\n")
