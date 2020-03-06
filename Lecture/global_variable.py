import math
isValid = True


def do_factorial(number):
    if isValid == True:
        fact = math.factorial(number);
        print(f"The factorial is: {fact}")
    else:
        print(f"Cannot calculate the factorial.")


def main():
    # ask for a number
    number = int(input("Enter a number: "))
    if number < 0:
        global  isValid
        isValid = False

    # calculate the factorial
    do_factorial(number)

main()