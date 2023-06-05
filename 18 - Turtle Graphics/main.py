import colorgram
import turtle
import random
import os


def random_color(color_pallete : list) -> tuple:

    chosen_color = random.choice(color_pallete)
    color = chosen_color.rgb
    return color


def clear_screen():

    os.system("cls")


clear_screen()
print("Welcome to program that paints dots based on your color palette!")
jpg_link = input("Please put a link to the picture, "
                 "to extract color palette from it:\n")
colors = colorgram.extract(jpg_link, 6)

dot_size = int(input("Please enter Dot Size(5 - 30): "))
number_of_dots = int(input("Please enter Number of Dots (5 - 30): "))

dot_spacing = dot_size * 2 
screen_size_ur = number_of_dots * dot_spacing + dot_size * 2

x_coordinates = dot_spacing
y_coordinates = dot_spacing
window_width_res = 820
window_height_res = 820

screen = turtle.Screen()
screen.setup(window_width_res, window_height_res)
screen.setworldcoordinates(0, 0, screen_size_ur, screen_size_ur)
screen.colormode(255)

brush = turtle.Turtle()
brush.hideturtle()
brush.speed('fastest')
brush.penup()
brush.setposition(x_coordinates, y_coordinates)

for _ in range(number_of_dots):

    for _ in range(number_of_dots):
        brush.dot(dot_size, random_color(colors))
        brush.forward(dot_spacing)

    y_coordinates += dot_spacing
    brush.setposition(x_coordinates, y_coordinates)

screen.exitonclick()
