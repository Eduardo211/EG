import turtle
LENGTH = 100
ANGLE = 45
NUM_SIDES = 8

turtle.hideturtle()
for count in range(NUM_SIDES):
    turtle.forward(LENGTH)
    turtle.left(ANGLE)
turtle.done()
