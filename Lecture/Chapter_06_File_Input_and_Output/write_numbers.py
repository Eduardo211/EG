# This program demonstrates how numbers
# must be converted to strings before
# they are written to a text file
import math
def main():
    # Open a file for writing
    outfile = open('circle.txt', 'w')

    # Enter the radius of a circle
    radius = float(input('Enter the radius of a circle: '))
    area = math.pi * radius**2
    circumference = math.pi * radius*2

    # Write the numbers to the file
    outfile.write(str(radius)+'\n')
    outfile.write(str(area) + '\n')
    outfile.write(str(circumference) + '\n')

    # Close the file
    outfile.close()
    print('Data written to circle.txt')

def read_circle_data():
    # Open the file
    infile = open('circle.txt', 'r')
    radius = float(infile.readline())
    infile.close()
    area = math.pi * radius**2 * 4
    circumference = math.pi * radius * 4
    print(radius)
    print(area)
    print(circumference)

read_circle_data()