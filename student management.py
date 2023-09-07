# STUDENT MANAGEMENT SYSTEM
# NAME: AMWINE NICKSON
# REG NO: 20/U/0086

# Defining a class for the student object
class Student:
    def __init__(self, name, roll_number, marks):
        self.name = name
        self.roll_number = roll_number
        self.marks = marks
        self.grade = self.grade_calc()
# Method for setting up a new name for the student
    def set_name(self, new_name):
        self.name = new_name
        return self.name
    def get_name(self):       #method for retrieving the name of a student
        return self.name
# Method for setting up a new roll number for the student
    def set_roll_number(self, new_roll_number):
        self.roll_number = new_roll_number
        return self.roll_number
    def get_roll_number(self):      #Method for retrieving the roll number of a student
        return self.roll_number
# Method for setting the new grade
    def set_grade(self, new_grade):
        self.grade = new_grade
        return self.grade
    def get_grade(self):            #Method for retrieving a grade of a student
        return self.grade
# Method for setting new marks
    def set_marks(self, new_marks):
        self.marks = new_marks
        self.grade = self.grade_calc()
        return self.marks
    def get_marks(self):            #Method for retrieving marks of a student
        return self.marks
# Function for calculating the grade from the marks entered
    def grade_calc(self):
        if self.marks >= 85:
            return 'A'
        elif self.marks >= 70 and self.marks < 85:
            return 'B'
        elif self.marks >= 60 and self.marks < 70:
            return 'C'
        elif self.marks >= 50 and self.marks < 60:
            return 'D'
        else:
            return 'F'
        
# Creating a list where all students added are to  be stored
students = []
# Function for adding students in the system
def adding_students():
    print('\n')
    num_students = int(input('How many students do you want to add: '))
    for num in range(num_students):
        name = input('Enter student name: ')
        roll_number = input('Enter student roll_number: ')
        marks = float(input('Enter student marks: '))
        student = Student(name, roll_number, marks)
        students.append(student)
        print(f"{name.title()} has been added successfully\n")
# Function for displaying student information
def display(students):
    if not students:
        print('No students found. The students list is empty.')
        return
    roll_num = input('\nEnter student roll number: ')
    for student in students:
        if roll_num == student.get_roll_number():
            print('\n\t\tStudent Information')
            print('\t\t==========================')
            print(f"student Name: {student.get_name().title()}\n")
            print(f"Roll number: {student.get_roll_number()}\n")
            print(f"Marks: {student.get_marks()}\n")
            print(f"Grade: {student.get_grade()}\n")
            break
        else:
            print('Student does not exist')
# Function for updating student Information
def update_student(students):
    if not students:
        print('No students to update. The students list is empty.')
        return
    roll_num = input('\nEnter student roll number of student to be updated: ')
    for student in students:
        if student.get_roll_number() == roll_num:
            print("1. student name\n2. Roll number\n3. Marks\n")
            select = int(input('select the attribute to update: '))
            if select == 1:
                new_name = input('Enter new name: ')
                student.set_name(new_name)
                print('Name has been updated successfully!')
            elif select == 2:
                new_roll_number = input('Enter new roll number: ')
                student.set_roll_number(new_roll_number)
                print('Roll number has been updated successfully!')
            elif select == 3:
                new_marks = float(input('Enter new marks: '))
                student.set_marks(new_marks)
                print('Marks have been updated successfully!')
            else:
                print('Invalid selection!')
            break
        else:
            print('Student doesnot exist')
# Function for deleting students from the system
def delete_student(students):
    if not students:
        print('Nothing to delete. Student list is empty!')
        return
    roll_number = input('Enter roll number of student to delete: ')
    for student in students:
        if roll_number == student.get_roll_number():
            students.remove(student)
            print(f"{student.get_name()} deleted successfully")
            break
        else:
            print('student doesnot exist')
# Function for displaying the options menu
def menu():
    print('===========================MENU====================================')
    print('Select an operation to perform from the menu below')
    print('1. Add student\n2. Display student information\n3. Update student details\n4. Delete student\n5. Quit')
    print('===================================================================\n')
# while loop for calling the menu function and evaluating the users selection from the menu 
while True:
    menu()
    choice = int(input('Enter operation to perform: '))
    if choice == 1:
        adding_students()
    elif choice == 2:
        display(students)
    elif choice == 3:
        update_student(students)
    elif choice == 4:
        delete_student(students)
    elif choice == 5:
        break
    else:
        print('Invalid choice')
        break