# The Collatz Conjecture is named after Lothar Collatz, who introduced the idea in 1937, two years
# after receiving his doctorate
# State of the problem
# Considering the following operation on an arbitrary positive integer:
# if the number is even, divide it by two
# if the number is odd, triple it and add one
# Now form a sequence by performing this operation repeatedly, beginning with any positive
# integer, and taking the result at each step as the input at the next
# The Collatz conjecture is: This process will eventually reach the number 1, regardless
# of which positive integer is chosen initially

# Write a program to prompt user to enter a positive integer
# then print out the Collatz sequence for the positive integer

# Prompt user for the input (don't forget to validate the input)
def user_input():
    while True:
        try:
            n = int(input("Please enter a positive integer: "))
            if n <= 0:
                print("The number must be positive. ")
            else:
                return n
        except ValueError:
            print("It's not a valid number. ")
# if we reach here, it means the number is valid
print(n)

def collatz(num):
    print(num, end=' ')
    while num != 1:
        if num % 2 == 0:  # an even number
            num = num // 2
        else:
            num = num * 3 + 1
        print(num, end=' ')
    print()
# What type of loop should we use?


number = user_input()
collatz(number)

# The sequence should start with the number user chose
# and end with 1
