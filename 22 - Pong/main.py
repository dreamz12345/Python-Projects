from tennis_rocket import TennisRocket
from ball import Ball
from scoreboard import Scoreboard
import turtle


def update_screen():
    tennis_rocket_l.update_pos()
    tennis_rocket_r.update_pos()
    ball.upadate_pos()
    scoreboard.update_score()
    screen.update()
    screen.ontimer(fun=update_screen, t=1)


screen = turtle.Screen()
screen.tracer(0)
screen.bgcolor("black")
screen.setup(width=1000, height=600)
screen.listen()

tennis_rocket_r = TennisRocket(is_right=True, screen=screen)
tennis_rocket_l = TennisRocket(is_right=False, screen=screen)
ball = Ball(tennis_rocket_l=tennis_rocket_l, tennis_rocket_r=tennis_rocket_r)
scoreboard = Scoreboard(ball=ball, screen=screen)

update_screen()
screen.mainloop()

# screen.exitonclick()
