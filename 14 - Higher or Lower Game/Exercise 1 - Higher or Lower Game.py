import os
import random
import inquirer
import art
import game_data

def clear_screen():
    """Clears the console."""
    os.system("cls")

def print_good_bye():
    clear_screen()
    print(art.logo)
    print("Thank You for playing!\n")

def ask_question(question : str, answers : list) -> str:
    question = inquirer.List('decision',
        message = question,
        choices = answers,
        )
    answer_dict : dict[str, str] = inquirer.prompt([question])
    answer = answer_dict["decision"]
    return answer

def select_random_item() -> dict:
    item = random.choice(game_data.data)
    return item

def select_until_different(item_1 : dict, item_2 : dict) -> dict:
    while item_1 == item_2:
        item_2 = select_random_item()
    return item_2

def print_user_display(score : int, item_in_game : dict, new_item : dict):
    clear_screen()
    print(art.logo)
    print(f"Score: {score}\n")
    print(f"{item_in_game['name']} is {item_in_game['description']}"
            f", from {item_in_game['country']}.")
    print(art.vs)
    print(f"{new_item['name']} is {new_item['description']}"
            f", from {new_item['country']}.\n") 

def check_who_has_more_followers(item_1 : dict, item_2 : dict) -> dict:
    if item_1["follower_count"] > item_2["follower_count"]:
        return item_1
    else:
        return item_2

def keep_playing() -> bool:
    answer = ask_question(
        question= "Would You like to start a new game?: ",
        answers= ["Yes", "No"])
    if answer == "Yes":
        return True
    else:
        return False

def game():
    score = 0
    user_win = True
    item_in_game = select_random_item()
    new_item = select_random_item()
    
    while user_win:
        new_item = select_until_different(
            item_1= item_in_game,
            item_2= new_item)
        winning_item = check_who_has_more_followers(
            item_1= item_in_game,
            item_2= new_item)
        
        print_user_display(score= score,
                           item_in_game= item_in_game,
                           new_item= new_item)
        
        user_guess = ask_question(
            question= f"Who has more followers?: ",
            answers= [item_in_game["name"],
                      new_item["name"]])
        
        if user_guess == winning_item["name"]:
            score += 1
            item_in_game = new_item
        else:
            print(f"Correct answer was {winning_item['name']}\n")
            user_win = False

clear_screen()
print(art.logo)
while keep_playing():
    game()
print_good_bye()
