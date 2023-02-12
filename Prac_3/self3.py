# list slicing
# parameters: 
# lower bound (start) (0)
# step count (1)

def func1():
    numbers = [10, 20, 30, 40, 50]

    # save numbers from index 1 to 3 in another list
    list1 = []
    for i in range(1,4):
        list1.append(numbers[i])

    print(numbers)
    print(list1)

# func1()
# [10, 20, 30, 40, 50]
# [20, 30, 40]



def function2():
    numbers = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]

    # [30, 40, 50, 60]
    print(f"values from 2 to 5th = {numbers[2:6]}")

    # [60, 70, 80, 90]
    print(f"values from 5 to 8 = {numbers[5:9]}")

    print()

    # [10, 20, 30, 40, 50]
    print(f"values from 0 to 4 = {numbers[0:5]}")

    # by default the slicing starts at 0th position
    print(f"values from 0 to 4 = {numbers[:5]}")

    print()

    # [60, 70, 80, 90, 100]
    print(f"values from 5 to 9 = {numbers[5:10]}")

    # by default the slicing can go to the last position
    print(f"values from 5 to 9 = {numbers[5:]}")

    print()

    # [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
    print(f"values from 0 to 9 = {numbers[0:10]}")
    print(f"values from 0 to 9 = {numbers[0:]}")
    print(f"values from 0 to 9 = {numbers[:10]}")
    print(f"values from 0 to 9 = {numbers[:]}")

# function2()
# values from 2 to 5th = [30, 40, 50, 60]
# values from 5 to 8 = [60, 70, 80, 90]

# values from 0 to 4 = [10, 20, 30, 40, 50]
# values from 0 to 4 = [10, 20, 30, 40, 50]

# values from 5 to 9 = [60, 70, 80, 90, 100]
# values from 5 to 9 = [60, 70, 80, 90, 100]

# values from 0 to 9 = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
# values from 0 to 9 = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
# values from 0 to 9 = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
# values from 0 to 9 = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]

def func3():
    numbers = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]

    # store values at even positions 
    values_at_even_pos = []
    for i in range(0,len(numbers),2):
        values_at_even_pos.append(numbers[i])
    print(values_at_even_pos)

    print()

    # store values at odd positions
    values_at_odd_pos = []
    for i in range(1,len(numbers), 2):
        values_at_odd_pos.append(numbers[i])
    print(values_at_odd_pos)

# func3()
# [10, 30, 50, 70, 90]

# [20, 40, 60, 80, 100]

def function4():
    numbers = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]

    # collect values at even position
    print(f"values at even positions = {numbers[0::2]}")
    print(f"values at even positions = {numbers[:10:2]}")
    print(f"values at even positions = {numbers[::2]}")

    # collect values at odd position
    print(f"values at even positions = {numbers[1:10:2]}")
    print(f"values at even positions = {numbers[1::2]}")


# function4()
# values at even positions = [10, 30, 50, 70, 90]
# values at even positions = [10, 30, 50, 70, 90]
# values at even positions = [10, 30, 50, 70, 90]
# values at even positions = [20, 40, 60, 80, 100]
# values at even positions = [20, 40, 60, 80, 100]

