import turtle


class Ball:
    def __init__(self, screen) -> None:
        self.ball = turtle.Turtle()
        self.ball.color("white")
        self.move()

    def move(self):
        pass
