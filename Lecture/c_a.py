# Python allows a function to return multiple values in one function call

import math


def c_a(r):
    circumference = math.pi * 2 * r
    area = math.pi * r * r
    return circumference, area


C, A = c_a(20)

print(C)
print(A)
