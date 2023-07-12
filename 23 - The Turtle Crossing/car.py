import turtle
import random


class Car(turtle.Turtle):
    COLORS: list = ["red", "green", "blue", "purple", "yellow"]
    SHAPE_CONST: str = "square"
    STRETCH_FACTOR: float = 2
    FACE_WEST: float = 180
    X_OFFSET: int = 350

    def __init__(self):
        super().__init__()
        self.shape(self.SHAPE_CONST)
        self.shapesize(stretch_len=self.STRETCH_FACTOR)
        self.color(random.choice(self.COLORS))
        self.penup()
        self.set_position()

    def set_position(self):
        # Generate random int within screen height
        random_y = random.randint(-220, 220)
        self.goto(self.X_OFFSET, random_y)
        self.setheading(self.FACE_WEST)

    def update_pos(self, car_speed):
        self.forward(car_speed)

    def should_delete_car(self) -> bool:
        if self.position()[0] < -250:
            return True

    def hitbox(self) -> tuple:
        x = self.position()[0]
        y = self.position()[1]
        width = (x - 30, x + 30)
        height = (y - 25, y + 25)
        hitbox = (width, height)
        return hitbox

    def increase_speed(self, speed):
        self.car_speed += speed
