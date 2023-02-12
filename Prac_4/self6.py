# variable length arguments function

def add(*nums):
    # nums is not a pointer
    # it is a symbol to denote that the function can accept any number of positional parameters
    print("inside add function")
    print(f"nums = {nums}, type = {type(nums)}")
    addition = 0
    for value in nums:
        addition += value
    print(f"addition = {addition}")
    print()

# add(10)
# add(10, 20)
# add(10, 20, 30)
# add(10, 20, 30, 40)
# add(10, 20, 30, 40, 50)


def my_function(*args, **kwargs):
    # args: collects all the positional parameters (tuple)
    # kwargs: collects all the named parameters (dictionary)
    print("inside my_function")
    print(f"args = {args}, type = {type(args)}")
    print(f"kwargs = {kwargs}, type = {type(kwargs)}")
    if kwargs.get('operation') == 'add':
        result = 0
        for value in args:
            result += value
        print(f"addition = {result}")
    elif kwargs.get('operation') == 'multiply':
        result = 1
        for value in args:
            result *= value
        print(f"multiplication = {result}")


# my_function(10, 20, operation="add")
# inside my_function
# args = (10, 20), type = <class 'tuple'>
# kwargs = {'operation': 'add'}, type = <class 'dict'>
# addition = 30

# my_function(10, 20, operation="multiply")
# inside my_function
# args = (10, 20), type = <class 'tuple'>
# kwargs = {'operation': 'multiply'}, type = <class 'dict'>
# multiplication = 200