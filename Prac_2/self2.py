# Lambda Function

# named func: has only one statement in body which is return statement
def num_squared(num):
    return num**2

# lambda :
# parameter: number
# return: calculation

# get_square = lambda num: num**2
# print(f"get_square(5) = {get_square(5)}")
# # get_square(5) = 25

# increment
incr_num = lambda num: num+1
print(f"incr_num(23) = {incr_num(23)}, type(incr_num) = {type(incr_num)}")
# incr_num(23) = 24, type(incr_num) = <class 'function'>

# Celcius to Farenheit
# celcius_to_farenheit = lambda c: (c * (9/5)) + 32
# print(f"37 degree celsius in farenheit is {celcius_to_farenheit(37):.2f}")
# # 37 degree celsius in farenheit is 98.60

# Add two numbers
# add = lambda a, b: a+b
# print(f"addition of 35 and 76 is {add(35,76)}")
# # addition of 35 and 76 is 111

