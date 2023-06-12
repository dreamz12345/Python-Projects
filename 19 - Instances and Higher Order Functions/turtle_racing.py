import turtle
import random


class GameSettings:

    def __init__(self) -> None:

        self.game_title = "Turtle Racing"

        self.window_width = 600
        self.window_height = 600
        self.running_distance = 400

        self.frame_delay_ms = 10

        self.colors = ["red", "green", "blue", "gold", "purple"]

        self.num_of_turtles = 4 #Max 5 turtles
        self.turtle_shape = "turtle"
        self.turtle_shape_size = 1
        self.turtle_line_size = 3
        self.spacing = self.window_height / (self.num_of_turtles + 1)


class TurtleRacing:

    def __init__(self) -> None:

        self.winner = None
        self.settings = GameSettings()
        self.screen = turtle.Screen()
        self.screen.title(self.settings.game_title)
        window_width = self.settings.window_width
        window_height = self.settings.window_height
        self.screen.setup(window_width, window_height)
        self.screen.tracer(0)
        self.create_turtles()
        self.draw_line("start")
        self.draw_line("finish")


    def create_turtles(self):

        self.turtles = []
        for index in range(self.settings.num_of_turtles):
            new_turtle = turtle.Turtle()
            new_turtle.leapforward = 1
            new_turtle.color(self.settings.colors[index])
            new_turtle.shape(self.settings.turtle_shape)
            new_turtle.penup()
            self.turtles.append(new_turtle)


    def set_turtles(self):
        """Set turtles at the starting position"""

        x = (self.settings.running_distance / 2) * (-1)
        y = (self.settings.window_height / (-2)) + self.settings.spacing
        ADJUST_TO_TURTLE_SIZE = 15
        x -= ADJUST_TO_TURTLE_SIZE
        for racing_turtle in self.turtles:
            racing_turtle.setposition(x, y)
            y += self.settings.spacing


    def draw_line(self, line="start"):

        if line == "start":
            inverter = -1
        else:
            inverter = 1

        working_turtle = turtle.Turtle()
        working_turtle.hideturtle()
        working_turtle.penup()
        FACE_NORTH = 90
        working_turtle.setheading(FACE_NORTH)

        x = self.settings.running_distance / 2
        y = self.settings.window_height / 2

        working_turtle.setposition(x * inverter, y * (-1))
        working_turtle.pendown()
        working_turtle.forward(self.settings.window_height)
        working_turtle.penup()


    def turtle_move_forward(self):

        for index, racing_turtle in enumerate(self.turtles):
            x = random.randint(1, 3)
            self.turtles[index].forward(racing_turtle.leapforward + x)


    def assing_random_speed(self):

        for racing_turtle in self.turtles:
            random_speed = random.randint(1, 5) * 0.1
            racing_turtle.leapforward = random_speed


    def tick(self):

        self.check_winner()
        self.turtle_move_forward()
        if not self.winner:
            self.screen.update()
            self.screen.ontimer(self.tick, self.settings.frame_delay_ms)


    def check_winner(self):

        for racing_turtle in self.turtles:
            if racing_turtle.xcor() > (self.settings.running_distance / 2) - 14:
                self.winner = racing_turtle
                print(self.winner.color())


    def main(self):

        self.set_turtles()
        self.assing_random_speed()
        self.tick()
        self.screen.exitonclick()


turtle_racing = TurtleRacing()
turtle_racing.main()
