import os
os.system("cls")

def prime_checker(number):
    is_prime_number = False
    number_of_clean_divisions = 0
    # Count how many times a number is divisible without remainder
    for divisor in range(1, number + 1):
        remainder = number % divisor
        if remainder == 0:
            number_of_clean_divisions += 1
    # if number was divided 2 times -> divided by 1 and by itself -> prime number
    if number_of_clean_divisions == 2:
        is_prime_number = True
    return is_prime_number

program_mode = input("Welcome to Prime Number Checker!\nWould you like to check"
      " 'specific' number or 'range' of numbers?: ").lower()

if program_mode == "specific":
    number = int(input("What number would you like to check?: "))
    is_prime_number = prime_checker(number)
    if is_prime_number == True:
        print(f"\n{number} - Is a Prime Number!\n")
    else:
        print(f"\n{number} - Is not a prime number.\n")

elif program_mode == "range":
    print_all_numbers = input("Would you like to print 'all' numbers "
                              "or just a 'list' of prime numbers?: ").lower()
    first_number = int(input("Write your first number: "))
    last_number = int(input("Write your last number: "))
    prime_numbers = []
    # Find all prime numbers in between first_number and last_number
    for number in range(first_number, last_number + 1):
        is_prime_number = prime_checker(number)
        if is_prime_number == True:
            prime_numbers.append(number)
            if print_all_numbers == "all":
                print(f"    {number} - Prime Number!")
        else:
            if print_all_numbers == "all":
                print(f"{number}")
        # Add empty lines every 10 loops for better readability
        if (number % 10) == 9 and print_all_numbers == "all":
            print("\n\n")
    print(f"\nAll of Prime Numbers found: {prime_numbers}\n")

