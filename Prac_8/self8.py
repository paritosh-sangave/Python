# hierarchical inheritance

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age


class Player(Person):
    def __init__(self, name, age, team):
        Person.__init__(self, name, age)
        self.team = team


class Employee(Person):
    def __init__(self, name, age, emp_id):
        Person.__init__(self, name, age)
        self.emp_id = emp_id


class Student(Person):
    def __init__(self, name, age, roll):
        Person.__init__(self, name, age)
        self.roll = roll


