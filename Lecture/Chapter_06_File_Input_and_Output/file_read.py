# This program reads and displays the contents
# of the philosophers.txt file
def main():
    infile = open('philosophers.txt') # it is the same as open('philosophers.txt','r')
    line1 = infile.readline()
    line2 = infile.readline()
    line3 = infile.readline()
    infile.close()
    line1 = line1.rstrip('\n')
    line2 = line2.rstrip('\n')
    line3 = line3.rstrip('\n')
    print(line1)
    print(line2)
    print(line3)


main()
