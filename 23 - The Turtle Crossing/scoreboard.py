import turtle


class Scoreboard(turtle.Turtle):
    score: int = None

    def __init__(self) -> None:
        super().__init__()
        self.hideturtle()
        self.penup()
        self.goto(-260, 260)
        self.score = 0
