# A loop this is inside another loop is called a nested loop.
# A simple example of a nested loop
for i in range(5):  # outer loop
    print('a')
    for j in range(3): # inner loop
        print('b')

# Example 2
# Write a program using a nested loop to draw this pattern:
# *******
# *******
# *******
# *******
# *******
NUM_ROWS = 6
NUM_COLS = 7
for row in range(NUM_ROWS):
    for col in range(NUM_COLS):
        print('*', end='')
    print()


# Example 3
# Write a program using a nested loop to draw this pattern:
# *
# **
# ***
# ****
# *****
# ******
ROW = 6
for row in range(ROW):
    for col in range(row+1):
        print('*', end='')
    print()


# Example 3
# Write a program using a nested loop to draw this pattern:
# *
#  *
#   *
#    *
#     *
#      *
NUMBER_OF_ROWS = 6
for row in range(NUMBER_OF_ROWS):
    for col in range(row):
        print(' ', end='')
    print('*')

