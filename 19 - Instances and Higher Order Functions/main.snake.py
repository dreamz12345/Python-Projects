import turtle
import random
from enum import Enum
from typing import Set
import math


class GameSettings:
    def __init__(self) -> None:
        self.food_shape = "circle"
        self.food_shape_size = 1.5
        self.food_hitbox_size = 30
        self.food_color = "red"


class Arrow(Enum):
    LEFT = 0
    RIGHT = 1


class KeysPressed:
    keys_pressed: Set[Arrow] = None

    def __init__(self) -> None:
        self.keys_pressed = set()

    def press(self, arrow: Arrow):
        self.keys_pressed.add(arrow)

    def unpress(self, arrow: Arrow):
        self.keys_pressed.remove(arrow)

    def get_pressed(self) -> Set[Arrow]:
        return self.keys_pressed


class GameEngine:
    # Constants

    GAME_TITLE: str = "Snake Game!"

    WINDOW_WIDTH: int = 600
    WINDOWS_HEIGHT: int = 600

    COLORMODE: int = 255

    FRAME_DELAY_MS: int = 10

    # Variables

    turtle_screen: turtle._Screen = None
    keys_pressed: KeysPressed = None
    on_update: callable(Set[Arrow]) = None
    on_clear: callable = None

    def __init__(self, on_update: callable, on_clear: callable) -> None:
        self.on_update = on_update
        self.on_clear = on_clear
        screen = turtle.Screen()
        screen.tracer(0)
        screen.setup(self.WINDOW_WIDTH, self.WINDOWS_HEIGHT)
        screen.title(self.GAME_TITLE)
        screen.colormode(self.COLORMODE)
        self.turtle_screen = screen
        self.keys_pressed = KeysPressed()

    def get_screen_size(self):
        return (self.WINDOW_WIDTH, self.WINDOWS_HEIGHT)

    def setup_key_events(self):
        keys = self.keys_pressed
        screen = self.turtle_screen

        screen.onkeypress(lambda: keys.press(Arrow.LEFT), "Left")
        screen.onkeypress(lambda: keys.press(Arrow.RIGHT), "Right")

        screen.onkeyrelease(lambda: keys.unpress(Arrow.LEFT), "Left")
        screen.onkeyrelease(lambda: keys.unpress(Arrow.RIGHT), "Right")

        screen.onkey(fun=self.handle_clear, key="e")

    def on_tick(self):
        self.on_update(self.keys_pressed.get_pressed())
        self.turtle_screen.update()
        self.turtle_screen.ontimer(fun=self.on_tick, t=self.FRAME_DELAY_MS)

    def start_game(self):
        self.setup_key_events()
        self.turtle_screen.listen()
        self.on_tick()
        self.turtle_screen.exitonclick()

    def handle_clear(self):
        if self.on_clear is not None:
            self.on_clear()


class Snake:
    # Constants

    TURN_ANGLE = 10

    SNAKE_SHAPE = "circle"
    SNAKE_SHAPE_SIZE = 2

    SNAKE_STAMP_MAX = 16

    STEP_SPEED: int = 2

    COLLISION_RADIUS: int = 50

    # Variable

    snake_stamp_clock: int = 0
    snake_turtle: turtle.Turtle = None

    def __init__(self) -> None:
        self.snake_turtle = turtle.Turtle()
        self.snake_turtle.shape(self.SNAKE_SHAPE)
        self.snake_turtle.shapesize(self.SNAKE_SHAPE_SIZE, self.SNAKE_SHAPE_SIZE)
        self.snake_turtle.penup()

    def on_update(self, arrows: Set[Arrow]):
        if Arrow.LEFT in arrows:
            self.snake_turtle.left(self.TURN_ANGLE)
        if Arrow.RIGHT in arrows:
            self.snake_turtle.right(self.TURN_ANGLE)
        self.snake_turtle.forward(self.STEP_SPEED)

    def is_collision(self, x: int, y: int) -> bool:
        turtle_x = self.snake_turtle.position()[0]
        turtle_y = self.snake_turtle.position()[1]

        dis2x = (turtle_x - x) ** 2
        dis2y = (turtle_y - y) ** 2

        distance = math.sqrt(dis2x + dis2y)

        collision = False
        if distance < self.COLLISION_RADIUS:
            collision = True
        return collision


class Food:
    FOOD_SHAPE = "circle"
    FOOD_SHAPE_SIZE = 2
    FOOD_COLOR = "red"
    PADDING = 100

    # Variable

    food_turtle: turtle.Turtle = None
    screen_size: tuple[int] = None

    def __init__(self, screen_size: tuple[int]) -> None:
        self.screen_size = screen_size
        self.food_turtle = turtle.Turtle()
        self.food_turtle.shape(self.FOOD_SHAPE)
        self.food_turtle.shapesize(self.FOOD_SHAPE_SIZE, self.FOOD_SHAPE_SIZE)
        self.food_turtle.color(self.FOOD_COLOR)
        self.food_turtle.penup()

    def get_position(self):
        return self.food_turtle.position()

    def move_to_new_position(self):
        x = self.screen_size[0] - self.PADDING
        y = self.screen_size[1] - self.PADDING
        random_x = random.randint((x / -2), (x / 2))
        random_y = random.randint((y / -2), (y / 2))
        self.food_turtle.goto((random_x, random_y))


class SnakeGame:
    engine: GameEngine = None
    snake: Snake = None
    food: Food = None

    def __init__(self) -> None:
        self.engine = GameEngine(self.on_update, None)
        self.snake = Snake()
        self.food = Food(self.engine.get_screen_size())
        self.engine.start_game()

    def on_update(self, arrows: Set[Arrow]):
        self.snake.on_update(arrows)
        food_pos = self.food.get_position()
        collision = self.snake.is_collision(food_pos[0], food_pos[1])
        if collision:
            self.food.move_to_new_position()


snake_game = SnakeGame()


# =============================================================================
# self.s = GameSettings()

# self.actions = {
#     "u": lambda: self.snake.forward(self.s.step_speed),
#     "l": lambda: self.snake.left(self.s.angle),
#     "r": lambda: self.snake.right(self.s.angle),
# }

# self.food = turtle.Turtle()
# self.starting_food_settings()
# self.food_exists = False

# self.snake = turtle.Turtle()
# self.starting_snake_settings()
# self.snake_hitbox = []


# def starting_snake_settings(self):

#     line_size = self.s.snake_line_size
#     shape_size = self.s.snake_shape_size
#     self.snake_num_of_stamps = 0
#     self.snake_len = 0
#     self.snake.shape(self.s.snake_shape)
#     self.snake.pensize(line_size)
#     self.snake.shapesize(shape_size, shape_size)
#     self.snake.penup()


# def starting_food_settings(self):

#     self.food.hideturtle()
#     self.food.shape(self.s.food_shape)
#     self.food.shapesize(self.s.food_shape_size)
#     self.food.color(self.s.food_color)
#     self.food.penup()


# def spawn_food(self):

#     self.food.showturtle()
#     if not self.food_exists:
#         random_x = random.randint((self.s.window_width / -2),
#                                   (self.s.window_width / 2))
#         random_y = random.randint((self.s.window_height / -2),
#                                   (self.s.window_height / 2))
#         self.food.goto((random_x, random_y))
#         self.food_exists = True


# def snake_keep_length(self):

#     if len(self.snake_hitbox) > self.snake_len:
#         self.snake.clearstamps(1)
#         if self.snake_hitbox is not None:
#             first_stamp = self.snake_hitbox[0]
#             self.snake_hitbox.remove(first_stamp)


# def make_stamp(self):

#     if self.s.snake_stamp_clock < self.s.snake_stamp_reset:
#         self.s.snake_stamp_clock += 1
#     else:
#         if self.snake_len > 0:
#             self.snake.stamp()
#             stamp_hitbox = self.create_hitbox(self.snake, 30)
#             self.snake_hitbox.append(stamp_hitbox)
#             self.s.snake_stamp_clock = 0


# def create_hitbox(self, game_object, hitbox_size) -> tuple:

#     hitbox = (round(game_object.position()[0] - hitbox_size),
#               round(game_object.position()[0] + hitbox_size),
#               round(game_object.position()[1] - hitbox_size),
#               round(game_object.position()[1] + hitbox_size))
#     return hitbox


# def snake_eat(self):

#     # Create hitbox around food object centre
#     FOOD_HITBOX_SIZE = self.s.food_hitbox_size
#     food_position_x = (self.food.position()[0] - FOOD_HITBOX_SIZE,
#                        self.food.position()[0] + FOOD_HITBOX_SIZE)
#     food_position_y = (self.food.position()[1] - FOOD_HITBOX_SIZE,
#                        self.food.position()[1] + FOOD_HITBOX_SIZE)

#     # If snake head inside food hitbox
#     if self.food_exists:
#         if self.snake.position()[0] > food_position_x[0]:
#             if self.snake.position()[0] < food_position_x[1]:
#                 if self.snake.position()[1] > food_position_y[0]:
#                     if self.snake.position()[1] < food_position_y[1]:
#                         # Snake increase length, print score, respawn food
#                         self.snake_len += 1
#                         print(self.snake_len)
#                         self.food_exists = False
#                         self.spawn_food()


# def snake_self_damage(self):

#     SNAKE_HITBOX_SIZE = self.s.food_hitbox_size


# def clear_screen(self):

#     self.screen.reset()
#     self.starting_snake_settings()
#     self.starting_food_settings()


# def tick(self):

#     self.handle_keys_pressed()
#     self.handle_angle_speed()
#     self.spawn_food()
#     self.snake_eat()
#     self.make_stamp()
#     self.snake_keep_length()
# for index, element in enumerate(self.snake_hitbox):
#     print(f"{index}. {element}")
# print("")


# def main(self):

#     self.user_input()
#     self.screen.listen()
#     self.tick()
#     self.screen.exitonclick()
