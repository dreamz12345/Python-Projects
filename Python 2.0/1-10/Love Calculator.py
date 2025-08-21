import os

def clear_terminal():
    os.system('cls' if os.name == 'nt' else 'clear')

if __name__ == "__main__":

    TRUE_LETTERS = ["t", "r", "u", "e"]
    LOVE_LETTERS = ["l", "o", "v", "e"]
    true_count = 0
    love_count = 0
    love_score = 0
    

    clear_terminal()
    print("Welcome to the Love Calculator!")
    
    name1 = input("What is your name? ")
    name2 = input("What is their name? ")

    combined_names = (name1 + name2).lower()
    combined_names_no_space = combined_names.replace(" ", "")
    
    for char in combined_names_no_space:
        if char in TRUE_LETTERS:
            true_count += 1
        if char in LOVE_LETTERS:
            love_count += 1
    
    love_score = str(true_count) + str(love_count)
    print(f"Your love score is: {love_score}")
