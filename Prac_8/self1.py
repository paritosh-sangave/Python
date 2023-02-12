# write classes
# - Student: name, roll, marks
# - School: name, address, phone, email
# one-to-one relationship: one school has one student

class Student:
    def __init__(self, roll, name, marks):
        self.__roll = roll
        self.__name = name
        self.__marks = marks

    def print_student_details(self):
        print(f"Name = {self.__name}")
        print(f"Roll = {self.__roll}")


class School:
    def __init__(self, name, address, phone, email):
        self.__name = name
        self.__address = address
        self.__phone = phone
        self.__email = email
    
        # create an empty student
        self.__student = None

    def enroll_student(self, name, roll, marks):
        # composition
        # create a new student with given details
        self.__student = Student(roll, name, marks)

    def add_student(self, student):
        # aggregation
        self.__student = student
    
    def print_school_details(self):
        print(f"name : {self.__name}")
        print(f"address : {self.__address}")
        print(f"phone : {self.__phone}")
        print(f"email : {self.__email}")

        print("------------Student Details-----------")
        self.__student.print_student_details()

school = School("school1", "pune", "school1@test.com", "+912343242344")
# school.enroll_student("student1", 1, 20)

# create a student object
student = Student(1, "student 1", 10)

# add a student to school
school.add_student(student)

# add a student to school
school.add_student(student)