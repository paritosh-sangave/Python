class Person:
    def __init__(self, name, age):
        self.name = name
        self.__age = age
    
    def print_details(self):
        print(f"Name = {self.name}")
        print(f"Age = {self.__age}")

p1 = Person("Ian", 30)
# p1.print_details()
# Name : Ian
# Age : 30

print(p1.__dict__)
# {'_Person__name': 'Ian', '_Person__age': 30}


print(f"age = {p1.name}")
# age = Ian


# adding a new attribute with name __age
p1.__age = 50
print(f"age = {p1.__age}")
# age = 50


p1.print_details()
# Name = Ian
# Age = 30