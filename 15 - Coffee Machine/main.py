"""Program that simulates Coffee Machine.

User can choose from list of Coffees and then
inserts money. If user inserted enough money Coffee Machine makes Coffee and
gives back change to the user.

User can access Service Mode and turn 'off' the machine or get the 'report' of
- resources remaining inside the machine
- money collected from sales
"""


import os
import inquirer
import resources


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
        answers=["Espresso", "Latte", "Cappuccino", "Service Mode"])
    return user_choice.lower()


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
        print_report()
    else:
        print("\nWrong input.")


def print_welcome():
    """Prints welcome message to the user."""

    print("Welcome to the Coffee Machine!\n")


def print_menu():
    """Prints coffee machine menu from resources file."""

    for coffee, coffee_info in resources.MENU.items():
        print(f"{coffee.title()} - ${coffee_info['cost']}")
    print("")


def enough_resources(coffee : str) -> bool:
    """Checks if there is enough ingredients in the coffee machine,
    to prepare coffee, that was selected by the user. If theres is not
    enough ingredients, prints missing ingredient.

    Args:
        coffee (str): coffee selected by the user

    Returns:
        bool: True if enough resources to prepare coffee
    """

    enough_resources_in_machine = True
    coffee_ingredients = resources.MENU[coffee]["ingredients"]
    for ingredient in coffee_ingredients:
        if resources.resources[ingredient] < coffee_ingredients[ingredient]:
            enough_resources_in_machine = False
            print(f"Sorry there is not enough {ingredient}.")
    return enough_resources_in_machine


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
              f"{resources.MENU[coffee]['cost']}")
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


def enough_money(money : float, coffee : str) -> bool:
    """Checks if user inserted enough money to buy selected coffee.

    Args:
        money (float): Amount of money inserted by the user.
        coffee (str): Coffee selected by the user.

    Returns:
        bool: True if user inserted enough money. else: False
    """

    if money < resources.MENU[coffee]["cost"]:
        print("Sorry, there is not enough money.\nMoney refunded.")
        return False
    return True


def process_money(money : float, coffee : str) -> float:
    """Calculates the change that coffee machine should give back
    to the user. If there's money to be refunded, refunds money, then
    returns the amount of money paid for the coffee.

    Args:
        money (float): Amount of money inserted by the user.
        coffee (str): Coffee chosen by the user.

    Returns:
        float: Money paid for the coffee.
    """

    change_to_give_back = money - resources.MENU[coffee]["cost"]
    if change_to_give_back != 0:
        print(f"Here is ${change_to_give_back:.2f} dollars in change.")
    return resources.MENU[coffee]["cost"]


def print_report():
    """Prints collected money and how much 
    resources left in the Coffee Machine"""

    print(f"\nMoney in machine: ${money_in_machine:.2f}\n")
    print("Resources left in the machine: \n")
    for key, value in resources.resources.items():
        print(f"{key.title()}: {value}")


def make_coffee(coffee : str):
    """Make coffee for the user, then reduce the amount of resources
    inside the machine, by the amount of resources used for making that coffee.

    Args:
        coffee (str): Coffee chosen by the user.
    """

    coffee_ingredients = resources.MENU[coffee]["ingredients"]
    for ingredient in coffee_ingredients:
        resources.resources[ingredient] -= coffee_ingredients[ingredient]
    print(f"\nHere is your {coffee.title()}. Enjoy!")


def sell_coffee() -> float:
    """Sell coffee to the user or enter service mode.

    Returns:
        float: Money from successful sale.
    """

    clear_screen()
    print_welcome()
    print_menu()

    chosen_coffee = user_input()

    if chosen_coffee == "service mode":
        service_mode()
        return 0

    if not enough_resources(coffee=chosen_coffee):
        return 0

    user_money = get_money_from_user(coffee=chosen_coffee)

    if not enough_money(money=user_money, coffee=chosen_coffee):
        return 0

    profit_to_be_added = process_money(money=user_money, coffee=chosen_coffee)
    make_coffee(coffee=chosen_coffee)

    return profit_to_be_added



money_in_machine = 0

while True:
    money_in_machine += sell_coffee()
    input("\nPress enter to continue: ")
