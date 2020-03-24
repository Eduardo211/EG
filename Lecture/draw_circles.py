# This program draws a circle.
# (x, y) - the coordinates of the center point
# radius - the radius of the circle
# color - the fill color for the circle

import turtle

def circle(x, y, radius, color):
    turtle.hideturtle()
    turtle.penup()
    turtle.goto(x, y - radius)
    turtle.pendown()
    turtle.fillcolor(color)
    turtle.begin_fill()
    turtle.circle(radius)
    turtle.end_fill()


circle(0, 0, 200, 'red')
circle(-150, -200, 100, 'blue')
circle(-150, 75, 75, 'green')

turtle.done()


