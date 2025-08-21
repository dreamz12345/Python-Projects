import random
import os

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j',
           'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z',
           'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J',
           'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '@', '#', '$', '%', '^', '&', '*', '+']

def generate_password(amount_of_letters=0, amount_of_numbers=0, amount_of_symbols=0):
    password_list = []

    for _ in range(amount_of_letters):
        password_list.append(random.choice(letters))
    for _ in range(amount_of_numbers):
        password_list.append(random.choice(numbers))
    for _ in range(amount_of_symbols):
        password_list.append(random.choice(symbols))

    random.shuffle(password_list)

    return ''.join(password_list)

def clear_terminal():
    os.system('cls' if os.name == 'nt' else 'clear')


if __name__ == "__main__":
    clear_terminal()
    print("Welcome to the Random Password Generator!")
    
    try:
        amount_of_letters = int(input("How many letters would you like in your password? "))
        amount_of_numbers = int(input("How many numbers would you like in your password? "))
        amount_of_symbols = int(input("How many symbols would you like in your password? "))
    except ValueError:
        print("Please enter valid numbers.")
        exit()

    password = generate_password(amount_of_letters, amount_of_numbers, amount_of_symbols)
    print(f"Your generated password is: {password}")