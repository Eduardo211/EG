# This program draws a list of squares
# (x, y) - the coordinates of the lower-left corner of the square
# width - the width of each side of the square
# color - the fill color for filling up the square

import  turtle

def square(x, y, width, color):
    turtle.hideturtle()
    turtle.penup()
    turtle.goto(x, y)
    turtle.pendown()
    turtle.fillcolor(color)
    turtle.begin_fill()
    for count in range(4):
        turtle.forward(width)  # step 1
        turtle.left(90)  # step 2
    turtle.end_fill()


square(0, 0, 35, 'red')
square(100, 100, 75, 'blue')
square(200, 75, 50, 'green')

turtle.done()


