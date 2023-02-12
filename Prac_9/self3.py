# operator overloading
# - giving more meaning to the default operators
# - like +, -, /, * etc.

class MyNumber:
    def __init__(self, number):
        self.number = number

    def __add__(self, other):
        return self.number + other.number

    def __sub__(self, other):
        return self.number - other.number


n1 = 100
n2 = 200

m1 = MyNumber(100)
m2 = MyNumber(200)

print(f"n1 + n2 = {n1.__add__(n2)}")
# n1 + n2 = 300
print(f"n1 + n2 = {n1 + n2}")
# n1 + n2 = 300

print()

print(f"m1 + m2 = {m1.__add__(m2)}")
# m1 + m2 = 300
print(f"m1 + m2 = {m1 + m2}")
# m1 + m2 = 300

print()

print(f"n1 - n2 = {n1.__sub__(n2)}")
# n1 - n2 = -100
print(f"n1 - n2 = {n1 - n2}")
# n1 - n2 = -100

print(f"m1 - m2 = {m1.__sub__(m2)}")
# m1 - m2 = -100
print(f"m1 - m2 = {m1 - m2}")
# m1 - m2 = -100

# Person.print_details(p1)
# p1.print_details()