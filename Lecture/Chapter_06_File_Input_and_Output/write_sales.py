def main():
    num_days = int(input('For how many days do you have sales? '))
    sale_file = open('sales.txt', 'w')

    for count in range(1, num_days + 1):
        sales = float(input('Enter the sales for day #' + str(count) + ': '))
        sale_file.write(str(sales) + '\n')

    sale_file.close()
    print('Data written to sales.txt.')

main()