# polymorphism
# - static
#   - function/method overloading
#     - multiple functions having same name with one of the following
#       - different number of paramters
#       - different data types of parameters
#       - different order of parameters
# - dynamic
#   - run-time polymorphism
#   - method overriding
#   - having same method name in both base and derived class
#   - used to invoke the method from the type of object

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def print_details(self):
        print(f"--print_details method in Person class")
        print(f"name = {self.name}")
        print(f"age = {self.age}")


class Student(Person):
    def __init__(self, roll, name, age):
        Person.__init__(self, name, age)
        self.roll = roll

    # Student class is overriding the print_details method
    def print_details(self):
        print(f"--print_details method in Student class")

        # way to call super class method
        Person.print_details(self)
        print(f"roll = {self.roll}")


s1 = Student(1, 'student 1', 20)
s1.print_details()
# -- method called from Student class
# -- method called from Person class
# name = student 1
# age = 20
# roll = 1

# p1 = Person('person1', 30)
# p1.print_details()
# -- method called from Student class
# -- method called from Person class
# name = person1
# age = 30


class Animal:
    def __init__(self, name):
        self.name = name

    def make_sound(self):
        print(f"{self.name} is making sound...")


class Dog(Animal):
    def __init__(self):
        Animal.__init__(self, "dog")

    def make_sound(self):
        print(f"dog says woff woff..")


class Cat(Animal):
    def __init__(self):
        Animal.__init__(self, 'Cat')

    def make_sound(self):
        print(f"cat says mew mew..")


# d1 = Dog()
# d1.make_sound()
#
# c1 = Cat()
# c1.make_sound()


class Teacher:
    def __init__(self, name):
        self.name = name

    def print_details(self):
        print(f"method is called from Teacher")


class LabAssistant:
    def __init__(self, name):
        self.name = name

    def print_details(self):
        print(f"method is called from LabAssistant")


class TeacherLabAssistant(LabAssistant, Teacher):
    def __init__(self, name):
        Teacher.__init__(self, name)
        LabAssistant.__init__(self, name)

    def print_details(self):
        print(f"method called from TeacherLabAssistant")


# t1 = Teacher('teacher1')
# t1.print_details()

print()

# la1 = LabAssistant('lab assistant1')
# la1.print_details()

print()

# tla1 = TeacherLabAssistant('teacher lab assistant 1')
# tla1.print_details()


# a employee and player class must print all the required details by using
# same method (print_details)
# Employee: name, age, email, salary, id
# Player: name, age, team

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def print_details(self):
        print(f"name = {self.name}")
        print(f"age = {self.age}")


class Employee(Person):
    def __init__(self, emp_id, name, age, email, salary):
        Person.__init__(self, name, age)
        self.emp_id = emp_id
        self.email = email
        self.salary = salary

    def print_details(self):
        Person.print_details(self)
        print(f"emp id = {self.emp_id}")
        print(f"email = {self.email}")
        print(f"salary = {self.salary}")


class Player(Person):
    def __init__(self, name, age, team):
        Person.__init__(self, name, age)
        self.team = team

    def print_details(self):
        Person.print_details(self)
        print(f"team = {self.team}")

