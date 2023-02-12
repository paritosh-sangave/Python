# calling convention
# - the way to decide the parameter's sequence
# - left to right similar to C
# - c calling convention

# all the parameters are required
def function1(name, address, phone):
    print("inside function1")
    print(f"name: {name}, address: {address}, phone: {phone}")


# positional parameters
# - parameters will be passed from left to right in a required sequence

function1("person1", "+91234234", "address1")
# inside function1
# name: person1, address: +91234234, phone: address1

# named parameters

# function1(name="person1", address="address1", phone="+91234324")
function1(address="address2", phone="+91234334", name="person2")
# inside function1
# name: person2, address: address2, phone: +91234334


# mix
function1(None, phone=91234234, address="address3")
# inside function1
# name: None, address: address3, phone: 91234234


# parameter with default value
# - if the parameter does not get any value at the time of function call,
#   the parameter will use the default value
# - this makes the parameter optional
# - the default value(s) must be given from right to left
def function2(p1, p2=0):
    print("inside function2")
    print(f"p1 = {p1}, p2 = {p2}")


# function2(10, 20)
# function2(p1=10, p2=20)
function2(p2=20, p1=10)
# inside function2
# p1 = 10, p2 = 20

# p1: 10, p2: 20
# function2(10, 20)

# p1: 10, p2: 0
function2(10)
# inside function2
# p1 = 10, p2 = 0


# default country = "india"
def print_details(name, address, city="pune", state="mh", phone=0, country="india"):
    print(f"name: {name}")
    print(f"address: {address}")
    print(f"city: {city}")
    print(f"state: {state}")
    print(f"phone: {phone}")
    print(f"country: {country}")


# try calling function with positional parameters
# print_details("p1", "pune", "pune", "mh", "+9132434", "india")

# try calling function with named parameters
# print_details("p1", "pune", "pune", "mh", country="usa")
# name: p1
# address: pune
# city: pune
# state: mh
# phone: 0
# country: usa

print_details("person2", "h-105", phone="+91342243")
# name: person2
# address: h-105
# city: pune
# state: mh
# phone: +91342243
# country: india


