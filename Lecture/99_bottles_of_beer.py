bottle_number = 99
for bottle_count in range(bottle_number, 0, -1):
    if bottle_count >= 3:
        print(f'\n{bottle_count} bottles of beer on the wall, {bottle_count} bottles of beer \
        \nTake one down pass it around, {bottle_count - 1} bottles of beer on the wall.')
    elif bottle_count == 2:
        print(f'\n{bottle_count} bottles of beer on the wall, {bottle_count} bottles of beer \
        \nTake one down pass it around, {bottle_count - 1} bottle of beer on the wall.')
    elif bottle_count == 1:
        print(f'\n{bottle_count} bottle of beer on the wall, {bottle_count} bottle of beer \
        \nTake one down pass it around, {bottle_count - 1} bottles of beer on the wall. \
        \n\nNo more bottles of beer on the wall, no more bottles of beer. \
        \nGo to the store and buy some more, \
        \n{bottle_number} bottles of beer on the wall.')