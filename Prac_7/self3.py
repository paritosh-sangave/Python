# abstraction
# - hide the details of the object from outsider

# accessibility conventions
# - private
#   - attribute is declared with double underscores (__)
#   - can be accessed inside the class
#   - can not be accessed outside the class
#   - e.g. __age
# - public
#   - attribute is declared without any underscore (_)
#   - can be accessed outside the class
#   - e.g. name, address
# -

class Person:
    def __init__(self, name, address, age):
        # public access specifier
        self.name = name
        self.address = address

        # private
        self.__age = age

    def print_details(self):
        print('-' * 80)
        print(f"name = {self.name}")
        print(f"address = {self.address}")
        print(f"age = {self.__age}")
        print('-' * 80)

    def can_vote(self):
        if self.__age>=18:
            print(f"{self.name} is eligible for voting")
        else:
            print(f"{self.name} is NOT eligible for voting")

p1 = Person("Om", "Pune", 24)
p1.print_details()
p1.can_vote()
# --------------------------------------------------------------------------------
# name = Om
# address = Pune
# age = 24
# --------------------------------------------------------------------------------
# Om is eligible for voting



# can access the public attributes
# print(f"name = {p1.name}")
# print(f"address = {p1.address}")

# can NOT access the private attribute outside the class
# print(f"age = {p1.__age}")


# create a class named Car
# private: model, company price
# methods: print_details, can_afford

class Car:
    def __init__(self, model, company, price):
        self.__model = model
        self.__company = company
        self.__price = price

    def print_details(self):
        print(f"model = {self.__model}")
        print(f"company = {self.__company}")
        print(f"price = {self.__price}")
        print()

    # getter method
    def get_price(self):
        return self.__price

    # setter / mutator method
    def set_price(self, price):
        # validate price
        if price > 0:
            self.__price = price
        else:
            print(f"{price} is not valid price")

    def get_model(self):
        return self.__model

    def set_model(self, model):
        self.__model = model

    def get_company(self):
        return self.__company

    def set_company(self, company):
        self.__company = company

c1 = Car("Camry", "Toyota", 15)
c1.print_details()
# model = Camry
# company = Toyota
# price = 15


c1.set_model("Camry 2021")
c1.set_company("Toypta Endurance")
c1.set_price(18)
c1.print_details()
# model = Camry 2021
# company = Toypta Endurance
# price = 18

print(f"Company : {c1.get_company()}")
# Company : Toyota Endurance


# write a class named Employee
# attribute: name, id, salary
# methods: print_details, setters and getters

class Employee:
    def __init__(self, id, name, salary):
        self.__id = id
        self.__name = name
        self.__salary = salary
    
    def print_details(self):
        print(f"id : {self.__id}")
        print(f"Name : {self.__name}")
        print(f"Salary : {self.__salary}")

    def get_id(self):
        return self.__id

    def get_name(self):
        return self.__name
    
    def set_name(self, name):
        self.__name = name
    
    def get_salary(self):
        return self.__salary
    
    def set_salary(self, salary):
        self.__salary = salary

e1 = Employee(24, 'Aryton', '1000000')
e1.print_details()
# id : 24
# Name : Aryton
# Salary : 1000000