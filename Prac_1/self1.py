# All data types in python are inferred


num = 100.01
num_int: int = 100
num_float: float = 100.101

print(f"value of num = {num}")
print(f"data type of num = {type(num)}")

print(f"value of num = {num_int}")
print(f"data type of num = {type(num_int)}")

print(f"value of num = {num_float}")
print(f"data type of num = {type(num_float)}")

# value of num = 100.01
# data type of num = <class 'float'>
# value of num = 100
# data type of num = <class 'int'>
# value of num = 100.101
# data type of num = <class 'float'>
print('\n\n')

# float
salary = 13000.50
print(f"Salary = {salary} type = {type(salary)}")

# bool
pass_status = True
print(f"Salary = {pass_status} type = {type(pass_status)}")

# str
first_name = "steve"
print(f"value of first_name = {first_name}, type = {type(first_name)}")

# multiline string
bhai_string = """Tension nahi leneka bhaii..!!
Yeh toh shuru hotee hi khatam hoo gaya...
deewar todd ke side ka kamra under kar lenge"""
print(bhai_string)
print(type(bhai_string))

# Salary = 13000.5 type = <class 'float'>
# Salary = True type = <class 'bool'>
# value of first_name = steve, type = <class 'str'>
# Tension nahi leneka bhaii..!!
# Yeh toh shuru hotee hi khatam hoo gaya...
# deewar todd ke side ka kamra under kar lenge
# <class 'str'>

print('\n\n')

dialog1 = 'arnold once said, "trust me!! I will back."'
print(dialog1)

dialog2 = "arnold once said, \"trust me!! I will back.\""
print(dialog2)

dialog3 = "arnold once said, 'trust me!! I will back.'"
print(dialog3)

dialog4 = 'arnold once said, \'trust me!! I will back.\''
print(dialog4)

# arnold once said, "trust me!! I will back."
# arnold once said, "trust me!! I will back."
# arnold once said, 'trust me!! I will back.'



num2 = 10
print(f"value of num2 = {num2}", end="---")
print(f"type of num2 = {type(num2)}")

num2 += 1
print(f"value of num2 = {num2}")

# type hinting
# this variable may contain int value
num3: int = 500
print(f"num3 = {num3}, type = {type(num3)}")
num += 1

num = "test"
print(f"num = {num}, type = {type(num)}")

# value of num2 = 10---type of num2 = <class 'int'>
# value of num2 = 11
# num3 = 500, type = <class 'int'>
# num = test, type = <class 'str'>