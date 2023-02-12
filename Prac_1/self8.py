# scope
# - global
# - local

# global variable
# - declared outside of
#   - function
#   - class
#   - block
num = 100
print(f"global num = {num}")
print()


def function1():
    print("inside function1")

    # local variable for function1
    num = 500
    print(f"global num = {num}")

    # local variable
    # - scope: limited to the function
    salary = 15.50
    print(f"salary = {salary}")


function1()


def function2():
    print("inside function2")

    # henceforth, consider num as global
    global num

    # will not declare a new local variable
    # update the global variable (num) value to 500
    num = 500
    print(f"num = {num}")


# function2()

print()
# print(f"outside of function1 salary = {salary}")
print(f"outside of function1, global num = {num}")

