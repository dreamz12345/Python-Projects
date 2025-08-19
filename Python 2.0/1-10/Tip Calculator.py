import os

def check_if_num_is_int(number):
    try:
        return int(number)
    except ValueError:
        print("That was not a valid number.")
        return None

def check_if_num_is_float(number):
    try:
        return float(number)
    except ValueError:
        print("That was not a valid number.")
        return None

def prompt_until_valid(prompt, check_function):
    while True:
        user_input = input(prompt)
        valid_input = check_function(user_input)
        if valid_input is not None:
            return valid_input

os.system('cls' if os.name == 'nt' else 'clear')

print("Welcome to the Tip Calculator!\n")

bill = prompt_until_valid("What was the total bill amount? $", check_if_num_is_float)
tip_percentage = prompt_until_valid("What percentage tip would you like to give? (0-100): ", check_if_num_is_int)
amount_people = prompt_until_valid("How many people to split the bill? ", check_if_num_is_int)

tip_amount = bill * (tip_percentage / 100)
total_bill = bill + tip_amount
amount_per_person = total_bill / amount_people

print(f"\nTotal bill amount: ${total_bill:.2f}")
print(f"Tip amount: ${tip_amount:.2f}")
print(f"Each person should pay: ${amount_per_person:.2f}")
print("\nThank you for using the Tip Calculator!\n")

