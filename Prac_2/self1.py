def func1(name=None, address=None):
    """
    Dummy Function with no purpose than to print a string
    """
    print("Inside func1")

# func1()
# Inside func1


# print(func1.__doc__)
#    Dummy Function with no purpose than to print its call


# print(print.__doc__)
# print(value, ..., sep=' ', end='\n', file=sys.stdout, flush=False)

# Prints the values to a stream, or to sys.stdout by default.
# Optional keyword arguments:
# file:  a file-like object (stream); defaults to the current sys.stdout.
# sep:   string inserted between values, default a space.
# end:   string appended after the last value, default a newline.
# flush: whether to forcibly flush the stream.

# def inner_function():
#     print("this is a global inner function")


# inner_function()
# this is a global inner function


# global function
# - a function written outside of any other function

# rules of inner function
# - outer function can call inner function
# - inner function can call any global function
# - inner function can access all the members of outer function
# - but outer function CAN NOT access any of the member declared within nested function

# Global func
def my_global_func():
    print("Inside my_func")

def outer_func():
    print("Inside outer_func")

    # local scope
    num = 100
    print(f"num = {num}")

    # nested / local / inner func
    def inner_func():
        print("Inside inner_func")

        # accessing outer func's members
        print(f"num = {num}")

        # Calling global func inside nested func
        my_global_func()

        inner_var = 500
        print(f"Inner_var = {inner_var}")

    # since it is a local func,
    # it can be called only within this func

    inner_func()

    return num

outer_func()
# Inside inner_func
# num = 100
# Inside my_func
# Inner_var = 500


# can not access this as its a local variable of outer_function
# print(num)

# since the inner_function is having a local scope of outer_function
# it can not be called outside of outer function
# inner_function()