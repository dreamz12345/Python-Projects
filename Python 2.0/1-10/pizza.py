import os

def clear_terminal():
    # Clear command for Windows or Unix-based systems
    os.system('cls' if os.name == 'nt' else 'clear')

class pizza:
    def __init__(self):
        self.S_PIZZA_PRICE = 15.00
        self.M_PIZZA_PRICE = 20.00
        self.L_PIZZA_PRICE = 25.00
        self.S_PEPPERONI_PRICE = 2.00
        self.M_PEPPERONI_PRICE = 3.00
        self.L_PEPPERONI_PRICE = 3.00
        self.EXTRA_CHEESE_PRICE = 1.00

        self.total_price = 0.00
        self.size = None
        self.pepperoni = False
        self.extra_cheese = False

    def user_input(self):
        self.size = input("Choose pizza size (S/M/L): ").strip().upper()
        if (input("Add pepperoni? (yes/no): ").strip().lower()) == 'yes':
            self.pepperoni = True
        if (input("Add extra cheese? (yes/no): ").strip().lower()) == 'yes':
            self.extra_cheese = True
        

    def order_pizza(self):
        if self.size == 'S':
            self.total_price = self.S_PIZZA_PRICE
            if self.pepperoni:
                self.total_price += self.S_PEPPERONI_PRICE
        elif self.size == 'M':
            self.total_price = self.M_PIZZA_PRICE
            if self.pepperoni:
                self.total_price += self.M_PEPPERONI_PRICE
        elif self.size == 'L':
            self.total_price = self.L_PIZZA_PRICE
            if self.pepperoni:
                self.total_price += self.L_PEPPERONI_PRICE
        else:
            print("Invalid size selected. Please choose S, M, or L.")
            return
        if self.extra_cheese:
            self.total_price += self.EXTRA_CHEESE_PRICE

        
    def print_total_price(self):
        print(f"Total price for your pizza: ${self.total_price:.2f}")

# Main execution
if __name__ == "__main__":
    clear_terminal()

    print("Welcome to the Pizza Ordering System!\n")
    print("Please follow the prompts to order your pizza.\n")

    calc_pizza = pizza()
    calc_pizza.user_input()
    calc_pizza.order_pizza()
    calc_pizza.print_total_price()
    
    print("\nThank you for your order!")


