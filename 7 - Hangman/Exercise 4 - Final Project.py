import os, random, ASCII_Art, WordList
os.system("cls")

isPlayerGuessCorrect = False
livesLeft = len(ASCII_Art.stages) - 1
chosenWord = random.choice(WordList.words)
chosenWordDisplay = []

# Create list filled with blanks that will represent hidden word
for _ in chosenWord:
    chosenWordDisplay += "_"

# Loop until all blanks are filled, main game loop
while "_" in chosenWordDisplay:
    playerGuess = input("Guess a letter: ").lower()
    for index, letter in enumerate(chosenWord):
        if playerGuess == letter:
            isPlayerGuessCorrect = True
            chosenWordDisplay[index] = playerGuess
    if isPlayerGuessCorrect == False:
        livesLeft -= 1
    isPlayerGuessCorrect = False
    if livesLeft == 0:
        os.system("cls")
        print("".join(chosenWordDisplay))
        print(ASCII_Art.stages[livesLeft])
        print(f"You Lose!\nCorrect word was: {chosenWord}\n")
        exit()
    else:
        os.system("cls")
        print("".join(chosenWordDisplay))
        print(ASCII_Art.stages[livesLeft])

print("You Win!\n")