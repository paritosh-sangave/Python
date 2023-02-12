# multi-level inheritance

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

class Employee(Person):
    def __init__(self, emp_id, name, age):
        Person.__init__(self, name, age)
        self.emp_id = emp_id

class Manager(Employee):
    def __init__(self, emp_id, name, age, department):
        Employee.__init__(self, emp_id, name, age)
        self.department = department