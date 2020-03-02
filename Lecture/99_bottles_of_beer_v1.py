# Defining variables
bottle_start_amount = 99
bottle_end = 0
bottles_current = bottle_start_amount
bottles_remaining = int(bottles_current) - 1


# This function checks if the word "bottle" should be singular or plural
def bottle_check():
    bottle_state = "bottles"
    if bottles_remaining != 1:
        bottle_state = "bottles"
    elif bottles_remaining == 1:
        bottle_state = "bottle"
    return bottle_state


# This function is used at the end to see when beer has run out and the store lyrics begin
def buy_bottles():
    if bottles_remaining == 0:
        bottle_plurality = str(bottle_check())
        print("No more bottles of beer on the wall, no more bottles of beer.")
        print("Go to the store and buy some more,", bottle_start_amount, bottle_plurality, "of beer on the wall.")


# Main portion of code that prints lyrics with proper plurality and a space between each verse
while bottles_remaining > 0:
    bottle_plurality = str(bottle_check())
    print(bottles_current, bottle_plurality, "of beer on the wall,", bottles_current, bottle_plurality, "of beer.")
    bottles_remaining = int(bottles_current) - 1
    bottle_plurality = str(bottle_check())
    print("Take one down and pass it around,", bottles_remaining, bottle_plurality, "of beer on the wall.\n")
    bottles_current -= 1
    if bottles_remaining == 0:
        buy_bottles()
