# class: Person
# attrs: name, address, age
# methods: initializer, can_vote, print_details

class Person:
    def __init__(self, name, address, age):
        setattr(self, 'name', name)
        setattr(self, 'address', address)
        setattr(self, 'age', age)

    def print_details(self):
        print(f"Name : {getattr(self, 'name')}")
        print(f"Address : {self.address}")
        print(f"Age : {self.age}")

    def can_vote(self):
        if getattr(self, 'age')>=18:
            print(f'{self.name} can vote')
        else:
            print(f"{getattr(self, 'name')} can NOT vote")

p1 = Person('Person1', 'Pune', 31)
p1.print_details()
p1.can_vote()
# Name : Person1
# Address : Pune
# Age : 31
# Person1 can vote

p2 = Person('Person2', 'Kolhapur', 17)
p2.print_details()
p2.can_vote()
# Name : Person2
# Address : Kolhapur
# Age : 17
# Person2 can NOT vote