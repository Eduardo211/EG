# save_student_records() function gets student data
# from the user and saves it as records in
# the students.txt file
import os


def main():
    choice = ''
    while choice.upper() != 'Q':
        choice = print_menu_options()
        if choice == 'W':
            save_student_records()
        elif choice == 'R':
            read_student_records()
        elif choice == 'E':
            edit_student_record()
        elif choice == 'D':
            delete_student_record()

def edit_student_record():
    found = False
    print()
    print('=== Edit a student record ===')
    search = input('Enter the name of the student: ')
    stu_file = open('students.txt', 'r')
    temp_file = open('temp.txt', 'w')
    name = stu_file.readline().rstrip('\n')  # the first line is the name field
    while name != '':
        id_num = stu_file.readline().rstrip('\n')
        major = stu_file.readline().rstrip('\n')
        gpa = stu_file.readline().rstrip('\n')
        if name == search:
            print(f'Current Major is {major}. ', end='')
            new_major = input('Enter the new Major: ')
            print(f'Current GPA is {gpa}. ', end='')
            new_gpa = input('Enter the new GPA: ')
            temp_file.write(name + '\n')
            temp_file.write(id_num + '\n')
            temp_file.write(new_major + '\n')
            temp_file.write(new_gpa + '\n')
            found = True
        else:
            temp_file.write(name + '\n')
            temp_file.write(id_num + '\n')
            temp_file.write(major + '\n')
            temp_file.write(gpa + '\n')
        name = stu_file.readline().rstrip('\n')

    stu_file.close()
    temp_file.close()

    os.remove('students.txt')
    os.rename('temp.txt', 'students.txt')

    if found:
        print('The student record has been updated.')
    else:
        print('The student record was not found in the file.')


def delete_student_record():
    print()
    print('=== Delete a student record ===')
    search = input('Enter the name of the student: ')
    stu_file = open('students.txt', 'r')
    temp_file = open('temp.txt', 'w')
    name = stu_file.readline().rstrip('\n')

    found = False
    while name != '':
        id_num = stu_file.readline().rstrip('\n')
        major = stu_file.readline().rstrip('\n')
        gpa = stu_file.readline().rstrip('\n')
        if name != search:
            temp_file.write(name + '\n')
            temp_file.write(id_num + '\n')
            temp_file.write(major + '\n')
            temp_file.write(gpa + '\n')
        else:
            found = True
        name = stu_file.readline().rstrip('\n')
    stu_file.close()
    temp_file.close()

    os.remove('students.txt')
    os.rename('temp.txt', 'students.txt')

    if found:
        print('The student record has been deleted.')
    else:
        print('The student record was not found in the file.')



def print_menu_options():
    print()
    print('What would you like to do? ')
    print(' - Save student records (W/w)')
    print(' - Read student records (R/r)')
    print(' - Edit a student record (E/e)')
    print(' - Delete a student record (D/d)')
    print(' - Quit the program (Q/q)')
    choice = input('Enter your choice: ')
    return choice.upper()


def save_student_records():
    print()
    print('=== Save student records ===')
    # Get the number of student records to create
    num_students = int(input('How many student records do you want to create? '))
    # Open a file for writing
    stu_file = open('students.txt', 'a')
    # Get each student's data and write it to
    # the file
    for count in range(1, num_students + 1):
        print('Enter data for student #', count, sep='')
        name = input('Name: ')
        id_num = input('ID Number: ')
        major = input('Major: ')
        gpa = input('GPA: ')

        stu_file.write(name + '\n')
        stu_file.write(id_num + '\n')
        stu_file.write(major + '\n')
        stu_file.write(gpa + '\n')

        print() # print a blank line

    # Don't forget to close the file
    stu_file.close()
    print('Student records written to students.txt')

# Displays the student records that are
# in the students.txt file
def read_student_records():
    print()
    print('=== Read student records ===')
    # Open the students.txt file
    stu_file = open('students.txt', 'r')
    # Read the first line from the file, which is
    # the name field of the first record
    name = stu_file.readline()
    # If a field was read, continue processing
    while name != '':
        id_number = stu_file.readline()
        major = stu_file.readline()
        gpa = stu_file.readline()
        # Strip the newline character from the fields
        name = name.rstrip('\n')
        id_number = id_number.rstrip('\n')
        major = major.rstrip('\n')
        gpa = gpa.rstrip('\n')

        # Display the record
        print('Name:', name)
        print('ID Number:', id_number)
        print('Major:', major)
        print('GPA:', gpa)

        # Print a blank line
        print()

        # Read the name field of the next record
        name = stu_file.readline()

    # Don't forget to close the file
    stu_file.close()

main()