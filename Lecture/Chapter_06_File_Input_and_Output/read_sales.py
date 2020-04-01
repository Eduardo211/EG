# Reading a file with a Loop and detecting
# the end of the file

def main():
    print('Reading sales data using a while loop')
    read_sales_while_loop()
    print('Reading sales data using a for loop')
    read_sales_for_loop()


# 1. Use a "while" loop
def read_sales_while_loop():
    # In Python, the readline method returns an empty string ('')
    # when it has attempted to read beyond the end of a file

    # Open the file
    # Use readline to read the first line from the file
    # While the value returned from readline is not an empty string:
    #   Process the item that was just read from the file
    #   Use readline to read the next line from the file
    # Close the file
    outfile = open('sales.txt','r')
    sales = outfile.readline()
    while sales != '':
        print(sales.rstrip('\n'))
        sales = outfile.readline()
    outfile.close()



# 2. Use a "for" loop
def read_sales_for_loop():
    outfile = open('sales.txt', 'r')
    for sales_line in outfile:
        print(sales_line.rstrip('\n'))

    outfile.close()

main()


