# Datatypes: Everything is an object in python, datatypes are classes and variables are instance(object) of these classes.

# Python Numbers:
# 1) int
# 2) float
# 3) complex

# type(): to know class of a variable
# isinstance(,): to check if object belongs to a particular class

a = 2
print(a,"is of type",type(a))

a = 3.9
print(a,"is of type",type(a))

a = 3 + 4j
print("is",a,"an integer? ==>",isinstance(a,int))

# o/p
# 2 is of type <class 'int'>
# 3.9 is of type <class 'float'>
# is (3+4j) an integer? ==> False

# Integer length only limited by available memory
# Float is rounded off if decimal place exceedes 15 places

#-----------------------------------
# List: Ordered sequence of entities (enclosed in closed/square brackets)

a = [6, 2.3, 3+4j, 'C', "Hello"]

# a[0]=6, a[1]=2.3, a[2]=3+4j, a[3]=C, a[4]="Hello"

print(a)

# o/p:
# [6, 2.3, (3+4j), 'C', 'Hello']

print(a[3]) # C
print(a[4]) # Hello

# Lists are mutable, values of elements can be altered
# ---------------------------------------------

# Tuples: Ordered sequences of elements (enclosed in open/round brackets)
# tuples are immutable, values of elements cannot be altered

primes = (2,3,5,7,11)
primes[2]=0
# o/p
# Traceback (most recent call last):
#   File "c:\Programiz\Python\04_Datatypes.py", line 50, in <module>
#     primes[2]=0
# TypeError: 'tuple' object does not support item assignment

# -------------------------

# Python Strings:
