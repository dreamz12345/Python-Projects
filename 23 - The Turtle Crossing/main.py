import turtle
from car import Car
import random
from player import Player


def update_cars():
    for car in list_of_cars:
        car: Car
        car.update_pos(car_speed)


def delete_car():
    for car in list_of_cars:
        car: Car
        if car.should_delete_car():
            car.hideturtle()
            list_of_cars.remove(car)


def create_car():
    # 3% chance to create a car
    random_num = random.randint(1, 100)
    if random_num > 97:
        list_of_cars.append(Car())


def check_collision():
    for car in list_of_cars:
        car: Car
        if player.is_collision_with_car(car):
            game_over()


def print_number_of_cars():
    number_of_cars = len(list_of_cars)
    print(f"033\[FNumber of Cars: {number_of_cars}")


def game_over():
    screen.bye()
    print("Game Over!")


def update_screen():
    create_car()
    update_cars()
    delete_car()
    player.update_pos()
    check_collision()
    screen.update()
    screen.ontimer(fun=update_screen, t=10)


screen = turtle.Screen()
screen.tracer(0)
screen.setup(width=600, height=600)
screen.listen()

car_speed = 1.5
list_of_cars = []
player = Player(screen)

update_screen()
screen.mainloop()
