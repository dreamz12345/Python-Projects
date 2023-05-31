import os
import inquirer
from prettytable import PrettyTable
from menu import Menu
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine


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


def user_input() -> str:
    """Let the user select one of Coffees or enter Service Mode.

    Returns:
        str: Coffee selected by the user. (or Service Mode)
    """

    user_choice = ask_question(
        question="What would you like to buy? ",
        answers=["Latte", "Espresso", "Cappuccino", "Service Mode"])
    return user_choice.lower()


def print_menu():
    user_menu_display = PrettyTable()
    user_menu_display.field_names = ["Coffee", "Price"]
    for item in new_menu.menu:
        menu_print = [item.name.title(), f"{item.cost:.2f} $"]
        user_menu_display.add_row(menu_print)
    print(f"{user_menu_display}\n")


def service_mode():
    """Enter Service Mode.

    User can enter commands to access special
    functionality of Coffee Machine.

    'off' - To turn off the Coffee Machine

    'report' - To get the report of resources and earned money
    """

    clear_screen()
    service_mode_choice = input("Please enter the command: ").lower()
    if service_mode_choice == "off":
        print("\nTurning off the machine.\n")
        exit()
    elif service_mode_choice == "report":
        print("")
        coffee_maker.report()
        money_machine.report()
    else:
        print("\nWrong input.")


def get_money_from_user(coffee : str) -> float:
    """Prints coffee selected by the user and sum of coins inserted by the user.
    Prompts 4 possible coins that user can insert to the machine.
    Sums all coins inserted by the user.

    Args:
        coffee (str): Coffee selected by the user.

    Returns:
        float: Sum of coins inserted by the user.
    """

    coin = None
    coins_inserted = 0
    while coin != "Done":
        clear_screen()
        print(f"Chosen Coffee: {coffee.title()} - $"
              f"{new_menu.find_drink(coffee).cost}")
        print(f"Money inserted = ${coins_inserted:.2f}\n")
        coin = ask_question(
            question="Please insert coins: ",
            answers=["Quarter = $0.25",
                    "Dime = $0.10",
                    "Nickel = $0.05",
                    "Penny = $0.01",
                    "Done"]
        )
        if coin != "Done":
            coins_inserted += float(coin[-4:])
    return coins_inserted



coffee_maker = CoffeeMaker()
new_menu = Menu()
money_machine = MoneyMachine()

while True:
    clear_screen()
    print("Welcome to Coffee Machine!\n")
    print_menu()
    coffee_name = user_input()
    if coffee_name == "service mode":
        service_mode()
        input("\nPress Enter to continue.")
        continue
    chosen_coffee = new_menu.find_drink(coffee_name)
    enough_resources = coffee_maker.is_resource_sufficient(chosen_coffee)
    if not enough_resources:
        input("\nPress Enter to continue.")
        continue
    money_machine.money_received = get_money_from_user(coffee_name)
    enough_money = money_machine.make_payment(chosen_coffee.cost)
    if not enough_money:
        input("\nPress Enter to continue.")
        continue
    coffee_maker.make_coffee(chosen_coffee)
    input("\nPress Enter to continue.")
