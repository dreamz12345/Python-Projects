import turtle


class TennisRocket:
    COLOR: str = "white"
    SHAPE: str = "square"
    OFFSET: int = 400
    STRETCH_FACTOR: float = 2
    FACE_NORTH: float = 90
    is_right: bool = None
    screen: turtle._Screen = None

    def __init__(self, is_right, screen):
        tennis_rocket = turtle.Turtle()
        tennis_rocket.shape(self.SHAPE)
        tennis_rocket.shapesize(stretch_len=self.STRETCH_FACTOR)
        tennis_rocket.setheading(self.FACE_NORTH)
        tennis_rocket.color(self.COLOR)
        tennis_rocket.penup()
        self.screen = screen
        self.is_right = is_right
        self.tennis_rocket = tennis_rocket
        self.set_position()
        self.move()

    def set_position(self):
        if self.is_right:
            self.tennis_rocket.goto(self.OFFSET, 0)
        else:
            self.tennis_rocket.goto(-self.OFFSET, 0)

    def move(self):
        self.screen.onkeypress(key="Up", fun=lambda: self.tennis_rocket.forward(20))
        # self.screen.onkeypress(key="Up", fun=print("asdasd"))
