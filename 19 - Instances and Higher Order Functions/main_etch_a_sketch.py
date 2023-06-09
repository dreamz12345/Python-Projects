import turtle
import random


class GameSettings:

    def __init__(self) -> None:

        self.game_title = "Etch-A-Sketch"

        self.window_width = 600
        self.window_height = 600

        self.colormode = 255

        self.step_speed = 3
        self.frame_delay_ms = 10

        self.angle = 1
        self.angle_max = 15
        self.angle_increment = 0.5

        self.brush_shape_size = 1
        self.brush_line_size = 3


class EtchASketch:

    def __init__(self) -> None:

        self.settings = GameSettings()
        self.keys_pressed = set()
        self.actions = {
            "u": lambda: self.brush.forward(self.settings.step_speed),
            "l": lambda: self.brush.left(self.settings.angle),
            "r": lambda: self.brush.right(self.settings.angle),
        }

        self.brush = turtle.Turtle()
        self.starting_pen_settings()

        self.screen = turtle.Screen()
        self.screen.title(self.settings.game_title)
        self.screen.colormode(self.settings.colormode)
        self.screen.tracer(0)
        self.screen.setup(self.settings.window_width, self.settings.window_height)


    def starting_pen_settings(self):

        line_size = self.settings.brush_line_size
        shape_size = self.settings.brush_shape_size
        self.brush.pensize(line_size)
        self.brush.shapesize(shape_size, shape_size)


    def change_color(self):

        red = random.randint(0, 255)
        green = random.randint(0, 255)
        blue = random.randint(0, 255)
        new_color = (red, green, blue)
        self.brush.color(new_color)


    def tick(self):

        self.handle_keys_pressed()
        self.handle_angle_speed()
        self.screen.update()
        self.screen.ontimer(fun=self.tick, t=self.settings.frame_delay_ms)


    def handle_keys_pressed(self):

        for action in self.keys_pressed:
            self.actions[action]()


    def handle_angle_speed(self):

        if "l" in self.keys_pressed or "r" in self.keys_pressed:
            if self.settings.angle < self.settings.angle_max:
                self.settings.angle += self.settings.angle_increment
        else:
            self.settings.angle = 1
    

    def clear_screen(self):

        self.screen.reset()
        self.starting_pen_settings()

    def user_input(self):

        self.screen.onkeypress(lambda: self.keys_pressed.add("u"), "Up")
        self.screen.onkeypress(lambda: self.keys_pressed.add("l"), "Left")
        self.screen.onkeypress(lambda: self.keys_pressed.add("r"), "Right")

        self.screen.onkeyrelease(lambda: self.keys_pressed.remove("u"), "Up")
        self.screen.onkeyrelease(lambda: self.keys_pressed.remove("l"), "Left")
        self.screen.onkeyrelease(lambda: self.keys_pressed.remove("r"), "Right")

        self.screen.onkey(fun=self.clear_screen, key="e")
        self.screen.onkey(fun=self.change_color, key="f")


    def main(self):

        self.user_input()
        self.screen.listen()
        self.tick()
        self.screen.exitonclick()


etch_a_sketch = EtchASketch()
etch_a_sketch.main()
