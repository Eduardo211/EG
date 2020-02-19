user_input = input("Enter an integer: ")
try:
    number = int(user_input)
    print("You entered", number)
    # your code
except ValueError:
    print("The input must be an integer.")
