import turtle
import random
import tennis_rocket


class Ball:
    paddle_l: tennis_rocket.TennisRocket = None
    paddle_r: tennis_rocket.TennisRocket = None

    def __init__(self, tennis_rocket_l, tennis_rocket_r) -> None:
        self.paddle_l = tennis_rocket_l
        self.paddle_r = tennis_rocket_r
        self.ball = turtle.Turtle()
        self.ball.color("white")
        self.ball.shape("circle")
        self.ball.shapesize(1)
        self.ball.penup()
        self.reset_ball()

    def upadate_pos(self):
        if self.screen_top_edge_collision():
            self.screen_edge_collision()
        elif self.screen_bottom_edge_collision():
            self.screen_edge_collision()
        elif self.paddle_collision(self.paddle_l):
            self.left_paddle_collision()
        elif self.paddle_collision(self.paddle_r):
            self.right_paddle_collision()
        self.ball.forward(1)

    def screen_edge_collision(self):
        self.ball.setheading(-self.ball.heading())

    def screen_left_edge_collision(self) -> bool:
        return self.ball.xcor() < -500

    def screen_right_edge_collision(self) -> bool:
        return self.ball.xcor() > 500

    def screen_top_edge_collision(self) -> bool:
        return self.ball.ycor() > 290

    def screen_bottom_edge_collision(self) -> bool:
        return self.ball.ycor() < -290

    def move_direction(self) -> str:
        heading = self.ball.heading()
        if heading >= 0 and heading < 90:
            return "right"
        elif heading >= 90 and heading < 270:
            return "left"
        elif heading >= 270:
            return "right"

    def paddle_collision(self, paddle: tennis_rocket.TennisRocket) -> bool:
        if self.ball.position()[0] > paddle.hitbox()[0][0]:
            if self.ball.position()[0] < paddle.hitbox()[0][1]:
                if self.ball.position()[1] > paddle.hitbox()[1][0]:
                    if self.ball.position()[1] < paddle.hitbox()[1][1]:
                        return True

    def right_paddle_collision(self):
        paddle_position = self.paddle_r.tennis_rocket.position()[1]
        # Bounce one time only
        if self.move_direction() == "right":
            if self.paddle_r.keys_pressed == {"up"} and paddle_position < 240:
                self.ball.setheading(160 - self.ball.heading())
            elif self.paddle_r.keys_pressed == {"down"} and paddle_position > -240:
                self.ball.setheading(200 - self.ball.heading())
            else:
                self.ball.setheading(180 - self.ball.heading())

    def left_paddle_collision(self):
        paddle_position = self.paddle_l.tennis_rocket.position()[1]
        # Bounce one time only
        if self.move_direction() == "left":
            if self.paddle_l.keys_pressed == {"up"} and paddle_position < 240:
                self.ball.setheading(200 - self.ball.heading())
            elif self.paddle_l.keys_pressed == {"down"} and paddle_position > -240:
                self.ball.setheading(160 - self.ball.heading())
            else:
                self.ball.setheading(180 - self.ball.heading())

    def reset_ball(self):
        self.ball.goto(0, 0)
        random_number = random.randint(0, 1)
        # Set ball direction to left or right
        if random_number == 0:
            self.ball.setheading(random.randint(180, 240))
        else:
            self.ball.setheading(random.randint(0, 60))
