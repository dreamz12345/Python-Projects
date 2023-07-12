import turtle
from car import Car


class Player(turtle.Turtle):
    PLAYER_SHAPE: str = "turtle"
    OFFSET: int = -280
    STRETCH_FACTOR: float = 1
    FACE_NORTH: float = 90
    screen: turtle._Screen = None
    keys_pressed: set = None

    def __init__(self, screen):
        super().__init__()
        self.keys_pressed = set()
        self.shape(self.PLAYER_SHAPE)
        self.shapesize(self.STRETCH_FACTOR)
        self.setheading(self.FACE_NORTH)
        self.penup()
        self.reset_pos()
        self.move(screen)

    def reset_pos(self):
        self.goto(0, self.OFFSET)

    def move(self, screen: turtle._Screen):
        keys_p = self.keys_pressed
        screen.onkeypress(key="Up", fun=lambda: keys_p.add("up"))
        screen.onkeyrelease(key="Up", fun=lambda: keys_p.remove("up"))

    def update_pos(self):
        if "up" in self.keys_pressed and self.position()[1] < 280:
            self.forward(3)

    def is_collision_with_car(self, car: Car) -> bool:
        is_collision = False
        flag_1 = False
        flag_2 = False
        flag_3 = False
        flag_4 = False
        if self.position()[0] > car.hitbox()[0][0]:
            flag_1 = True
        if self.position()[0] < car.hitbox()[0][1]:
            flag_2 = True
        if self.position()[1] > car.hitbox()[1][0]:
            flag_3 = True
        if self.position()[1] < car.hitbox()[1][1]:
            flag_4 = True
        if flag_1 and flag_2 and flag_3 and flag_4:
            is_collision = True
        return is_collision

    def reached_finish(self):
        if self.position()[1] > 275:
            self.reset_pos()
            return True
