# tuple

def function1():
    # tuple packing
    # - adding all the values into a tuple collection
    t1 = 10, 20, 30, 40, 50

    t2 = 10, 20
    print(f"value at 0th position = {t2[0]}")
    print(f"value at 1st position = {t2[1]}")

    p1 = t2[0]
    p2 = t2[1]
    result = p1 + p2

    # tuple unpacking
    n1, n2, n3 = 10, 20, 30
    print(f"n1 = {n1}, n2 = {n2}, n3 = {n3}")

    # p3 = 30
    # p4 = 40
    # p5 = 50
    # p6 = 60
    p3, p4, p5, p6 = 30, 40, 50, 60


# function1()
# value at 0th position = 10
# value at 1st position = 20
# n1 = 10, n2 = 20, n3 = 30



def function2():
    n1, n2 = 10, 20
    print(f"n1 = {n1}, n2 = {n2}")

    # temp = n1
    # n1 = n2
    # n2 = temp
    # print(f"n1 = {n1}, n2 = {n2}")

    # swapping two variables
    n1, n2 = n2, n1
    print(f"n1 = {n1}, n2 = {n2}")


# function2()
# n1 = 10, n2 = 20
# n1 = 20, n2 = 10
