import os
import random
import inquirer
import art
import game_data


def clear_screen():
    """Clears the console."""

    os.system("cls")


def ask_question(question: str, answers: list) -> str:
    """Prompts string to user and let them select from list
       of string answers then returns string chosen by the user.

    Args:
        question (str): question that will be prompted to user "question"

        answers (list): answers that user can choose from ["answer1", "answer2"]

    Returns:
        str: answer that was chosen by the user from the list of answers.
    """

    question = inquirer.List(
        "decision",
        message=question,
        choices=answers,
    )
    answer_dict: dict[str, str] = inquirer.prompt([question])
    answer = answer_dict["decision"]
    return answer


def print_user_display(score: int, item_in_game: dict, new_item: dict):

    clear_screen()
    print(art.logo)
    print(f"Score: {score}\n")
    print(
        f"{item_in_game['name']} is {item_in_game['description']}"
        f", from {item_in_game['country']}."
    )
    print(art.vs)
    print(
        f"{new_item['name']} is {new_item['description']}"
        f", from {new_item['country']}.\n"
    )


def game():
    """Main Game Loop"""

    score = 0
    did_user_win = True
    item_in_game = random.choice(game_data.data)
    new_item = random.choice(game_data.data)

    while did_user_win:
        # Select new item if both items are the same
        while new_item == item_in_game:
            new_item = random.choice(game_data.data)

        # Find the winning item
        if item_in_game["follower_count"] > new_item["follower_count"]:
            item_with_more_followers = item_in_game
        else:
            item_with_more_followers = new_item

        print_user_display(
            score=score, item_in_game=item_in_game, new_item=new_item)

        # User makes a guess
        user_guess = ask_question(
            question="Who has more followers?: ",
            answers=[item_in_game["name"], new_item["name"]],
        )

        # If user answers correctly continue playing, else quit the game
        if user_guess == item_with_more_followers["name"]:
            score += 1
            item_in_game = new_item
        else:
            print(f"Correct answer was {item_with_more_followers['name']}\n")
            did_user_win = False


clear_screen()
print(art.logo)
while ask_question(question="Would you like to start a new game?: ",
                   answers=["Yes", "No"]) == "Yes":
    game()
print("Thank You for playing!\n")
