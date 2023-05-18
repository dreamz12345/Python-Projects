import os
os.system("cls")

def add_bidder():
    name = input("What is your name?: ")
    bid = int(input("What is your bid?: $"))
    dict_of_bidder = {
        "name": name,
        "bid": bid,
    }
    return dict_of_bidder

def create_list_of_bidders():
    list_of_bidders = []
    more_bidders_left = True
    while more_bidders_left:
        list_of_bidders.append(add_bidder())
        should_continue = input("Is there more "
                                "bidders?('Y' or 'N'): ").lower()
        if should_continue == "n":
            more_bidders_left = False
        os.system("cls")
    return list_of_bidders

def find_highest_bidder(list_of_bidders):
    highest_bid = 0
    for bidder in list_of_bidders:
        if bidder["bid"] > highest_bid:
            highest_bid = bidder["bid"]
            highest_bidder = bidder
    return highest_bidder

def print_welcome():
    print("Welcome to the Secret Auction!\n\n"
          "Each bidder should make a bid in secret and then\n"
          "highest bidder will be revealed!\n")

def print_list_of_bidders(list_of_bidders):
    print("List of all bidders:")
    for bidder in list_of_bidders:
        print(f"{bidder['name']}: "
              f"${bidder['bid']}")
    print("")

def print_highest_bidder(list_of_bidders):
    highest_bidder = find_highest_bidder(list_of_bidders)
    print(f"Highest bidder was: {highest_bidder['name']}: "
      f"${highest_bidder['bid']}\n")


print_welcome()
list_of_bidders = create_list_of_bidders()
os.system("cls")
print_list_of_bidders(list_of_bidders)
print_highest_bidder(list_of_bidders)
