# function
# - when code gets compiled, the function gets converted into
#   a variable storing an address of function object (which has
#   the function body

# method
# - known as oop function
# - a method will be referred by a reference
# - every method gets added in the class as an attribute


class Person:
    def __init__(self, name):
        self.__name = name

    def print_details(self):
        print(f"name = {self.__name}")


# p1 = Person('person1')
# p1.print_details()
# p1.test_method()


# test_function
# - reference to the function object (having function body)
def test_function():
    print("inside test_function")


print(f"test_function = {test_function}")
# test_function = <function test_function at 0x00000201D0DEDE50>

test_function()
# inside test_function

# num1 = 100
# num2 = num1

# function alias
# - function reference
my_test_function = test_function
my_test_function()
# inside test_function


my_test_function2 = my_test_function
my_test_function2()
# inside test_function
