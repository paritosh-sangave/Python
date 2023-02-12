class Number:
    def __init__(self, number):
        self.value = number

    def __str__(self):
        return str(self.value)

    def __gt__(self, other):
        print(self)
        print(other)
        return self.value > other.value
        # if self.value > other.value:
        #     return True
        # else:
        #     return False

    def __ge__(self, other):
        return self.value >= other.value

    def __lt__(self, other):
        return self.value < other.value

    def __le__(self, other):
        return self.value <= other.value

    def __eq__(self, other):
        return self.value == other.value

    def __ne__(self, other):
        return self.value != other.value


n1 = Number(10)
n2 = Number(20)

# Number.__gt__(n1, n2)
# n1.__gt__(n2)
print(f"n1 > n2 = {n1 > n2}")
# 10
# 20
# n1 > n2 = False


# n1.__lt__(n2)
print(f"n1 < n2 = {n1 < n2}")
# n1 < n2 = True


# n1.__ge__(n2)
print(f"n1 >= n2 = {n1 >= n2}")
# n1 >= n2 = False


# n1.__le__(n2)
print(f"n1 <= n2 = {n1 <= n2}")
# n1 <= n2 = True


# n1.__eq__(n2)
print(f"n1 == n2 = {n1 == n2}")
# n1 == n2 = False


# n1.__ne__(n2)
print(f"n1 != n2 = {n1 != n2}")
# n1 != n2 = True