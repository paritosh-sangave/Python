# operator overloading

class Number:
    def __init__(self, number):
        self.number = number

    # converts the Number object to string
    def __str__(self):
        return f"{self.number}"

    # mathematical operators
    def __add__(self, other):
        result = self.number + other.number
        return Number(result)

    def __sub__(self, other):
        result = self.number - other.number
        return Number(result)

    def __mul__(self, other):
        result = self.number * other.number
        return Number(result)

    def __truediv__(self, other):
        result = self.number / other.number
        return Number(result)

    def __floordiv__(self, other):
        result = self.number // other.number
        return Number(result)

    def __pow__(self, other):
        result = self.number ** other.number
        return Number(result)

    def __mod__(self, other):
        result = self.number % other.number
        return Number(result)


# num1 = 10
# num2 = 20
# num3 = num1 + num2
# print(f"num1 = {num1}, type = {type(num1)}")
# print(f"num2 = {num2}, type = {type(num2)}")
# print(f"num3 = {num3}, type = {type(num3)}")

n1 = Number(10)
n2 = Number(20)
print(f"n1 = {n1}, n2 = {n2}")
# n1 = 10, n2 = 20


# n3 = Number.__add__(n1, n2)
# n3 = n1.__add__(n2)
n3 = n1 + n2
print(f"n1 = {n1}, type = {type(n1)}")
print(f"n2 = {n2}, type = {type(n2)}")
print(f"n3 = {n3}, type = {type(n3)}")
# n1 = 10, type = <class '__main__.Number'>
# n2 = 20, type = <class '__main__.Number'>
# n3 = 30, type = <class '__main__.Number'>


# n1.__sub__(n2)
print(f"n1 - n2 = {n1 - n2}")
# n1 - n2 = -10

# n1.__truediv__(n2)
print(f"n1 / n2 = {n1 / n2}")
# n1 / n2 = 0.5

# n1.__mul__(n2)
print(f"n1 * n2 = {n1 * n2}")
# n1 * n2 = 200

# n1.__pow__(n2)
print(f"n1 ** n2 = {n1 ** n2}")
# n1 ** n2 = 100000000000000000000

# n1.__mod__(n2)
print(f"n1 % n2 = {n1 % n2}")
# n1 % n2 = 10

# n1.__floordiv__(n2)
print(f"n1 // n2 = {n1 // n2}")
# n1 // n2 = 0
