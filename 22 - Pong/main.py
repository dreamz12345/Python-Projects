from tennis_rocket import TennisRocket
from screen import GameScreen
from ball import Ball

screen = GameScreen()
tennis_rocket_r = TennisRocket(is_right=True, screen=screen.screen)
tennis_rocket_l = TennisRocket(is_right=False, screen=screen.screen)
ball = Ball(screen=screen.screen)
screen.start_game()
