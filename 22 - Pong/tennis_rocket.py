import turtle


class TennisRocket:
    COLOR: str = "white"
    SHAPE: str = "square"
    OFFSET: int = 480
    STRETCH_FACTOR: float = 5
    FACE_NORTH: float = 90
    is_right: bool = None
    screen: turtle._Screen = None
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

    def move(self):
        keys_p = self.keys_pressed
        if self.is_right:
            self.screen.onkeypress(key="Up", fun=lambda: keys_p.add("up"))
            self.screen.onkeypress(key="Down", fun=lambda: keys_p.add("down"))
            self.screen.onkeyrelease(key="Up", fun=lambda: keys_p.remove("up"))
            self.screen.onkeyrelease(key="Down", fun=lambda: keys_p.remove("down"))
        else:
            self.screen.onkeypress(key="w", fun=lambda: keys_p.add("up"))
            self.screen.onkeypress(key="s", fun=lambda: keys_p.add("down"))
            self.screen.onkeyrelease(key="w", fun=lambda: keys_p.remove("up"))
            self.screen.onkeyrelease(key="s", fun=lambda: keys_p.remove("down"))

    def update_pos(self):
        if {"up", "down"} == self.keys_pressed:
            pass
        elif "up" in self.keys_pressed and self.tennis_rocket.position()[1] < 240:
            self.tennis_rocket.forward(10)
        elif "down" in self.keys_pressed and self.tennis_rocket.position()[1] > -240:
            self.tennis_rocket.backward(10)

    def hitbox(self):
        x = self.tennis_rocket.position()[0]
        y = self.tennis_rocket.position()[1]
        paddle_width = (x - 25, x + 25)
        paddle_height = (y - 55, y + 55)
        hitbox = (paddle_width, paddle_height)
        return hitbox
