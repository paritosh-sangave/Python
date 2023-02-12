# every subclass has to create an object of super class within itself

class Person:
    def __init__(self, name, address):
        self.name = name
        self.address = address


# Employee is derived from Person
# Person is super class of Employee
# Employee is subclass of Person
# Employee is-a Person


class Employee(Person):
    def __init__(self, id, name, address, email, salary):
        # create an object of super (Person) class object
        Person.__init__(self, name, address)
        self.email = email
        self.id = id
        self.salary = salary


class Student(Person):
    def __init__(self, roll, name, address, marks):
        Person.__init__(self, name, address)
        self.roll = roll
        self.marks = marks


p1 = Person('Bobby', 'Goa')
print(f"p1 = {p1.__dict__}")
# p1 = {'name': 'Bobby', 'address': 'Goa'}


e1 = Employee(1, 'Anna', 'Mumbai', 'avn@abc.co', 45000)
print(f"e1 = {e1.__dict__}")
# e1 = {'name': 'Anna', 'address': 'Mumbai', 'email': 'avn@abc.co', 'id': 1, 'salary': 45000}

print(f"base class for Employee = {Employee.__base__}")
# base class for Employee = <class '__main__.Person'>