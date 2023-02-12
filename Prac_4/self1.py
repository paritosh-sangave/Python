# tuple repeatition

def function1():
    t1 = (10, 20)

    # repeat the values of t1 4 times
    # and create a new tuple
    t2 = t1 * 4
    print(t1)
    print(t2)

# function1()
# (10, 20)
# (10, 20, 10, 20, 10, 20, 10, 20)


def function2():
    t1 = (10, 20, 30, 40)
    t2 = (50, 60, 70, 80)

    t3 = t1 + t2
    print(t1)
    print(t2)
    print(t3)

# function2()
# (10, 20, 30, 40)
# (50, 60, 70, 80)
# (10, 20, 30, 40, 50, 60, 70, 80)


def function3():
    t1 = 20, 40, 60, 80

    # tuple unpacking
    # n1, n2, n3, n4 = 20, 40, 60, 80
    n1, n2, n3, n4 = t1

    print(t1)
    print(f"n1: {n1}, n2: {n2}")

# function3()
# (20, 40, 60, 80)
# n1: 20, n2: 40
