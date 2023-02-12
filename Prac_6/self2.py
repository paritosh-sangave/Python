# class
# - entity which binds the data and functions together
# - collection of data members (attributes) and member functions
# - template to create an object
# - blueprint to create an object
# - logical entity
# - example: name, address and age are the data member while
#            can_vote and print_details are the member functions

# object
# - instance of a class
# - takes real memory to store the attributes
# - when you create an object every time a new memory will get allocated
# - every object can be uniquely identifyable by using its memory address

# empty class
class Person:
    pass

# create object of class Person
p1 = Person()
print(f"p1 = {p1}, type = {type(p1)}")
# p1 = <__main__.Person object at 0x000001B185F3B280>, type = <class '__main__.Person'>


# add an attribute inside the p1 object
setattr(p1, 'name', 'Babu Bhaiya')
setattr(p1, 'address', 'mumbai')
setattr(p1, 'age', 62)

# get attribute inside p1 object
print(f"name = {getattr(p1, 'name')}")
print(f"address = {getattr(p1, 'address')}")
print(f"age = {getattr(p1, 'age')}")
# name = Babu Bhaiya
# address = mumbai
# age = 62

# you cannot get value of any attribute which is not present in object
# print(f"email = {getattr(p1, 'email')}")


# create an empty class name Car
class Car:
    pass

# add attributes: model, company, price
c1 = Car()
setattr(c1, 'model', 'nano')
setattr(c1, 'company', 'tata')
setattr(c1, 'price', 2.5)
# print(f"c1 = {c1}, type = {type(c1)}")

c2 = Car()
setattr(c2, 'model', 'carens')
setattr(c2, 'company', 'kia')
setattr(c2, 'price', 22)
# print(f"c2 = {c2}, type = {type(c2)}")

# how many object will be created here
# two objects are having references
# c3 = Car()
# c4 = Car()

# anonymous objects
# - do not have any references
# Car()
# Car()
# Car()
