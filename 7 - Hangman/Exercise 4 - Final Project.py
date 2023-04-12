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

    # Search for player chosen letter in hidden word
    # if letter found fill blank with letter
    for index, letter in enumerate(chosenWord):
        if playerGuess == letter:
            isPlayerGuessCorrect = True
            chosenWordDisplay[index] = playerGuess

    # Reduce livesLeft if player didn't guess a letter
    if isPlayerGuessCorrect == False:
        livesLeft -= 1
    isPlayerGuessCorrect = False

    # If livesLeft == 0 end the game
    if livesLeft == 0:
        os.system("cls")
        # Show wordInProgress as string instead of list
        wordInProgress = ""
        wordInProgress = wordInProgress.join(chosenWordDisplay)
        print(f"Word to uncover: {wordInProgress}")
        print(ASCII_Art.stages[livesLeft])
        print(f"You Lose!\nCorrect word was: {chosenWord}\n")
        exit()

    # Print current player standing
    os.system("cls")
    # Show wordInProgress as string instead of list
    wordInProgress = ""
    wordInProgress = wordInProgress.join(chosenWordDisplay)
    print(f"Word to uncover: {wordInProgress}")
    print(ASCII_Art.stages[livesLeft])

# If out of while loop -> all blanks filled -> Player wins!
print("You Win!\n")