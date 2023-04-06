# Coded by Lukasz Spychala

# this code is supposed to be run at reeborg.ca

# These two functions exist only to stop VS Code showing errors because
# turn_left() and move() functions are not defined
#  |
#  V
def turn_left():
    ""
def move():
    ""
#  ^
#  |


def turn_right():
    turn_left()
    turn_left()
    turn_left()

def move_and_jump():
    move()
    turn_left()
    move()
    turn_right()
    move()
    turn_right()
    move()
    turn_left()

for loop in range(0, 6):
    move_and_jump()