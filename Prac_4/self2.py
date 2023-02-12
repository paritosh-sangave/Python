# Multidimensional collection: list, tuple

def func1():
    numbers1 = [10, 20, 30, 40, 50]
    print(numbers1)

    # 2 rows 2 columns
    numbers2 = [
        [10, 20], # row 0
        [30, 40]  # row 1
    ]
    print(numbers2)

    # 3 rows 5 columns
    numbers3 = [
        [10, 20, 30, 40, 50],       # row 0
        [60, 70, 80, 90, 100],      # row 1
        [110, 120, 130, 140, 150]   # row 2
    ]
    print(numbers3)

    numbers4 = [
        [10, 20],
        [30, 40, 50],
        [60, 70, 80, 90]
    ]
    print(numbers4)

# func1()
# [10, 20, 30, 40, 50]
# [[10, 20], [30, 40]]
# [[10, 20, 30, 40, 50], [60, 70, 80, 90, 100], [110, 120, 130, 140, 150]]
# [[10, 20], [30, 40, 50], [60, 70, 80, 90]]


def func2():
    # single dimensional list
    numbers = [10, 20, 30, 40, 50]

    # for...in or foreach loop
    for number in numbers:
        print(f"number = {number}")

    print()

    # traditional for loop
    # - get the values by using their index positions
    for index in range(len(numbers)):
        print(f"value at {index} = {numbers[index]}")

# func2()
# number = 10
# number = 20
# number = 30
# number = 40
# number = 50

# value at 0 = 10
# value at 1 = 20
# value at 2 = 30
# value at 3 = 40
# value at 4 = 50


def func3():
    numbers = [
        [10, 20],  # row 0
        [30, 40]   # row 1
    ]

    # traditional
    print(f"value stored at 0th index = {numbers[0]}")
    print(f"value stored at 0th index of 0th list = {numbers[0][0]}")
    print(f"value stored at 1th index of 0th list = {numbers[0][1]}")
    print(f"value stored at 0th index of 1st list = {numbers[1][0]}")
    print(f"value stored at 1st index of 1st list = {numbers[1][1]}")

    # standard for loop
    for row in range(len(numbers)):
        print(f"values at row {row}: {numbers[row]}")
        for col in range(len(numbers[row])):
            print(f"values at [{row}][{col}]: {numbers[row][col]}")
    print()

    # for... in loop
    for inner_list in numbers:
        print(inner_list)
        for number in inner_list:
            print(f"number = {number}")
    print()

# func3()
# value stored at 0th index = [10, 20]
# value stored at 0th index of 0th list = 10
# value stored at 1th index of 0th list = 20
# value stored at 0th index of 1st list = 30
# value stored at 1st index of 1st list = 40
# values at row 0: [10, 20]
# values at [0][0]: 10
# values at [0][1]: 20
# values at row 1: [30, 40]
# values at [1][0]: 30
# values at [1][1]: 40

# [10, 20]
# number = 10
# number = 20
# [30, 40]
# number = 30
# number = 40


def function4():
    numbers = [
        [10, 20],
        [30, 40, 50],
        [60, 70, 80, 90]
    ]

    # standard for loop
    for row_index in range(len(numbers)):
        row = numbers[row_index]
        print(row)
        for col_index in range(len(row)):
            print(f"value at {row_index}{col_index} = {row[col_index]}")
    print()

    # foreach
    for inner_list in numbers:
        print(f"inner_list = {inner_list}")
        for number in inner_list:
            print(f"value = {number}")
    print()

# function4()
# [10, 20]
# value at 00 = 10
# value at 01 = 20
# [30, 40, 50]
# value at 10 = 30
# value at 11 = 40
# value at 12 = 50
# [60, 70, 80, 90]
# value at 20 = 60
# value at 21 = 70
# value at 22 = 80
# value at 23 = 90

# inner_list = [10, 20]
# value = 10
# value = 20
# inner_list = [30, 40, 50]
# value = 30
# value = 40
# value = 50
# inner_list = [60, 70, 80, 90]
# value = 60
# value = 70
# value = 80
# value = 90

def func5():
    # list of tuples
    numbers = [
        (10, 20),
        (30, 40, 50),
        (60, 70, 80, 90)
    ]
    return numbers

# print(func5())
# [(10, 20), (30, 40, 50), (60, 70, 80, 90)]

def func6():
    # tuple of tuples
    numbers = (
        (10, 20),
        (30, 40, 50),
        (60, 70, 80, 90)
    )
    return numbers

# print(func6())
# ((10, 20), (30, 40, 50), (60, 70, 80, 90))

def func7():
    # tuple of lists
    numbers = (
        [10, 20],
        [30, 40, 50],
        [60, 70, 80, 90]
    )
    return numbers

# print(func7())
# ([10, 20], [30, 40, 50], [60, 70, 80, 90])


def func8():
    # tuple of lists
    numbers = (
        [10, 20],
        (30, 40, 50),
        [60, 70, 80, 90]
    )
    print(f"data type of numbers = {type(numbers)}")
    for inner_collection in numbers:
        print(f"data type of inner_collection = {type(inner_collection)}")

# func8()
# data type of numbers = <class 'tuple'>
# data type of inner_collection = <class 'list'>
# data type of inner_collection = <class 'tuple'>
# data type of inner_collection = <class 'list'>
