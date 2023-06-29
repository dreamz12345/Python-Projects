from tennis_rocket import TennisRocket
import turtle


def update_screen():
    tennis_rocket_l.update_pos()
    tennis_rocket_r.update_pos()
    screen.update()
    screen.ontimer(fun=update_screen, t=5)


screen = turtle.Screen()
screen.tracer(0)
screen.bgcolor("black")
screen.listen()

tennis_rocket_r = TennisRocket(is_right=True, screen=screen)
tennis_rocket_l = TennisRocket(is_right=False, screen=screen)

update_screen()

screen.exitonclick()
