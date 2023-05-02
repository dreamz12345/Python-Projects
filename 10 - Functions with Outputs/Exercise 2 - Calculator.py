import os

def clear_screen():
    """Clears the console."""
    os.system("cls")

def print_welcome():
    print("Welcome to the Calculator!\n")

def print_good_bye():
    print("\nThank You for using this Calculator!\n")

def calculate(number_1, operation, number_2):
    number_1 = float(number_1)
    number_2 = float(number_2)
    if operation == "+":
        total = number_1 + number_2
    elif operation == "-":
        total = number_1 - number_2
    elif operation == "*":
        total = number_1 * number_2
    elif operation == "/":
        total = number_1 / number_2
    return total

def create_user_display_list():
    if user_input[0] == "c":
        user_display_list.clear()
    elif old_total == None:
        user_display = " ".join(user_input) + " = " + str(total)
        user_display_list.append(user_display)
    else:
        user_display = str(old_total) + " " + " ".join(user_input) + " = " + str(total)
        user_display_list.append(user_display)
    return user_display_list

def print_user_display():
    clear_screen()
    print_user_options(total)
    if user_display_list == []:
        print("Total = 0")
    else:
        for equation in user_display_list:
            print(f"{equation}")
        print(f"\nTotal = {total}")

def print_user_options(total):
    print("'C' to clear Calculator.")
    print("'X' to exit Calculator.")
    print("Available operators - '+', '-', '*', '/'")
    if total == None:
        print("'number operator number' To calculate.\n")
    else:
        print("'operator number' To calculate.\n")

def get_user_input():
    user_input = input("").lower()
    user_input = user_input.split(" ")
    return user_input

def calc(user_input, total):
    if user_input[0] == "x":
        print_good_bye()
        exit()
    elif user_input [0] == "c":
        total = None
        return total
    elif total == None:
        total = calculate(number_1= user_input[0],
                          operation= user_input[1],
                          number_2= user_input[2])
        return total
    else:
        total = calculate(number_1= total,
                          operation= user_input[0],
                          number_2= user_input[1])
        return total


total = None
old_total = None
user_display_list = []

clear_screen()
print_welcome()
print_user_options(total)
print("Total = 0")

while True:
    user_input = get_user_input()
    total = calc(user_input, total)
    user_display_list = create_user_display_list()
    old_total = total
    print_user_display()
            