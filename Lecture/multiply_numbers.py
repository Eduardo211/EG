# Calculate the product of a list of positive numbers
import math
NUMBER_LIST = [2, 4, 9, 12, 15, 22, 27, 30, 41]

# General steps to calculate the product of a list of numbers:
# 1. Create an accumulator and set its initial value to 1
# Why set it to 1? Why not set it to 0 as we calculate
# the running total of a list of numbers?
# TODO
product = 1

# 2. Loop through the list of positive numbers, multiply each
# number by the accumulator, then assign the value back
# to the accumulator
# TODO
for number in NUMBER_LIST:
    product *= number # product = product * number

# 3. Finally, print out the product
# TODO
print("The product is", product)
