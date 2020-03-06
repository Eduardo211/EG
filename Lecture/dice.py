# This program simulates the rolling of dice
import random

MIN = 1
MAX = 6

def roll_dice():
    print('Rolling the dice...')
    print('Their values are: ')
    print(random.randint(MIN, MAX))
    print(random.randint(MIN, MAX))

def get_input():
    user_input = input("Roll them again? (y = yes): ")
    return user_input.upper()


def main():
    # create a variable to control the loop
    again = 'Y'

    while again == 'Y':
        roll_dice()
        again = get_input()


main()
