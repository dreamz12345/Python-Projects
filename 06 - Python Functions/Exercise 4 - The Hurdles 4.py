
def turn_left():
    ""
def wall_on_right():
    ""
def move():
    ""
def front_is_clear():
    ""
def at_goal():
    ""

#--------------------------------------------

def turn_right():
    turn_left()
    turn_left()
    turn_left()
   
def jump():
    height = 0
    turn_left()
    while wall_on_right():
        move()
        height += 1
    turn_right()
    move()
    turn_right()
    for step in range(0, height):
        move()
    turn_left()
    
while not at_goal():
    while front_is_clear() and not at_goal():
        move()
    if not front_is_clear() and not at_goal():
        jump()