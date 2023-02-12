# list operations

def function1():
    numbers = [10, 20, 30, 40, 50]
    print(numbers)

    # append only one item at the end
    # append does not return anything
    numbers.append(60)
    print(numbers)

    # append multiple values using extend
    # extend does not return anything
    numbers.extend([70, 80, 90, 100])
    print(numbers)


# function1()

# [10, 20, 30, 40, 50]
# [10, 20, 30, 40, 50, 60]
# [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]



def function2():
    numbers = [10, 20, 30, 40, 50]
    print(numbers)

    # insert value 15 in between 10 and 20
    # param1: position where you want to insert a value
    # param2: value to be inserted
    numbers.insert(1, 15)
    print(numbers)

    # insert value 25 between 20 and 30
    numbers.insert(3, 25)
    print(numbers)

    # insert value 35 between 30 and 40
    numbers.insert(5, 35)
    print(numbers)

    # insert value 45 between 40 and 50
    numbers.insert(7, 45)
    print(numbers)


# function2()

# [10, 20, 30, 40, 50]
# [10, 15, 20, 30, 40, 50]
# [10, 15, 20, 25, 30, 40, 50]
# [10, 15, 20, 25, 30, 35, 40, 50]
# [10, 15, 20, 25, 30, 35, 40, 45, 50]



def function3():
    numbers = [10, 20, 30, 40, 50]
    print(numbers)

    # pop: by default removes the last value
    # remove the last value
    value_deleted = numbers.pop()
    print(f"value deleted = {value_deleted}")
    print(numbers)

    # remove the last value
    value_deleted = numbers.pop()
    print(f"value deleted = {value_deleted}")
    print(numbers)


# function3()

# [10, 20, 30, 40, 50]
# value deleted = 50
# [10, 20, 30, 40]
# value deleted = 40
# [10, 20, 30]



def function4():
    numbers = [10, 20, 30, 40, 50]
    print(numbers)

    # removing a value in between using its index position
    # delete value 30 from second position
    numbers.pop(2)
    print(numbers)

    # delete value 50
    numbers.pop()
    print(numbers)

    # delete value 20
    numbers.pop(1)
    print(numbers)

    # delete value 10
    numbers.pop(0)
    print(numbers)

    # produces crash
    # numbers.pop(10)


# function4()

# 10, 20, 30, 40, 50]
# [10, 20, 40, 50]
# [10, 20, 40]
# [10, 40]
# [40]



def function5():
    numbers = [10, 20, 30, 40, 50]
    print(numbers)

    # delete value 30
    numbers.remove(30)
    print(numbers)

    numbers2 = [10, 20, 30, 40, 50, 10, 20, 30, 40, 50]
    print(numbers2)

    # the value 30 will be deleted from position 2
    # as the remove function removes only first ocurrance of the value
    numbers2.remove(30)
    print(numbers2)

    # remove will crash the application if the value to be deleted
    # does not exist in the collection
    # numbers2.remove(100)
    # print(numbers2)


# function5()

# [10, 20, 30, 40, 50]
# [10, 20, 40, 50]
# [10, 20, 30, 40, 50, 10, 20, 30, 40, 50]
# [10, 20, 40, 50, 10, 20, 30, 40, 50]



def function6():
    countries = ['india', 'usa', 'uk', 'china', 'japan']
    print(countries)

    # add a country named bhutan
    countries.append('bhutan')
    print(countries)

    # remove china by using index
    china_index = -1

    # start from 0 the last value in the collection
    for index in range(len(countries)):

        # check if the value at every position is china
        if countries[index] == 'china':

            # found china, store the index in china_index
            china_index = index

            # since we found the china's index there is no need
            # to continue further
            # break

    if china_index != -1:
        countries.pop(china_index)
        print(countries)

    for index in range(len(countries)):
        if countries[index] == 'uk':
            countries.pop(index)
            print(countries)
            break

    # remove usa by using remove
    countries.remove('usa')
    print(countries)


# function6()

# ['india', 'usa', 'uk', 'china', 'japan']
# ['india', 'usa', 'uk', 'china', 'japan', 'bhutan']
# ['india', 'usa', 'uk', 'japan', 'bhutan']
# ['india', 'usa', 'japan', 'bhutan']
# ['india', 'japan', 'bhutan']


def function7():
    countries = ['india', 'usa', 'uk', 'china', 'japan']
    print(countries)

    # find the index of china
    china_index = countries.index('china')
    print(f"china is present at {china_index}")

    # delete uk by using position

# function7()

# ['india', 'usa', 'uk', 'china', 'japan']
# china is present at 3

def function8():
    numbers = [10, 20, 30, 40, 50, 10, 20, 30, 40, 50, 10, 20, 30, 40, 50]

    # index function returns the index of first occurance
    # start searching value 10 from 0th position
    print(f"index of 10 = {numbers.index(10, 0)}")

    # start searching value 10 from 1st position
    print(f"index of 10 = {numbers.index(10, 1)}")

    # start searching value 10 from 6th position
    print(f"index of 10 = {numbers.index(10, 6)}")


# function8()

# index of 10 = 0
# index of 10 = 5
# index of 10 = 10


def function9():
    numbers = [10, 20, 30, 10, 50, 10, 20, 30, 10, 50, 10, 20, 30, 40, 50]

    # find out how many times 10 is repeated in the numbers
    print(f"value 10 is present {numbers.count(10)} times")

    # find out the position of value 10
    print(f"value 10 is present at {numbers.index(10)} position")

# function9()

# value 10 is present 5 times
# value 10 is present at 0 position


# find out all the ocurrances of a value from a collection
# find out on which positions the value 10 is present in the collection
# numbers = [10, 20, 30, 10, 50, 10, 20, 30, 10, 50, 10, 20, 30, 40, 50]
# hint:
# - find out the count of occurances
# - find out the index by using index() in a for loop


def function10():
    numbers = [10, 20, 30, 40, 50]
    print(numbers)

    # remove all values from numbers
    numbers.clear()
    print(numbers)

    # delete numbers collection
    del numbers
    # print(numbers)


# function10()

# [10, 20, 30, 40, 50]
# []


def function11():
    numbers = [20, 10, 50, 40, 30]
    print(numbers)

    # sort the numbers collection in asc order
    # sort does no return anything, rather it update the same
    # collection by changing the order of elements
    # numbers.sort()
    # print(numbers)

    # sort the collection in descending order
    numbers.sort(reverse=True)
    print(numbers)

    # not possible to sort a list with value of multiple data types
    # mixed = [10, 'india', 20, 'usa']
    # mixed.sort()
    # print(mixed)


# function11()

# [20, 10, 50, 40, 30]
# [50, 40, 30, 20, 10]


def function12():
    num1 = 10
    num2 = num1
    print(f"num1 = {num1}, num2 = {num2}")

    num1 = 30
    print(f"num1 = {num1}, num2 = {num2}")

    numbers1 = [20, 10, 40, 30, 50]

    # make a copy of numbers1
    numbers2 = numbers1.copy()
    print(numbers1)
    print(numbers2)

    # sorting the first collection
    numbers1.sort()
    print(numbers1)
    print(numbers2)


# function12()

# num1 = 10, num2 = 10
# num1 = 30, num2 = 10
# [20, 10, 40, 30, 50]
# [20, 10, 40, 30, 50]
# [10, 20, 30, 40, 50]
# [20, 10, 40, 30, 50]

