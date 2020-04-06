# save_student_records() function gets student data
# from the user and saves it as records in
# the students.txt file


def save_student_records():
    # Get the number of student records to create
    num_students = int(input('How many student records do you want to create? '))
    # Open a file for writing
    stu_file = open('students.txt', 'w')
    # Get each student's data and write it to
    # the file
    for count in range(1, num_students + 1):
        print('Enter data for student #', count, sep='')
        name = input('Name: ')
        id_num = input('ID Number: ')
        major = input('Major: ')

        stu_file.write(name + '\n')
        stu_file.write(id_num + '\n')
        stu_file.write(major + '\n')

        print() # print a blank line

    # Don't forget to close the file
    stu_file.close()
    print('Student records written to students.txt')

# Displays the student records that are
# in the students.txt file
def read_student_records():

    # Open the students.txt file
    stu_file = open('students.txt', 'r')
    # Read the first line from the file, which is
    # the name field of the first record
    name = stu_file.readline()
    # If a field was read, continue processing
    while name != '':
        id_number = stu_file.readline()
        major = stu_file.readline()
        # Strip the newline character from the fields
        name = name.rstrip('\n')
        id_number = id_number.rstrip('\n')
        major = major.rstrip('\n')

        # Display the record
        print('Name:', name)
        print('ID Number:', id_number)
        print('Major:', major)

        # Print a blank line
        print()

        # Read the name field of the next record
        name = stu_file.readline()

    # Don't forget to close the file
    stu_file.close()

# save_student_records()
read_student_records()