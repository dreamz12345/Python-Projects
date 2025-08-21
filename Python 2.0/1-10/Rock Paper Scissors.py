import random
import os

def evaluate_winner(player1, player2):
    winner = None
    if player1 == player2:
        winner = "tie"
    elif (player1 == "rock" and player2 == "scissors") or \
         (player1 == "scissors" and player2 == "paper") or \
         (player1 == "paper" and player2 == "rock"):
        winner = "Player 1"
    elif (player2 == "rock" and player1 == "scissors") or \
         (player2 == "scissors" and player1 == "paper") or \
         (player2 == "paper" and player1 == "rock"):
        winner = "Player 2"
    return winner


def play_against_computer():
    choices = ["rock", "paper", "scissors"]
    player2 = random.choice(choices)
    print(f"Computer chose: {player2}")
    return player2

def clear_terminal():
    os.system('cls' if os.name == 'nt' else 'clear')



if __name__ == "__main__":
    while True:
        clear_terminal()
        print("Welcome to Rock Paper Scissors!")
        mode = input("Choose mode: (1) Player vs Player (2) Player vs Computer: ").strip()
        if mode == '1':
            player1 = input("Player 1, enter your choice (rock, paper, scissors): ").strip().lower()
            player2 = input("Player 2, enter your choice (rock, paper, scissors): ").strip().lower()

        elif mode == '2':
            player1 = input("Player, enter your choice (rock, paper, scissors): ").strip().lower()
            player2 = play_against_computer()

        winner = evaluate_winner(player1, player2)

        if winner == "Player 1" or winner == "Player 2":
            if winner == "Player 2" and mode == '2':
                winner = "Computer"
            print(f"{winner} wins!")
        elif winner == "tie":
            print("It's a tie!")
        else:
            print("Invalid input. Please enter rock, paper, or scissors.")

        play_again = input("Do you want to play again? (yes/no): ").strip().lower()
        if play_again != 'yes':
            print("Thanks for playing!")
            break