'''
Q1. Define function student_data() to print ID, name, and class if given

Write a Python function student_data () that will print the ID of a student (student_id).
If the user passes an argument student_name or student_class the function will print the student name and class.
'''


# def student_data(student_id, student_name, student_class):
#     print(f'The name of the student is {student_name}. He/She studies on class {student_class}. \n The students id number is {student_id}.')


# student_id = int(input("Enter the student's id : "))
# student_name = input("Enter the student's name : ")
# student_class = input("Enter the student's class : ")
# student_data(student_id, student_name, student_class)


'''
Q2. Write a Python class named Student with two attributes student_name, marks.
Modify the attribute values of the said class and print the original and modified values of the said attributes.
'''


# class Student:
#     def __init__(self, student_name, marks):
#         self.student_name = student_name
#         self.marks = marks


# student1 = Student("John", 45)

# print(f'The name of the student is {student1.student_name}. The marks he got {student1.marks}.')

# student1 = Student("Ram", 70)
# print(f'The name of the student is {student1.student_name}. The marks he got {student1.marks}.')


'''
Q3. Create a Class Named Student with Attributes and a Function to Display All Attributes and Values

Write a Python class named Student with two attributes: student_id, student_name. Add a new attribute: student_class.
Create a function to display all attributes and their values in the Student class.
'''


class Student:
    def __init__(self, student_id, student_name, student_class):
        self.student_id = student_id
        self.student_name = student_name
        self.student_class = student_class

    def display_data(self):
        print(f'The name of the student is {self.student_name}')
        print(f'The ID of the student is {self.student_id}')
        print(f'The class of the student is {self.student_class}')


student1 = Student(1, "Ram", 12)
student2 = Student(2, "Shyam", 11)

student1.display_data()
student2.display_data()
