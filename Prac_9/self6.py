# access specifier conventions
# - private
#   - using two underscores as suffix to declare an attribute as private
#   - can be accessed only within the same class
#   - CAN NOT be accessed outside the same class
#   - e.g. __name
# - protected
#   - use one underscore as suffix to declare an attribute as protected
#   - SHOULD NOT be accessed outside the same class or child class(es)
#   - e.g. _name or _age
# - public
#   - no underscore to declare an attribute as public
#   - can be accessed anywhere (inside or outside the class)
#   - e.g. age

class Person:
    def __init__(self, name, age):
        self._name = name
        self._age = age

    def print_details(self):
        print(f"name = {self._name}")
        print(f"age = {self._age}")


class Employee(Person):
    def __init__(self, emp_id, name, age, salary):
        Person.__init__(self, name, age)
        self._emp_id = emp_id
        self._salary = salary

    def print_details(self):
        print(f"id = {self._emp_id}")
        print(f"name = {self._name}")
        print(f"age = {self._age}")
        print(f"salary = {self._salary}")


class Manager(Employee):
    def __init__(self, emp_id, name, age, salary, department):
        Employee.__init__(self, emp_id, name, age, salary)
        self._department = department

    def print_details(self):
        # _emp_id, _salary => Employee
        # _name, _age => Person
        print(f"id = {self._emp_id}")
        print(f"name = {self._name}")
        print(f"age = {self._age}")
        print(f"salary = {self._salary}")
        print(f"department = {self._department}")


# e1 = Employee(1, "emp1", 24, 23000)
# print(e1.__dict__)
# e1.print_details()

m1 = Manager(1, 'manager 1', 50, 60000, 'HR')
print(m1.__dict__)
m1.print_details()
# {'_name': 'manager 1', '_age': 50, '_emp_id': 1, '_salary': 60000, '_department': 'HR'}
# id = 1
# name = manager 1
# age = 50
# salary = 60000
# department = HR



# class Test:
#     def __init__(self, number):
#         self._number = number
#
#
# t = Test(100)

# do not access _number (protected) outside Test class
# print(f"number = {t._number}")
