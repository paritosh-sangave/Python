# explicit type conversion
# int() => used to convert anything to int
# str() => used to convert anything to string
# float() => used to convert anything to float
# bool() => used to convert anything to bool

num = 100
salary = 15.50
can_vote = True
str_value = '10.50'

print(f"num = {num}")
print(f"salary = {salary}")
print(f"can_vote = {can_vote}")
print(f"str_value = {str_value}")

# int to a string
str_num = str(num)
print(f"str_num = {str_num}, type = {type(str_num)}")

# float to string
str_salary = str(salary)
print(f"str_salary = {str_salary}, type = {type(str_salary)}")

# bool to string
str_can_vote = str(can_vote)
print(f"str_can_vote = {str_can_vote}, type = {type(str_can_vote)}")

# str_num = 100, type = <class 'str'>
# str_salary = 15.5, type = <class 'str'>
# str_can_vote = True, type = <class 'str'>

# string to int
value = '10'
int_value = int(value)
print(f"int_value = {int_value}, type = {type(int_value)}")
# int_value = 10, type = <class 'int'>
