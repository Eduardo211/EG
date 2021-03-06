# save_student_records() function gets student data
# from the user and saves it as records in
# the students.txt file
import os

def edit_student_record():
    found = False
    print()
    print('=== Edit a student record ===')
    # Open the original file for input and create a temporary file for output
    stu_file = open('students.txt', 'r')
    temp_file = open('temp.txt', 'w')
    # Get the name of the student record to be modified
    search_name = input('Enter the name of the student: ')
    # Read the first Name field from the original file
    name = stu_file.readline().rstrip('\n')
    # While the Name field is not empty:
    while name != '':
        # Read the ID Number field and the Major field
        id_num = stu_file.readline().rstrip('\n')
        major = stu_file.readline().rstrip('\n')
        if name == search_name:
            # Get the new value for the Major
            new_major = input('Enter the new Major: ')
            # Write the new data to the temporary file
            temp_file.write(name + '\n')
            temp_file.write(id_num + '\n')
            temp_file.write(new_major + '\n')
            found = True
        else:
            # Write the existing record to the temporary file
            temp_file.write(name + '\n')
            temp_file.write(id_num + '\n')
            temp_file.write(major + '\n')

        # Read the next Name field
        name = stu_file.readline().rstrip('\n')

    # Close the original file and the temporary file
    stu_file.close()
    temp_file.close()

    # Delete the original file
    os.remove('students.txt')
    # Rename the temporary file , giving it the name of the original file
    os.rename('temp.txt', 'students.txt')

    if found:
        print('The student record has been updated.')
    else:
        print('The student record was not found in the file.')



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
        id_num = int(input('ID Number: '))
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
edit_student_record()