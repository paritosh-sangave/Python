# object class
# - in python, every class is derived from object directly or indirectly
# - in python, object class is called as root class
# - this change is added in version 3.x
# - this class add many methods inside every class responsible for
#   - memory management (reference counting)
#   - string conversion
#   - copy object ...


# class Car:
# class Car():
class Car(object):
    def __init__(self, model, company):
        self.model = model
        self.company = company

    # overriding the str method to convert the car object to string
    def __str__(self):
        return f"Car--\n[model: {self.model}]\n[company: {self.company}]"


print(f"base class for Car class = {Car.__base__}")

c1 = Car('i20', 'Hyundai')
# print(f"c1 = {c1}, type = {type(c1)}")
# print(c1.__str__())
print(c1)
# Car--
# [model: i20]
# [company: Hyundai]


num = 100
# print(f"num = {num}, type = {type(num)}")
# print(num.__str__())
print(num)

# write a class named Mobile with model, company and price
# create an object and print using print()
# should print: Mobile [model: '', company: '', price: 0]
class Mobile:
    def __init__(self, model, company, price):
        self.model = model
        self.company = company
        self.price = price

    def __str__(self):
        return f"Mobile [model: {self.model}, company: {self.company}, price: {self.price}]"


m1 = Mobile("iphone", "apple", 144000)
print(m1)
# Mobile [model: iphone, company: apple, price: 144000]