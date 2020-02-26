# This program draws a design using repeated circles.

import turtle

NUM_CIRCLES = 36
RADIUS = 100
ANGLE = 10
ANIMATION_SPEED = 0

turtle.speed(ANIMATION_SPEED)
for count in range(NUM_CIRCLES):
    turtle.circle(RADIUS)
    turtle.left(ANGLE)

turtle.done()
