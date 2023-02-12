# create two classes
# Employee: id, name
# Manager: id, name, department

class Employee:
    def __init__(self, id, name):
        self.id = id
        self.name = name

    def print_employee_details(self):
        print(f"name = {self.name}")
        print(f"id = {self.id}")


class Manager(Employee):
    def __init__(self, id, name, department):
        Employee.__init__(self, id, name)
        self.department = department

    def print_manager_details(self):
        Employee.print_employee_details(self)
        print(f"department = {self.department}")


e1 = Employee(1, 'Tatya')
e1.print_employee_details()
# name = Tatya
# id = 1

print()

m1 = Manager(2, 'Jugnoo', 'Finance')
m1.print_manager_details()
# name = Jugnoo
# id = 2
# department = Finance


# create two classes
# Vehicle: fuel_type [print_vehicle_details]
# Car: model, company [print_car_details]
