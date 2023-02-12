class Person:
    def __init__(self, name, address, age):
        self.name = name
        self.age = age
        self.address = address

    def can_vote(self):
        if self.age>=18:
            print(f"{self.name} can vote")
        else:
            print(f"{self.name} can NOT vote")
    
    def print_details(self):
        print(f"name = {self.name}")
        print(f"address = {self.address}")
        print(f"age = {self.age}")

p1 = Person('Ambaani', 'Antila', 65)
p1.print_details()
p1.can_vote()

