import turtle
from car import Car
import random
from player import Player
from scoreboard import Scoreboard


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
    global tickrate_delay
    tickrate_delay = 100000
    print("Game Over!")


def player_reached_finish():
    if player.reached_finish():
        global car_speed
        player.reset_pos()
        scoreboard.increase_score()
        car_speed += 0.2


def update_screen():
    create_car()
    update_cars()
    delete_car()
    player.update_pos()
    player_reached_finish()
    check_collision()
    screen.update()
    screen.ontimer(fun=update_screen, t=tickrate_delay)


tickrate_delay = 10
screen = turtle.Screen()
screen.tracer(0)
screen.setup(width=600, height=600)
screen.listen()

car_speed = 1.5
list_of_cars = []
player = Player(screen)
scoreboard = Scoreboard()

update_screen()
screen.mainloop()
