class Person:
    def __init__(self, name, address, age):
        self.__name = name
        self.__address = address
        self.__age = age

    def print_person_details(self):
        print(f"name = {self.__name}")
        print(f"address = {self.__address}")
        print(f"age = {self.__age}")


# Employee is-a Person
# Employee is derived from Person

class Employee(Person):
    def __init__(self, id, name, address, age, salary):
        super().__init__(name, address, age)
        self.__id = id
        self.__salary = salary

    def print_employee_details(self):
        print(f"id : {self.__id}")
        print(f"salary : {self.__salary}")
        super().print_person_details()


class Player(Person):
    def __init__(self, jersey_no, name, address, age, team, role):
        super().__init__(name, address, age)
        self.__jersey_no = jersey_no
        self.__team = team
        self.__role = role

    def print_player_details(self):
        super().print_person_details()
        print(f"Jerser no. = {self.__jersey_no}")
        print(f"Team = {self.__team}")
        print(f"Role = {self.__role}")


e1 = Employee(1, 'Tars', 'US', 24, 0)
e1.print_employee_details()
# id : 1
# salary : 0
# name = Tars
# address = US
# age = 24

p1 = Player(10, 'Mbappe', "Paris", 23, "PSG", 'Striker')
p1.print_player_details()
# name = Mbappe
# address = Paris
# age = 23
# Jerser no. = 10
# Team = PSG
# Role = Striker