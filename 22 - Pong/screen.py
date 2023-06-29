import turtle


class GameScreen:
    BG_COLOR = "black"
    screen: turtle._Screen = None

    def __init__(self) -> None:
        screen = turtle.Screen()
        screen.bgcolor(self.BG_COLOR)
        # screen.tracer(0)
        self.screen = screen

    def start_game(self):
        self.screen.listen()
        self.screen.exitonclick()
