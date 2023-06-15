import turtle
import random
from enum import Enum
from typing import Set

class GameSettings:

    def __init__(self) -> None:



        self.angle = 1
        self.angle_max = 10
        self.angle_increment = 0.1

        self.food_shape = "circle"
        self.food_shape_size = 1.5
        self.food_hitbox_size = 30
        self.food_color = "red"

        self.snake_shape = "circle"
        self.snake_shape_size = 2
        self.snake_line_size = 3

        self.snake_stamp_clock = 0
        self.snake_stamp_reset = 16

class Arrow(Enum):
    LEFT = 0
    RIGHT = 1

class KeysPressed:

    keys_pressed : Set[Arrow] = None

    def __init__(self) -> None:
        self.keys_pressed = {}

    def press(self, arrow : Arrow):
        self.keys_pressed.add(arrow)

    def unpress(self, arrow : Arrow):
        self.keys_pressed.remove(arrow)

    def get_pressed(self) -> Set(Arrow):
        return  self.keys_pressed

class GameEngine:

    # Parameters

    GAME_TITLE : str = "Snake Game!"

    WINDOW_WIDTH : int = 600
    WINDOWS_HEIGHT : int = 600

    COLORMODE : int = 255

    STEP_SPEED : int = 2
    FRAME_DELAY_MS : int = 10

    # Fields

    turtle_screen : turtle._Screen = None
    keys_pressed : KeysPressed = None
    on_tick : callable(Set(Arrow)) = None
    on_clear : callable = None

    def __init__(self,
                 on_tick : callable,
                 on_clear : callable
                ) -> None:

        self.on_tick = on_tick
        self.on_clear = on_clear
        screen = turtle.Screen()
        screen.tracer(0)
        screen.setup(self.WINDOW_WIDTH, self.WINDOWS_HEIGHT)
        screen.title(self.GAME_TITLE)
        screen.colormode(self.COLORMODE)
        self.turtle_screen = screen
        self.keys_pressed = KeysPressed()

    def setup_key_events(self):

        keys = self.keys_pressed
        screen = self.turtle_screen

        screen.onkeypress(keys.press(Arrow.LEFT), "Left")
        screen.onkeypress(keys.press(Arrow.RIGHT), "Right")

        screen.onkeyrelease(keys.unpress(Arrow.LEFT), "Left")
        screen.onkeyrelease(keys.unpress(Arrow.RIGHT), "Right")

        screen.onkey(fun=self.handle_clear, key="e")

    def on_tick(self):
        self.on_tick(self.keys_pressed.get_pressed())
        self.turtle_screen.update()
        self.turtle_screen.ontimer(fun=self.on_tick, t=self.FRAME_DELAY_MS)

    def start_game(self):
        self.setup_key_events()
        self.on_tick()

    def handle_clear(self):
        if self.on_clear is not None:
            self.on_clear()

class SnakeGame:

    def __init__(self) -> None:

        self.s = GameSettings()
        
        self.actions = {
            "u": lambda: self.snake.forward(self.s.step_speed),
            "l": lambda: self.snake.left(self.s.angle),
            "r": lambda: self.snake.right(self.s.angle),
        }

        self.food = turtle.Turtle()
        self.starting_food_settings()
        self.food_exists = False

        self.snake = turtle.Turtle()
        self.starting_snake_settings()
        self.snake_hitbox = []




    def starting_snake_settings(self):

        line_size = self.s.snake_line_size
        shape_size = self.s.snake_shape_size
        self.snake_num_of_stamps = 0
        self.snake_len = 0
        self.snake.shape(self.s.snake_shape)
        self.snake.pensize(line_size)
        self.snake.shapesize(shape_size, shape_size)
        self.snake.penup()


    def starting_food_settings(self):

        self.food.hideturtle()
        self.food.shape(self.s.food_shape)
        self.food.shapesize(self.s.food_shape_size)
        self.food.color(self.s.food_color)
        self.food.penup()


    def spawn_food(self):

        self.food.showturtle()
        if not self.food_exists:
            random_x = random.randint((self.s.window_width / -2),
                                      (self.s.window_width / 2))
            random_y = random.randint((self.s.window_height / -2),
                                      (self.s.window_height / 2))
            self.food.goto((random_x, random_y))
            self.food_exists = True


    def snake_keep_length(self):

        if len(self.snake_hitbox) > self.snake_len:
            self.snake.clearstamps(1)
            if self.snake_hitbox is not None:
                first_stamp = self.snake_hitbox[0]
                self.snake_hitbox.remove(first_stamp)


    def make_stamp(self):

        if self.s.snake_stamp_clock < self.s.snake_stamp_reset:
            self.s.snake_stamp_clock += 1
        else:
            if self.snake_len > 0:
                self.snake.stamp()
                stamp_hitbox = self.create_hitbox(self.snake, 30)
                self.snake_hitbox.append(stamp_hitbox)
                self.s.snake_stamp_clock = 0


    def create_hitbox(self, game_object, hitbox_size) -> tuple:

        hitbox = (round(game_object.position()[0] - hitbox_size),
                  round(game_object.position()[0] + hitbox_size),
                  round(game_object.position()[1] - hitbox_size),
                  round(game_object.position()[1] + hitbox_size))
        return hitbox


    def snake_eat(self):

        # Create hitbox around food object centre
        FOOD_HITBOX_SIZE = self.s.food_hitbox_size
        food_position_x = (self.food.position()[0] - FOOD_HITBOX_SIZE,
                           self.food.position()[0] + FOOD_HITBOX_SIZE)
        food_position_y = (self.food.position()[1] - FOOD_HITBOX_SIZE,
                           self.food.position()[1] + FOOD_HITBOX_SIZE)

        # If snake head inside food hitbox
        if self.food_exists:
            if self.snake.position()[0] > food_position_x[0]:
                if self.snake.position()[0] < food_position_x[1]:
                    if self.snake.position()[1] > food_position_y[0]:
                        if self.snake.position()[1] < food_position_y[1]:
                            # Snake increase length, print score, respawn food
                            self.snake_len += 1
                            print(self.snake_len)
                            self.food_exists = False
                            self.spawn_food()
        
    
    def snake_self_damage(self):

        SNAKE_HITBOX_SIZE = self.s.food_hitbox_size
        


    def change_color(self):

        # Generate random RGB color and assign it to snake
        red = random.randint(0, 255)
        green = random.randint(0, 255)
        blue = random.randint(0, 255)
        new_color = (red, green, blue)
        self.snake.color(new_color)





    def handle_angle_speed(self):

        # When snake is changing direction, increase angle degree of movement
        # up to s.angle_max. When key is released, reset angle
        if "l" in self.keys_pressed or "r" in self.keys_pressed:
            if self.s.angle < self.s.angle_max:
                self.s.angle += self.s.angle_increment
        else:
            self.s.angle = 1


    def clear_screen(self):

        self.screen.reset()
        self.starting_snake_settings()
        self.starting_food_settings()





    def tick(self):

        self.handle_keys_pressed()
        self.handle_angle_speed()
        self.spawn_food()
        self.snake_eat()
        self.make_stamp()
        self.snake_keep_length()
        # for index, element in enumerate(self.snake_hitbox):
        #     print(f"{index}. {element}")
        # print("")



    def main(self):

        self.user_input()
        self.screen.listen()
        self.tick()
        self.screen.exitonclick()


snake_game = SnakeGame()
snake_game.main()
