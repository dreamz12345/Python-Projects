import os
os.system("cls")

def create_list_of_cities():
    cities_still_to_be_added = True
    list_of_cities = []
    while cities_still_to_be_added:
        city = input("Which city did you vist?: ")
        list_of_cities.append(city)
        continue_adding = input("Would you like to "
                                "add more cities?('Y' or 'N'): ").lower()
        if continue_adding == "n":
            cities_still_to_be_added = False
    return list_of_cities

def add_travel():
    country = input("What country did you visit?: ")
    visits = int(input("How many times did you visit this country?: "))
    cities = create_list_of_cities()
    travel = {
        "country": country,
        "visits": visits,
        "cities": cities,
    }
    return travel

def create_list_of_travels():
    travels_still_to_be_added = True
    list_of_travels = []
    while travels_still_to_be_added:
        list_of_travels.append(add_travel())
        continue_adding = input("Would you like to "
                                "add more travels?('Y' or 'N'): ").lower()
        if continue_adding == "n":
            travels_still_to_be_added = False
    return list_of_travels


travel_log = create_list_of_travels()
print(travel_log)
