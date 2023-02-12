# function

# non-returning functions
# in python every function by default returns None

# parameterless function
# function declaration / definition
def function1():
    print("inside function1")


# function call
# function1()


# parameterized function


def function2(p1):
    # param = 10
    print(f"inside function2")
    print(f"p1 = {p1}, type = {type(p1)}")


# function2(0)
# function2("test")
# function2(15.50)
# function2(True)


def function3(p1, p2, p3):
    print(f"inside function2")
    print(f"p1 = {p1}, type = {type(p1)}")
    print(f"p2 = {p2}, type = {type(p2)}")
    print(f"p3 = {p3}, type = {type(p3)}")


# function3(10, 10.50, "test")


# returning function
def add(p1, p2):
    result = p1 + p2

    # function is returning addition of two params
    return result


# capture the returned value from add function
addition = add(10, 20)
print(f"addition = {addition}, type = {type(addition)}")


# every variable MUST initialize with a value
# if a value is not avaialble at the time of declration
# use None in which case the data type of the variable
# will be set to NoneType
# num = None


def multiply(p1, p2):
    result = p1 * p2
    print(f"result = {result}")


def is_even(number):
    if number % 2 == 0:
        print("Yes")
    else:
        print("No")


def is_odd(number):
    if number % 2 != 0:
        print("Yes")
    else:
        print("No")
