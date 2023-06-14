import turtle
import random


class GameSettings:

    def __init__(self) -> None:

        self.game_title = "Snake Game!"

        self.window_width = 600
        self.window_height = 600

        self.colormode = 255

        self.step_speed = 2
        self.frame_delay_ms = 10

        self.angle = 1
        self.angle_max = 15
        self.angle_increment = 0.5

        self.food_shape = "circle"
        self.food_shape_size = 1.5
        self.food_color = "red"

        self.snake_shape = "circle"
        self.snake_shape_size = 2
        self.snake_line_size = 3

        self.snake_stamp_clock = 0
        self.snake_stamp_reset = 16


class SnakeGame:

    def __init__(self) -> None:

        self.settings = GameSettings()
        self.keys_pressed = set("u")
        self.actions = {
            "u": lambda: self.snake.forward(self.settings.step_speed),
            "l": lambda: self.snake.left(self.settings.angle),
            "r": lambda: self.snake.right(self.settings.angle),
        }

        self.food = turtle.Turtle()
        self.starting_food_settings()
        self.food_exists = False

        self.snake = turtle.Turtle()
        self.starting_snake_settings()

        self.screen = turtle.Screen()
        self.screen.tracer(0)
        self.screen.setup(self.settings.window_width,
                          self.settings.window_height)
        self.screen.title(f"{self.settings.game_title}    "
                          f"Score: {self.snake_len}")
        self.screen.colormode(self.settings.colormode)


    def starting_snake_settings(self):

        line_size = self.settings.snake_line_size
        shape_size = self.settings.snake_shape_size
        self.snake_num_of_stamps = 0
        self.snake_len = 0
        self.snake.shape(self.settings.snake_shape)
        self.snake.pensize(line_size)
        self.snake.shapesize(shape_size, shape_size)
        self.snake.penup()


    def starting_food_settings(self):

        self.food.hideturtle()
        self.food.shape(self.settings.food_shape)
        self.food.shapesize(self.settings.food_shape_size)
        self.food.color(self.settings.food_color)
        self.food.penup()


    def spawn_food(self):

        self.food.showturtle()
        if not self.food_exists:
            random_x = random.randint((self.settings.window_width / -2),
                                      (self.settings.window_width / 2))
            random_y = random.randint((self.settings.window_height / -2),
                                      (self.settings.window_height / 2))
            self.food.goto((random_x, random_y))
            self.food_exists = True


    def snake_keep_length(self):

        if self.snake_num_of_stamps > self.snake_len:
            self.snake_num_of_stamps -= 1
            self.snake.clearstamps(1)


    def snake_stamp(self):

        if self.settings.snake_stamp_clock < self.settings.snake_stamp_reset:
            self.settings.snake_stamp_clock += 1
        else:
            self.snake.stamp()
            self.snake_num_of_stamps += 1
            self.settings.snake_stamp_clock = 0


    def snake_eat(self):

        #snake_position_x = self.snake.position()
        #snake_position_y = list(self.snake.position()[1])
        food_position_x = (self.food.position()[0] - 30, self.food.position()[0] + 30)
        food_position_y = (self.food.position()[1] - 30, self.food.position()[1] + 30)

        if self.food_exists:
            if self.snake.position()[0] > food_position_x[0]:
                if self.snake.position()[0] < food_position_x[1]:
                    if self.snake.position()[1] > food_position_y[0]:
                        if self.snake.position()[1] < food_position_y[1]:
                            self.snake_len += 1
                            print(self.snake_len)
                            self.food_exists = False
                            self.spawn_food()

        #print(food_position_x)


    def change_color(self):

        red = random.randint(0, 255)
        green = random.randint(0, 255)
        blue = random.randint(0, 255)
        new_color = (red, green, blue)
        self.snake.color(new_color)


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
        self.starting_snake_settings()


    def user_input(self):

        #self.screen.onkeypress(lambda: self.keys_pressed.add("u"), "Up")
        self.screen.onkeypress(lambda: self.keys_pressed.add("l"), "Left")
        self.screen.onkeypress(lambda: self.keys_pressed.add("r"), "Right")

        #self.screen.onkeyrelease(lambda: self.keys_pressed.remove("u"), "Up")
        self.screen.onkeyrelease(lambda: self.keys_pressed.remove("l"), "Left")
        self.screen.onkeyrelease(lambda: self.keys_pressed.remove("r"), "Right")

        self.screen.onkey(fun=self.clear_screen, key="e")
        self.screen.onkey(fun=self.change_color, key="f")


    def tick(self):

        self.handle_keys_pressed()
        self.handle_angle_speed()
        self.spawn_food()
        self.snake_eat()
        self.snake_stamp()
        self.snake_keep_length()
        #print(self.food.position())
        self.screen.update()
        self.screen.ontimer(fun=self.tick, t=self.settings.frame_delay_ms)


    def main(self):

        self.user_input()
        self.screen.listen()
        self.tick()
        self.screen.exitonclick()


snake_game = SnakeGame()
snake_game.main()
