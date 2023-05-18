import os, random
os.system("cls")

wordList = ["ardvark", "baboon", "camel"]
chosenWord = random.choice(wordList)
print(chosenWord)
playerGuess = input("Guess a letter: ").lower()
print(playerGuess)

for letter in chosenWord:
    if letter == playerGuess:
        print("Right")
    else:
        print("Wrong")