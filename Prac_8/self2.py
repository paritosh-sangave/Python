# a school has multiple students
# one-to-many relationship: one school has many students

class Student:
    def __init__(self, roll, name):
        self.__name = name
        self.__roll = roll

    def print_student_details(self):
        print(f"Roll = {self.__roll}")
        print(f"Name = {self.__name}")


class School:
    def __init__(self, name, address):
        self.__name = name
        self.__address = address

        # create a collection to keep multiple students
        self.__students = []

    def enroll_student(self, roll, name):
        student = Student(roll, name)
        # enroll new student
        self.__students.append(student)

    def print_school_details(self):
        print(f"Name = {self.__name}")
        print(f"Address = {self.__address}")
        print('-'*40)

        print("------Student Details------")
        for student in self.__students:
            student.print_student_details()
            print()

school1 = School('ABC', 'Pune')

# enroll a new student
school1.enroll_student(1, 'Rajesh')

# enroll a new student
school1.enroll_student(2, "Jignesh")

# enroll a new student
school1.enroll_student(3, "Kumar")

school1.print_school_details()

# Name = ABC
# Address = Pune
# ----------------------------------------
# ------Student Details------
# Roll = 1
# Name = Rajesh

# Roll = 2
# Name = Jignesh

# Roll = 3
# Name = Kumar
    