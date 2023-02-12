# set

def func1():
    list1 = [10, 12, 14, 15]
    print(f"list1 = {list1}, type = {type(list1)}")

    t1 = (10, 12, 14, 15)
    print(f"t1 = {t1}, type = {type(t1)}")

    s1 = [10, 12, 14, 15]
    print(f"s1 = {s1}, type = {type(s1)}")

# func1()
# list1 = [10, 12, 14, 15], type = <class 'list'>
# t1 = (10, 12, 14, 15), type = <class 'tuple'>
# s1 = [10, 12, 14, 15], type = <class 'list'>

def func2():
    # empty list
    l1 = []
    print(f"l1 = {l1}, type = {type(l1)}")

    # empty tuple
    t1 = ()
    print(f"t1 = {t1}, type = {type(t1)}")

    # empty set
    s1 = set()
    print(f"s1 = {s1}, type = {type(s1)}")

    # empty dictionary
    d1 = {}
    print(f"d1 = {d1}, type = {type(d1)}")

# func2()
# l1 = [], type = <class 'list'>
# t1 = (), type = <class 'tuple'>
# s1 = set(), type = <class 'set'>
# d1 = {}, type = <class 'dict'>


def func3():
    s1 = {10, 20, 30, 40}
    s2 = {30, 40, 50, 60}

    print(f"intersection of s1 and s2 = {s1.intersection(s2)}")
    print(f"intersection of s2 and s1 = {s2.intersection(s1)}")
    print(f"union of s1 and s2 = {s1.union(s2)}")
    print(f"union of s2 and s1 = {s2.union(s1)}")
    print(f"s1 - s2 = {s1 - s2}")
    print(f"s2 - s1 = {s2 - s1}")

# func3()
# intersection of s1 and s2 = {40, 30}
# intersection of s2 and s1 = {40, 30}
# union of s1 and s2 = {40, 10, 50, 20, 60, 30}
# union of s2 and s1 = {40, 10, 50, 20, 60, 30}
# s1 - s2 = {10, 20}
# s2 - s1 = {50, 60}


def func4():
    # list
    numbers = [10, 20, 30, 40, 50, 10, 20, 30, 40, 50, 10, 20, 30, 40, 50]

    # tuple
    # numbers = (10, 20, 30, 40, 50, 10, 20, 30, 40, 50, 10, 20, 30, 40, 50)

    # find out the unique values from a collection
    unique_values = tuple(set(numbers))
    print(unique_values)


# func4()
# (40, 10, 50, 20, 30)