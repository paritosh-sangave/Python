# one company has many employees

class Employee:
    def __init__(self, id, name):
        self.__id = id
        self.__name = name
    
    def print_emp_details(self):
        print(f"id = {self.__id}")
        print(f"Name = {self.__name}")


class Company:
    def __init__(self, name, address):
        self.__name = name
        self.__address = address
        # creating list of employees
        self.__employees = []

    def recruit_employee(self, id, name):
        emp = Employee(id, name)
        self.__employees.append(emp)

    def print_company_details(self):
        print(f"name = {self.__name}")
        print(f"address = {self.__address}")
        print()
        print("-- employee details --")
        for employee in self.__employees:
            employee.print_emp_details()
            print()

company = Company('LMN Corp.', 'pune')

# recruit an employees
company.recruit_employee(1, 'Binod')
company.recruit_employee(2, 'Mogambo')
company.recruit_employee(3, 'Rahul')
company.recruit_employee(4, 'Gabru')

company.print_company_details()
# name = LMN Corp.
# address = pune

# -- employee details --
# id = 1
# Name = Binod

# id = 2
# Name = Mogambo

# id = 3
# Name = Rahul

# id = 4
# Name = Gabru

class Player:
    def __init__(self, name, age):
        self.__name = name
        self.__age = age
    
    def print_player_details(self):
        print(f"Name : {self.__name}")
        print(f"Age : {self.__age}")

class Team:
    def __init__(self, name):
        self.__name = name
        self.__players = []

    def add_player(self, name, age):
        player = Player(name, age)
        self.__players.append(player)

    def print_details(self):
        print(f"name = {self.__name}")
        print("-- player details --")
        for player in self.__players:
            player.print_player_details()

team = Team("Indian Cricket Team")
team.add_player("Virat Kohli", 31)
team.add_player("Rishabh Pant", 28)
team.add_player("Jasprit Bumrah", 28)
team.print_details()