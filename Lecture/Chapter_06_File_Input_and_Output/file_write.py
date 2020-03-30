# this program writes three lines of data
# to a file

def main():
    outfile = open('philosophers.txt', 'w')
    outfile.write('John Locke\n')
    outfile.write('David Hume\n')
    outfile.write('Edmund Burke\n')
    outfile.close()


main()