# Contentric circles
import turtle

NUM_CIRCLES = 20
STARTING_RADIUS = 20
OFFSET = 10
ANIMATION_SPEED = 0

turtle.speed(ANIMATION_SPEED)
turtle.hideturtle()
radius = STARTING_RADIUS
turtle.circle(radius)
for count in range(NUM_CIRCLES - 1):
    # find the new coordinates
    x = turtle.xcor()
    y = turtle.ycor() - OFFSET
    # move the turtle to the new location
    turtle.penup()
    turtle.goto(x,y)
    turtle.pendown()
    # calculate the new radius for the turtle to draw
    radius = radius + OFFSET
    turtle.circle(radius)
turtle.done()

