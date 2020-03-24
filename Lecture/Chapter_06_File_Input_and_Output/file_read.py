# This program reads and displays the contents
# of the philosophers.txt file
def main():
    read_all()
    read_line_by_line()


def read_all():
    infile = open('philosophers.txt', 'r')
    file_contents = infile.read()
    # infile.write('John Doe\n') # the file object is not writable
    infile.close()
    print(file_contents)


def read_line_by_line():
    infile = open('philosophers.txt')
    line1 = infile.readline()
    line2 = infile.readline()
    line3 = infile.readline()

    infile.close()
    print(line1)
    print(line2)
    print(line3)


main()