# __init__
# - this is called as initializer in python
# - it is also known as constructor in other languages
# - used to initialize the object
# - gets called implicitly for every object created
# - you MUST NOT call this method explicitly *

class Mobile:
    # will get called automatically
    # when a new object is created
    def __init__(self):
        print("inside __init__")
        setattr(self, 'model', "") 
        # empty string set by default
        setattr(self, "company", '')
        # empty string set by default


    def set_attributes(self, model, company):
        setattr(self, 'model', model)
        setattr(self, 'company', company)

    def print_details(self):
        print(f"model: {getattr(self, 'model')}")
        print(f"company: {getattr(self, 'company')}")
    
m1 = Mobile()
# inside __init__

m1.set_attributes('S22', 'Samsung')
m1.print_details()
# model: S22
# company: Samsung


class Person:
    # parameterized initializer
    def __init__(self, name='', address='', age=0):
        setattr(self, 'name', name)
        setattr(self, 'address', address)
        setattr(self, 'age', age)

    def print_details(self):
        print(f"name = {getattr(self, 'name')}")
        print(f"address = {getattr(self, 'address')}")
        print(f"age = {getattr(self, 'age')}")

p1 = Person('Shyam', 'Pune', 30)
p1.print_details()
# name = Shyam
# address = Pune
# age = 30

p2 = Person('Chotta Bheem', 'Dholakpur')
p2.print_details()
# name = Chotta Bheem
# address = Dholakpur
# age = 0

p3 = Person('Random')
p3.print_details()
# name = Random
# address =
# age = 0