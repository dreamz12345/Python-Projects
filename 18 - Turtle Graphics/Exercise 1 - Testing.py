import turtle
import random

def random_walk(moving_object : turtle.Turtle):

    moving_object.setheading(random.choice([0, 90, 180, 270]))
    moving_object.forward(20)


def set_random_color(moving_object : turtle.Turtle):

    red = random.randint(0, 255)
    green = random.randint(0, 255)
    blue = random.randint(0, 255)
    moving_object.color(red, green, blue)


turtle_1 = turtle.Turtle()
turtle_1.pensize(2)
screen = turtle.Screen()
screen.colormode(255)
turtle_1.speed("fastest")

SIZE_OF_CIRCLE = 100
SIZE_OF_GAP = 5
for _ in range(int(360 / SIZE_OF_GAP)):

    set_random_color(turtle_1)
    turtle_1.left(SIZE_OF_GAP)
    turtle_1.circle(SIZE_OF_CIRCLE)


# for angle in range(36):

#     turtle_1.penup()
#     turtle_1.forward(30)
#     turtle_1.left(10)
#     turtle_1.pendown()


# NUM_OF_FIGURES = 7
# num_of_corners = 3

# for figure in range(NUM_OF_FIGURES):

#     r = random.randint(0, 255)
#     g = random.randint(0, 255)
#     b = random.randint(0, 255)
#     turtle_1.color(r, g, b)

#     angle = 360 / num_of_corners
 
#     for _ in range(num_of_corners):
#         turtle_1.forward(100)
#         turtle_1.left(angle)

#     num_of_corners += 1

# for _ in range(150):
#     turtle_random_color(turtle_1)
#     random_walk(turtle_1)

screen.exitonclick()
