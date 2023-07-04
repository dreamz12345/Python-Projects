import ball
import turtle


class Scoreboard:
    score_l: int = None
    score_r: int = None
    ball_in_game: ball.Ball = None
    screen: turtle._Screen = None
    LEFT_EDGE_OF_SCREEN: int = None
    RIGHT_EDGE_OF_SCREEN: int = None

    def __init__(self, ball, screen) -> None:
        self.ball_in_game = ball
        self.screen = screen
        self.LEFT_EDGE_OF_SCREEN = int(self.screen.window_width() / -2)
        self.RIGHT_EDGE_OF_SCREEN = int(self.screen.window_width() / 2)
        self.score_l = 0
        self.score_r = 0
        self.initialize_scoreboard()

    def update_score(self):
        # If ball hits left side of the screen
        if self.ball_in_game.screen_left_edge_collision():
            self.ball_in_game.reset_ball()
            self.score_r += 1
            self.draw_score()
        # If ball hits right side of the screen
        elif self.ball_in_game.screen_right_edge_collision():
            self.ball_in_game.reset_ball()
            self.score_l += 1
            self.draw_score()

    def initialize_scoreboard(self):
        SCOREBOARD_X: int = 0
        SCOREBOARD_Y: int = int((self.screen.window_height() / 2))
        SCOREBOARD_Y_OFFSET: int = 50
        SCOREBOARD_Y -= SCOREBOARD_Y_OFFSET
        scoreboard_display = turtle.Turtle()
        scoreboard_display.penup()
        scoreboard_display.color("white")
        scoreboard_display.hideturtle()
        SCOREBOARD_CORDS = (SCOREBOARD_X, SCOREBOARD_Y)
        scoreboard_display.goto((SCOREBOARD_CORDS))
        self.scoreboard_display = scoreboard_display
        self.draw_score()

    def draw_score(self):
        self.scoreboard_display.clear()
        self.scoreboard_display.write(
            arg=f"{self.score_l}   -   {self.score_r}",
            font=("Arial", 30, "bold"),
            align="center",
        )
