# write a class named Employee
# attributes: employee_id, name, address, email, salary
# method: print_details, draw_salary, send_email

class Employee:
    def __init__(self, id, name, salary, address='', email=""):
        setattr(self, 'id', id)
        setattr(self, 'name', name)
        setattr(self, 'salary', salary)
        setattr(self, 'address', address)
        setattr(self, 'email', email)

    def print_details(self):
        print(f"id: {getattr(self, 'id')}")
        print(f"name: {getattr(self, 'name')}")
        print(f"address: {getattr(self, 'address')}")
        print(f"email: {getattr(self, 'email')}")
        print(f"salary: {getattr(self, 'salary')}")

    def update_salary(self, diff):
        setattr(self, 'salary', self.salary+diff)
        print(f"Salary updated to {self.salary}")

e1 = Employee(1, 'Emp1', 50000)
e1.print_details()
# id: 1
# name: Emp1
# address:
# email:
# salary: 50000
print()

e1.update_salary(5000)
# Salary updated to 55000
print()

e1.print_details()
# id: 1
# name: Emp1
# address:
# email:
# salary: 55000

# create a class name School
# attrs: name, address
# methods: print_details

class School:
    def __init__(self, name, address):
        setattr(self, 'name', name)
        setattr(self, 'address', address)

    def print_details(self):
        print(f"Name : {getattr(self, 'name')}")
        print(f"Address : {self.address}")

s1 = School('ABC', 'Pune')
s1.print_details()
# Name : ABC
# Address : Pune