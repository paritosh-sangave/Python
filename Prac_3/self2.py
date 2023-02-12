# indexing
# indexing always starts with 0, accessing list elemnets using index

def function1():
    num_list = [10, 20, 30, 40, 50, 60]
    #            0   1   2   3   4   5 
    print(f"value at 0th position = {num_list[0]}")
    print(f"value at 1st position = {num_list[1]}")
    print(f"value at 2nd position = {num_list[2]}")
    print(f"value at 3rd position = {num_list[3]}")
    print(f"value at 4th position = {num_list[4]}")
    print(f"value at 5th position = {num_list[5]}")

# function1()

def function2():
    numbers = [10, 20, 30, 40, 50]
    #          -5  -4  -3  -2  -1
    print(f"value stored at -1 index: {numbers[-1]}")
    print(f"value stored at -2 index: {numbers[-2]}")
    print(f"value stored at -3 index: {numbers[-3]}")
    print(f"value stored at -4 index: {numbers[-4]}")
    print(f"value stored at -5 index: {numbers[-5]}")


def function3():
    numbers = [10, 20, 30, 40, 50]
    print(f"first value : {numbers[0]}")
    print(f"first value : {numbers[-len(numbers)]}")
    print(f"last value: {numbers[len(numbers) - 1]}")
    print(f"last value: {numbers[-1]}")


# function3()
# first value : 10
# first value : 10
# last value: 50
# last value: 50