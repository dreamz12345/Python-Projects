import turtle


class TennisRocket:
    COLOR: str = "white"
    SHAPE: str = "square"
    OFFSET: int = 470
    STRETCH_FACTOR: float = 2
    FACE_NORTH: float = 90
    is_right: bool = None
    screen: turtle._Screen = None
    move_dir = 0
    keys_pressed = None

    def __init__(self, is_right, screen):
        self.keys_pressed = set()
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

    def set_dir(self, move_dir):
        self.move_dir = move_dir

    def move(self):
        if self.is_right:
            self.screen.onkeypress(key="Up", fun=lambda: self.keys_pressed.add("up"))
            self.screen.onkeypress(
                key="Down", fun=lambda: self.keys_pressed.add("down")
            )

            self.screen.onkeyrelease(
                key="Up", fun=lambda: self.keys_pressed.remove("up")
            )
            self.screen.onkeyrelease(
                key="Down", fun=lambda: self.keys_pressed.remove("down")
            )
        else:
            self.screen.onkeypress(key="w", fun=lambda: self.keys_pressed.add("up"))
            self.screen.onkeypress(key="s", fun=lambda: self.keys_pressed.add("down"))

            self.screen.onkeyrelease(
                key="w", fun=lambda: self.keys_pressed.remove("up")
            )
            self.screen.onkeyrelease(
                key="s", fun=lambda: self.keys_pressed.remove("down")
            )

    def update_pos(self):
        if {"up", "down"} == self.keys_pressed:
            pass
        elif "up" in self.keys_pressed:
            self.tennis_rocket.forward(5)
        elif "down" in self.keys_pressed:
            self.tennis_rocket.backward(5)
