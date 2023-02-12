# class
# - data members: attributes
# - member functions: methods

# self
# - it is NOT a keyword
# - convetionlly the first parameter of every method is named as self
# - self is always of type of same class
# - same as 'this' in other languages like C++ or Java


class Person:
    def set_attributes(self, name, address, age):
        setattr(self, 'name', name)
        setattr(self, 'address', address)
        setattr(self, 'age', age)

    def can_vote(self):
        age = getattr(self, 'age')
        if age>=18:
            print(f"{getattr(self, 'name')} is eligible for voting")
        else: 
            print(f"{getattr(self, 'name')} is NOT eligible for voting")

    def print_details(self):
        print(f"name: {getattr(self, 'name')}")
        print(f"address: {getattr(self, 'address')}")
        print(f"age: {getattr(self, 'age')}")

p1 = Person()
p1.set_attributes('Raaju', 'Pune', 30)
p1.print_details()
p1.can_vote()
# name: Raaju
# address: Pune
# age: 30
# Raaju is eligible for voting

print()

p2 = Person()
p2.set_attributes('Shyam', 'Mumbai', 29)
p2.print_details()
p2.can_vote()
# name: Shyam
# address: Mumbai
# age: 29
# Shyam is eligible for voting


# create a class named Car with attributes model, company and price
# with methods: set_attributes, print_details and can_afford

class Car:
    def set_attributes(self, model, company, price):
        setattr(self, 'model', model)
        setattr(self, 'company', company)
        setattr(self, 'price', price)

    def print_details(self):
        print(f"model: {getattr(self, 'model')}")
        print(f"company: {getattr(self, 'company')}")
        print(f"price: {getattr(self, 'price')}")

    def can_afford(self):
        if getattr(self, 'price') >= 2000000:
            print(f"{getattr(self, 'company')} {getattr(self, 'model')} is NOT affordable")
        else:
            print(f"{getattr(self, 'company')} {getattr(self, 'model')} is affordable")


car1 = Car()
car1.set_attributes('W13', "Mercedes", 14000000)
car1.print_details()
car1.can_afford()
# model: W13
# company: Mercedes
# price: 14000000
# Mercedes W13 is NOT affordable