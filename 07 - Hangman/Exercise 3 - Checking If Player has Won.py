import os, random
os.system("cls")

wordList = ["ardvark", "baboon", "camel"]
chosenWord = random.choice(wordList)
print(chosenWord)
chosenWordDisplay = []

# Create list filled with blanks that will represent hidden word
for _ in chosenWord:
    chosenWordDisplay += "_"

# Loop until all blanks are filled, main game loop
# Alternative loop (probably better)
#while "_" in chosenWordDisplay:
while chosenWordDisplay != list(chosenWord):
    playerGuess = input("Guess a letter: ").lower()
    for index, letter in enumerate(chosenWord):
        if letter == playerGuess:
            chosenWordDisplay[index] = playerGuess
    print(chosenWordDisplay)