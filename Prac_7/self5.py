class Person:
    def __init__(self, name, age, city, state, country, zipcode):
        self.__name = name
        self.__age = age
        self.__city = city
        self.__state = state
        self.__country = country
        self.__zipcode = zipcode

    def print_details(self):
        print(f"name = {self.__name}")
        print(f"age = {self.__age}")
        print(f"city = {self.__city}")
        print(f"state = {self.__state}")
        print(f"country = {self.__country}")
        print(f"zipcode = {self.__zipcode}")


class House:
    def __init__(self, rooms, city, state, country, zipcode):
        self.__rooms = rooms
        self.__city = city
        self.__state = state
        self.__country = country
        self.__zipcode = zipcode

    def print_details(self):
        print(f"rooms = {self.__rooms}")
        print(f"city = {self.__city}")
        print(f"state = {self.__state}")
        print(f"country = {self.__country}")
        print(f"zipcode = {self.__zipcode}")


class Address:
    def __init__(self, city, state, country, zipcode):
        self.__city = city
        self.__state = state
        self.__country = country
        self.__zipcode = zipcode

    def print_address(self):
        print(f"city = {self.__city}")
        print(f"state = {self.__state}")
        print(f"country = {self.__country}")
        print(f"zipcode = {self.__zipcode}")


class Person:
    def __init__(self, name, age, city, state, country, zipcode):
        self.__name = name
        self.__age = age
        # add an object of Address class with required details
        self.__person_address = Address(city, state, country, zipcode)

    def print_details(self):
        print(f"name = {self.__name}")
        print(f"age = {self.__age}")
        self.__person_address.print_address()


class Bank:
    def __init__(self, name, city, state, country, zipcode):
        self.__name = name
        self.__address = Address(city, state, country, zipcode)


# create an object of Person
p1 = Person("person1", 20, "pune","MH", "India", 414100)

# create an object of House
h1 = House(4, "mumbai", "MH", "India", 433433)


class Engine:
    def __init__(self, type, fuel):
        self.type = type
        self.fuel = fuel

    def print_engine_details(self):
        print(f"type = {self.type}")
        print(f"fuel = {self.fuel}")

class Car:
    def __init__(self, model, engine_type, engine_fuel):
        self.model = model
        # Engine(engine_type, engine_fuel): object of Engine class
        self.engine = Engine(engine_type, engine_fuel)

    def print_details(self):
        print(f"model = {self.model}")
        self.engine.print_engine_details()


class Bike:
    def __init__(self, model, engine_type, engine_fuel):
        self.model = model
        self.engine = Engine(engine_type, engine_fuel)

    def print_details(self):
        print(f"model = {self.model}")
        self.engine.print_engine_details()


c1 = Car('car1', 'car', 'petrol')
print(c1.__dict__)
# {'model': 'car1', 'engine': <__main__.Engine object at 0x00000202BD1434C0>}

c1.print_details()
# model = car1
# type = car
# fuel = petrol


# create two classes: School and Student
# School: name, address
# Student: roll, name, age
# create a relationship like: School has-a Student

class Student:
    def __init__(self, roll, name, age):
        self.roll = roll
        self.name = name
        self.age = age

    def print_details(self):
        print(f"name: {self.name}")
        print(f"age: {self.age}")
        print(f"roll: {self.roll}")


class School:
    def __init__(self, name, address, student_roll, student_name, student_age):
        self.name = name
        self.address = address

        # School has-a Student
        self.student = Student(student_roll, student_name, student_age)

    def print_school_details(self):
        print(f"name = {self.name}")
        print(f"address = {self.address}")
        print("--- student details ---")
        self.student.print_details()

# create two classes:
# Bank: name, address,
# Account: id, name, amount
# relationship: Bank has-an Account

# create two classes:
# Employee: id, name, address, email
# Company: name, address, phone
# relationship: Company has-en Employee