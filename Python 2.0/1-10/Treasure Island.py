import os
import random

def clear_terminal():
    # Clear command for Windows or Unix-based systems
    os.system('cls' if os.name == 'nt' else 'clear')


ASCII_ART = print("""
             _.--.
         _.-'_:-'||
     _.-'_.-::::'||
._.-:'_.-::::::'  ||
.'`-.-:::::::'     ||
/.'`;|:::::::'      |__
||   |::::::'     _.;._'-._
||   |:::::'  _.-!oo @.!-._'-.
\\'. |:::::.-!()oo @!()@.-'_.|
 '.'-;|:.-'.&$@.& ()$%-'o.'\\|
   `>'-.!@%()@'@_%-'_.-o _.|' 
    |.-._'-.@.-'_.-' _.-o  |' 
    |=| '-._.-' '-._    o |'     
    | '-.]=|   | |      o |'  
    |      |   | |        _| '
    |      |   | |    _.-'_.-'
    '-._   |   | |_.-'_.-'
     '-._'-|   | `_.-'
          '-|__/.-'   
""")


if __name__ == "__main__":

    clear_terminal()
    print("Welcome to Treasure Island!")
    print(ASCII_ART)
    print("Your mission is to find the treasure.")


    hp = 100
    Treasures = 0
    print(f"Your starting health is {hp} HP.")
    print(f"You have {Treasures} treasures collected.")

    choice1 = input("Do you want to go left or right? (left/right): ").strip().lower()
    print()  # Empty line after choice

    if choice1 == "left":
        print("You encounter a wild beast!")
        action = input("Do you want to fight or run? (fight/run): ").strip().lower()
        print()  # Empty line after choice
        if action == "fight":
            hp -= 20
            print(f"You fought bravely! Your health is now {hp} HP.")
        else:
            print("You ran away safely.")
    
    elif choice1 == "right":
        print("You find a treasure chest!")
        action = input("Do you want to open it? (yes/no): ").strip().lower()
        print()  # Empty line after choice
        if action == "yes":
            Treasures += 10
            print(f"You found a treasure! Total treasures: {Treasures}")
        else:
            print("You decided to leave the treasure chest alone.")

    choice2 = input("Do you want to continue exploring or go back? (explore/back): ").strip().lower()
    print()  # Empty line after choice

    if choice2 == "explore":
        print("You find a hidden cave with more treasures!")
        print("You bravely enter the cave. and face more challenges.")
        print("You encounter a guardian of the cave! Its eyes glow in the dark.")
        action = input("Do you want to fight the guardian or sneak past it? (fight/sneak): ").strip().lower()
        print()  # Empty line after choice
        if action == "fight":
            hp -= random.randint(10, 100)
            if hp <= 0:
                print("You fought valiantly but lost all your health. Game over!")
                exit()
            else:
                Treasures += random.randint(5, 20)
                print(f"You defeated the guardian! Your health is now {hp} HP and you collected more treasures.")
        elif action == "sneak":
            print("You successfully sneaked past the guardian and found more treasures!")
            Treasures += random.randint(5, 20)

    else:
        print("You safely returned back.")
    
    print(f"Your final health is {hp} HP.")
    print(f"You collected a total of {Treasures} treasures.")

    print("Congratulations! You completed the Treasure Island adventure!")
    print("Thank you for playing!")

