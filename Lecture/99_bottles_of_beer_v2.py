# The following code is an implementation using a "for" loop
# Author: Jeffrey Zheng
bottle_start_amount = 99


def get_plurality(num):
    if num != 1:
        return 'bottles'
    else:
        return 'bottle'


def get_more_beer():
    print("No more bottles of beer on the wall, no more bottles of beer.")
    print("Go to the store and buy some more,", bottle_start_amount,
          get_plurality(bottle_start_amount), "of beer on the wall ")


for bottle_count in range(bottle_start_amount, 0, -1):
    print(f'{bottle_count} {get_plurality(bottle_count)} of beer on the wall, {bottle_count} '
          f'{get_plurality(bottle_count)} of beer...')
    print(
        f'Take one down and pass it around, {bottle_count - 1} {get_plurality((bottle_count - 1))} of beer on the '
        f'wall.\n')

get_more_beer()
