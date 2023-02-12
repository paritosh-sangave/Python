# set vs frozen set
# set: mutable, frozen set: immutable

def func1():
    s1 = {10, 20, 30, 40, 50}
    print(s1)

    s1.pop()
    print(s1)

    s1.pop()
    print(s1)

    s1.add(90)
    print(s1)

# func1()
# {50, 20, 40, 10, 30}
# {20, 40, 10, 30}
# {40, 10, 30}
# {90, 40, 10, 30}


def func2():
    # immutable set
    s1 = frozenset([10, 20, 30, 40, 50])
    print(s1)

    # can not perform pop()
    # s1.pop()

    # can not perform add()
    # s1.add(60)


# func2()
