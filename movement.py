def yukari(turtle1, facing):
    if facing == "right":
        turtle1.left(90)
    if facing == "left":
        turtle1.right(90)
    if facing == "down":
        turtle1.left(180)
    turtle1.forward(50)
    facing = "up"
    return facing

def asagi(turtle1, facing):
    if facing == "right":
        turtle1.right(90)
    if facing == "left":
        turtle1.left(90)
    if facing == "up":
        turtle1.right(180)
    turtle1.forward(50)
    facing = "down"
    return facing

def sag(turtle1, facing):
    if facing == "up":
        turtle1.right(90)
    if facing == "down":
        turtle1.left(90)
    if facing == "left":
        turtle1.right(180)
    turtle1.forward(50)
    facing = "right"
    return facing

def sol(turtle1, facing):
    if facing == "up":
        turtle1.left(90)
    if facing == "down":
        turtle1.right(90)
    if facing == "right":
        turtle1.left(180)
    turtle1.forward(50)
    facing = "left"
    return facing
