# tuple
# - type conversion
#   - tuple: any collection to a tuple
#   - list: any collection to a list
#   - set: any collection to a set

def function1():
    # list
    numbers1 = [10, 20, 30, 40, 50]
    print(f"numbers1 = {numbers1}, type = {type(numbers1)}")

    # tuple
    numbers2 = (10, 20, 30, 40, 50)
    print(f"numbers2 = {numbers2}, type = {type(numbers2)}")

    # tuple
    numbers3 = 10, 20, 30, 40, 50
    print(f"numbers3 = {numbers3}, type = {type(numbers3)}")    

# function1()
# numbers1 = [10, 20, 30, 40, 50], type = <class 'list'>
# numbers2 = (10, 20, 30, 40, 50), type = <class 'tuple'>
# numbers3 = (10, 20, 30, 40, 50), type = <class 'tuple'>

def function2():
    t1 = 10, 20, 30, 40
    t2 = 50, 60, 70

    t3 = t1 + t2
    # This creates new tuple with contents from both t1 and t2
    print(t1)
    print(t2)
    print(t3)

# function2()
# (10, 20, 30, 40)
# (50, 60, 70)
# (10, 20, 30, 40, 50, 60, 70)

def function3():
    t1 = 10, 20, 30, 40, 50
    t2 = 1, 2, 3, 4, 5

    # this does not mean the t1 is getting updated
    # rather, the new memory will be allocated with contents of both t1 and t2
    # and will be referred by t1
    t1 = t1 + t2
    print(t1)

    # tuple is immutable and hence you can not perform these
    # operations like, append, extend, clear, remove, pop, sort etc

# function3()
# (10, 20, 30, 40, 50, 1, 2, 3, 4, 5)


def function4():
    # empty list
    list1 = []
    list2 = list()

    print(list1)
    print(list2)

    print()

    # empty tuple
    t1 = ()
    t2 = tuple()
    print(t1)
    print(t2)

    print()

    list3 = [10, 20, 30]
    print(f"list3 = {list3}, type = {type(list3)}")
    # list3.append(40)
    # list3.remove(20)

    # converting the list into a tuple
    t3 = tuple(list3)
    print(f"t3 = {t3}, type = {type(t3)}")

    # converting a tuple to a list
    list4 = list(t3)
    print(f"list4 = {list4}, type = {type(list4)}")
    # list4.append(40)


# function4()
# []
# []

# ()
# ()

# list3 = [10, 20, 30], type = <class 'list'>
# t3 = (10, 20, 30), type = <class 'tuple'>
# list4 = [10, 20, 30], type = <class 'list'>


def function5():
    # list with one value
    list1 = [10]
    print(f"list1 = {list1}, type = {type(list1)}")

    # tuple with one value
    t1 = (10, )
    # t1 = 10,
    print(f"t1 = {t1}, type = {type(t1)}")

    t2 = ('test', )
    # t2 = 'test',
    print(f"t2 = {t2}, type = {type(t2)}")

    t3 = tuple([10])
    print(f"t3 = {t3}, type = {type(t3)}")


# function5()
# list1 = [10], type = <class 'list'>
# t1 = (10,), type = <class 'tuple'>
# t2 = ('test',), type = <class 'tuple'>
# t3 = (10,), type = <class 'tuple'>