def function1():
    numbers = [10, 20, 30, 40, 50]
    print(numbers)
    print(f"number of values in numbers: {len(numbers)}")

    # for..in loop
    for number in numbers:
        print(f"number = {number}, square = {number ** 2}")


# function1()


def function2():
    positions = [1, 2, 3, 4, 5]
    names = []
    for position in positions:
        name = input(f"enter name {position}: ")
        names.append(name)
    print(names)


# function2()


def function3():
    # param1: start value [default as 0]
    # param2: stop value [excluded from the generated collection]
    # param3: step [default as 1]
    # positions = list(range(1, 21, 1))
    # print(positions)

    # positions = list(range(1, 21, 2))
    # print(positions)

    # positions = list(range(0, 10))
    # print(positions)

    # positions = list(range(10))
    # print(positions)

    names = []
    for position in range(5):
        name = input(f"enter name {position}: ")
        names.append(name)

# function3()


def function4():
    numbers1 = [10, 20, 30, 40, 50]
    numbers2 = [60, 70, 80, 90, 100]

    # numbers1.append(numbers2)
    # for number in numbers2:
    #     numbers1.append(number)
    numbers1.extend(numbers2)

    print(numbers1)
    print(len(numbers1))


# function4()


def function5():
    numbers = []
    results = []

    numbers1 = [10, 20, 30, 40, 50]
    numbers2 = [60, 70, 80, 90, 100]

    # add all values from numbers1 and numbers2 to numbers
    numbers.extend(numbers1)
    numbers.extend(numbers2)
    print(numbers)

    # add individual values from numbers1 and numbers2 and put the result in results
    # print(f"0th value from numbers1 = {numbers1[0]}, numbers2 = {numbers2[0]}")
    # print(f"1st value from numbers1 = {numbers1[1]}, numbers2 = {numbers2[1]}")

    print(numbers1)
    print(numbers2)
    # print(f"addition of values at 0th position: {numbers1[0] + numbers2[0]}")
    # print(f"addition of values at 1st position: {numbers1[1] + numbers2[1]}")

    for index in range(5):
        result = numbers1[index] + numbers2[index]
        results.append(result)
    print(results)

    # subtract individual values from numbers1 and numbers2 and put the result in results
    results = []
    for i in range(5):
        result = numbers1[i] - numbers2[i]
        results.append(result)
    print(results)

    # multiply individual values from numbers1 and numbers2 and put the result in results
    results = []
    for i in range(5):
        result = numbers1[i] * numbers2[i]
        results.append(result)
    print(results)

function5()