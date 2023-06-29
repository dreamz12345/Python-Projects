import turtle
import random


class Ball:
    def __init__(self) -> None:
        self.ball = turtle.Turtle()
        self.ball.color("white")
        self.ball.shape("square")
        self.ball.penup()
        self.random_start()

    def upadate_pos(self, tennis_rocket_l, tennis_rocket_r):
        if self.ball.ycor() > 280 or self.ball.ycor() < -280:
            self.ball.setheading(-self.ball.heading())

        if (
            self.ball.distance(tennis_rocket_l.tennis_rocket.position()) < 40
            or self.ball.distance(tennis_rocket_r.tennis_rocket.position()) < 40
        ):
            self.ball.setheading(180 - self.ball.heading())
        self.ball.forward(5)

    def right_collision(self):
        if self.ball.heading < 90 and self.ball.heading > 0:
            self.ball.setheading(180 - self.ball.heading())
        elif self.ball.heading > 270 and self.ball.heading < 360:
            pass

    def random_start(self):
        random_number = random.randint(0, 1)
        if random_number == 0:
            self.ball.setheading(random.randint(0, 60))
        else:
            self.ball.setheading(random.randint(180, 240))
