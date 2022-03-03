# Variable: A named entity which is used to store data in memory.

num = 10

# Variables can be reassigned values at any point inside program.

num = 2.7182

# Note: In Python, values are not assigned to the variables. 
# Python gives the reference of the object(value) to the variable.

# Declaring and assigning values to variable:

knight = '3 points'
print(knight) # o/p: 3 points

# Note: Python is a type-inferred language, defining variable type not needed.

knight = '4 points'
print(knight) # o/p: 4 points

# Assigning multiple values to multiple variables

a,b,c = 3.1415, 2.7182, 'Trancendentals'

print(a,b,c) # o/p: 3.1415 2.7182 Trancendentals

l = m = n = 2
print(l)
print(m)
print(n)

# o/p: 
# 2
# 2
# 2

import Mconst as ct

print('e =',ct.e)
print('pi =',ct.pi)
print('ln(2) =',ct.ln2)

# o/p:
# e = 2.7382
# pi = 3.1415
# ln(2) = 0.69

# Numeric literals: (Immutable)

a = 0b1010 #Binary Literals
b = 100 #Decimal literals
c = 0o310 #Octal Literal
d = 0x12c #Hexadecimal Literal

#Float Literal
fnum1 = 10.5
fnum2 = 2.1e2

#Complex Literal
z = 2 + 3j

print(a,b,c,d)
print(fnum1, fnum2)
print(z,z.real,z.imag)

# o/p:
# 10 100 200 300
# 10.5 210.0
# (2+3j) 2.0 3.0

# String literals: Sequence of characters enclosed inside quotes.
# Allowed quotes - (" ") (' ') (''' ''') (""" """)

string1 = "Python in VS code"
char = 'C'
multiline_str = """Multiline string with more than one line code."""
unicode = u"\u00dcnic\u00f6de"
raw_str = r"raw \n string"

print(string1)
print(char)
print(multiline_str)
print(unicode)
print(raw_str)

# o/p:
# Python in VS code
# C
# Multiline string with more than one line code.
# Ünicöde
# raw \n string

# Boolean Literals: True, False

x = (1 == True)
y = (1 == False)
a = True + 2
b = False + 2

print("x = ",x)
print("y = ",y)
print("a:",a)
print("b:",b)

# o/p
# x =  True
# y =  False
# a: 3
# b: 2

# Special literal (None): To specify that field has not been created

food = "Paratha, Sabji, Biryani"
drinks = None

def menu(x):
    if x == drinks:
        print(drinks)
    else:
        print(food)

menu(drinks)
menu(food)

# o/p
# None
# Paratha, Sabji, Biryani

# Literals Collection:

India = {"Vishwanathan Anand","Vidit Gujrathi","Adhiban"}
India_elo = {2751,2727,2648}
letters = {'A','B','C'}

print(India)
print(India_elo)
print(letters)

# o/p
# {'Vidit Gujrathi', 'Vishwanathan Anand', 'Adhiban'}
# {2648, 2751, 2727}
# {'A', 'B', 'C'}