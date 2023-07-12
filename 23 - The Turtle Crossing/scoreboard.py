import turtle


class Scoreboard(turtle.Turtle):
    score: int = None

    def __init__(self) -> None:
        super().__init__()
        self.hideturtle()
        self.penup()
        self.goto(-260, 260)
        self.score = 0
        self.display_score()

    def increase_score(self):
        self.clear()
        self.score += 1
        self.display_score()

    def display_score(self):
        self.write(arg=f"Score: {self.score}", font=("Arial", 20, "bold"))
