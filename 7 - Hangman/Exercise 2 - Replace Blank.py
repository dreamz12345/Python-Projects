import os, random
os.system("cls")

wordList = ["ardvark", "baboon", "camel"]
chosenWord = random.choice(wordList)
print(chosenWord)
chosenWordDisplay = []

for _ in chosenWord:
    chosenWordDisplay += "_"

playerGuess = input("Guess a letter: ").lower()

for index, letter in enumerate(chosenWord):
    if letter == playerGuess:
        print("Right")
        chosenWordDisplay[index] = playerGuess
    else:
        print("Wrong")

print(chosenWordDisplay)