# This program gets three names from the user
# and writes them to a file

def main():
    # Get three names
    print('Enter the names of three friends. ')
    name1 = input('Friend #1: ')
    name2 = input('Friend #2: ')
    name3 = input('Friend #3: ')

    # Open a file named friends.txt
    # and use variable myfile to reference the file object
    myfile = open('friends.txt', 'w')  # complete this line in the chat window
    myfile.write(name1 + '\n')
    myfile.write(name2 + '\n')
    myfile.write(name3 + '\n')

    # close the file
    myfile.close()
    print('The names were written to friends.txt.')

def append_names():
    name4 = input('Friend #4: ')
    name5 = input('Friend #5: ')
    # Open the file
    app_file = open('friends.txt', 'a')
    app_file.write(name4 + '\n')
    app_file.write(name5 + '\n')

    app_file.close()


append_names()