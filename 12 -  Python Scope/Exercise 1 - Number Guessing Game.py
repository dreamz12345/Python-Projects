import os
import random
import inquirer

def clear_screen():
    """Clears the console."""
    os.system("cls")

def print_welcome():
    print("Welcome to the Number Guessing Game!\n")

def print_good_bye():
    print("Thank You for playing!\n")

def player_guess_number() -> int:
    guess = int(input("\nGuess the number: "))
    return guess

def ask_question(question : str, answers : list) -> str:
    question = inquirer.List('decision',
        message = question,
        choices = answers,
        )
    answer_dict : dict[str, str] = inquirer.prompt([question])
    answer = answer_dict["decision"]
    return answer

def choose_game_mode() -> int:
    mode = ask_question(question= "What mode would you like to play?: ",
                        answers= ["Easy - 10 attempts.", "Hard - 5 attempts."],
                        )
    if mode == "Easy - 10 attempts.":
        attempts_left = EASY_MODE_ATTEMPTS
    elif mode == "Hard - 5 attempts.":
        attempts_left = HARD_MODE_ATTEMPTS
    return attempts_left

def print_player_status(list_of_player_guesses: list,
                        attempts_left : int,
                        hidden_number : int):
    clear_screen()
    print(f"Guess the number in between "
          f"{LOWEST_HIDDEN_NUMBER} and {HIGHEST_HIDDEN_NUMBER}\n")
    
    print(f"You have {attempts_left} attempts left.\n")
    for guess in list_of_player_guesses:
        if guess < hidden_number:
            print(f"{guess} - Too low.")
        elif guess == hidden_number:
            print("---Hidden Number---")
        elif guess > hidden_number:
            print(f"{guess} - Too high.")

def game():
    list_of_player_guesses = []
    attempts_left = choose_game_mode()
    hidden_number = random.randint(LOWEST_HIDDEN_NUMBER,
                                   HIGHEST_HIDDEN_NUMBER)
    
    # Append hidden_number to list_of_player_guesses to display it later on as
    # ---Hidden Number--- in between of player guesses
    list_of_player_guesses.append(hidden_number)
    
    clear_screen()
    print_player_status(list_of_player_guesses= list_of_player_guesses,
                        attempts_left= attempts_left,
                        hidden_number= hidden_number)

    while attempts_left > 0:
        player_guess = player_guess_number()
        if player_guess == hidden_number:
            print("\nThats the correct number!\nYou Win!\n")
            break
        attempts_left -= 1
        list_of_player_guesses.append(player_guess)
        list_of_player_guesses.sort()
        print_player_status(list_of_player_guesses= list_of_player_guesses,
                            attempts_left= attempts_left,
                            hidden_number= hidden_number)
        if attempts_left == 0:
            print(f"\nCorrect number was: {hidden_number}\nYou Lose!\n")

LOWEST_HIDDEN_NUMBER = 1
HIGHEST_HIDDEN_NUMBER = 100
EASY_MODE_ATTEMPTS = 10
HARD_MODE_ATTEMPTS = 5
play_again = "Yes"

clear_screen()
print_welcome()

while play_again == "Yes":
    game()
    play_again = ask_question(question= "Would you like to play again? ",
                              answers= ["Yes", "No"]
                              )
    if play_again == "Yes":
        clear_screen()
print_good_bye()
