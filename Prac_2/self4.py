def func1():
    #empty list
    list1 = []
    print(f"list1 = {list1}, type = {type(list1)}")

# func1()
# list1 = [], type = <class 'list'>


def add(n1, n2):
    return n1 + n2

def subtract(n1, n2):
    return n1 - n2


def func2():
    # list of numbers
    numbers = [10, 20, 30, 40, 10, 20, 30, 40, 10, 20, 30, 40, 10, 20, 30, 40]
    print(f"numbers = {numbers}, type = {type(numbers)}")

    # list strings 
    countries = ['india', 'usa', 'uk', 'japan']
    print(f"countries = {countries}, type = {type(countries)}")

    # mixed values list
    mixed = [10, 'india', True, '20', 'uk', False]
    print(f"mixed = {mixed}, type = {type(mixed)}")

    # list of function references
    functions1 = [add, subtract, print]
    print(f"functions1 = {functions1}")

    functions2 = [add(10, 20), subtract(30,60), print('Element')]
    print(f"functions2 : {functions2}")

# func2()
# numbers = [10, 20, 30, 40, 10, 20, 30, 40, 10, 20, 30, 40, 10, 20, 30, 40], type = <class 'list'>
# countries = ['india', 'usa', 'uk', 'japan'], type = <class 'list'>
# mixed = [10, 'india', True, '20', 'uk', False], type = <class 'list'>
# functions1 = [<function add at 0x00000201AAFDDF70>, <function subtract at 0x00000201AAFE9040>, <built-in function print>]
# Element
# functions2 : [30, -30, None]


def append_demo():
    # list of numbers
    numbers = []
    print(numbers)

    # append a value
    numbers.append(11)
    print(numbers)

    numbers.append(19)
    print(numbers)

    numbers.append(42)
    print(numbers)

# append_demo()

# []
# [11]
# [11, 19]
# [11, 19, 42]



def function4():
    # get input from user
    name = input("Enter your name: ")
    print(f"Name : {name}, type : {type(name)}")

    age = int(input("Enter age : "))
    print(f"Age = {age}, type : {type(age)}")
    if age >= 18:
        print("Can vote")
    else:
        print("Cannot Vote")

# function4()

# Enter your name: ABC
# Name : ABC, type : <class 'str'>
# Enter age : 34
# Age = 34, type : <class 'int'>
# Can vote



def function5():
    # create an empty list
    names = []

    # get input from user for 5 user names and append them to the collection
    name1 = input("enter first name: ")
    names.append(name1)

    name2 = input("enter second name: ")
    names.append(name2)

    name3 = input("enter third name: ")
    names.append(name3)

    name4 = input("enter forth name: ")
    names.append(name4)

    name5 = input("enter fifth name: ")
    names.append(name5)

    print(names)

# function5()

# enter first name: AB
# enter second name: CD
# enter third name: EF
# enter forth name: GH
# enter fifth name: IJ
# ['AB', 'CD', 'EF', 'GH', 'IJ']