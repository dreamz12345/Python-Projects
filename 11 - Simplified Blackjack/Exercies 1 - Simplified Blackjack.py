import os
import random
import inquirer


MAX_SCORE = 21

def clear_screen():
    """Clears the console."""
    os.system("cls")

def print_welcome():
    print("Welcome to the Blackjack game!\n")

def print_good_bye():
    print("\nThank You for playing!\n")

def print_players_scores(current_player = None, determine_winners = False):
    for player in players:
        current_player_indicator = ""
        player_info = ""
        player_score = players[player]
        dealer_score = players["Dealer"]
        if player == current_player:
            current_player_indicator = "--->"
        if player_score > MAX_SCORE:
            player_info = "- Bust"
        elif determine_winners == True:
            if player_score == dealer_score:
                if player != "Dealer":
                    player_info = "- Draw"
            elif player_score > dealer_score:
                player_info = "- Win"
            else:
                player_info = "- Lose"

        message = f"{current_player_indicator}{player}: "
        message += f"{player_score} {player_info}"
        print(message)
    print("")


def print_current_player(player):
    print(f"{player}: {players[player]}")

def add_players():
    add_more_players = True
    while add_more_players:
        name = input("What is your name?: ")
        score = 0
        players[name] = score
        add_more_players = ask_yes_no_question("Do you want to "
                                               "add more players?")
    add_dealer()

def ask_yes_no_question(question : str) -> bool:
    question = inquirer.List('decision',
        message = question,
        choices = ['Yes', 'No'],
        )
    result_dict : dict[str, str] = inquirer.prompt([question])
    result = result_dict["decision"]
    return result == "Yes"

def add_dealer():
    name = "Dealer"
    score = 0
    players[name] = score

def deal_first_card():
    for player in players:
        card = random.choice(possible_cards)
        players[player] = card

def hit(player):
    ACE = 11
    card = random.choice(possible_cards)
    if card == ACE:
        if players[player] + ACE > MAX_SCORE:
            ACE = 1
            card = ACE
    return card

def check_if_bust(player):
    bust = False
    if players[player] > MAX_SCORE:
        bust = True
        return bust

def player_decision(player : str) -> str:
    question = inquirer.List('decision',
        message = f"What would you like to do {player}?",
        choices = ['Hit', 'Double Down', 'Pass'],
        )
    decision_dict : dict[str, str] = inquirer.prompt([question])
    decision = decision_dict["decision"].lower()
    return decision

def round():
    for player in players:
        while players[player] < MAX_SCORE:
            bust = False
            clear_screen()
            print_players_scores(player)
            decision = player_decision(player)
            if decision == "hit":
                players[player] += hit(player)
                bust = check_if_bust(player)
            if bust == True:
                break
            elif decision == "pass":
                break



possible_cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
players = {}


clear_screen()
print_welcome()
add_players()
clear_screen()
deal_first_card()
print_players_scores()
round()
clear_screen()
print_players_scores(determine_winners= True)
print_good_bye()