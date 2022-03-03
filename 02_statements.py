# statement: Instruction that interpreter can execute

# multi-line statement: use '\'

a = 2+3+4+\
    5+4+\
    7+3-4

print(a)

# o/p: 24

b = (5+
     3+2
     +2-2)

print(b)

# o/p: 10

colours = {'red',
           'yellow',
           'blue'}

# multiple statements in one line: use ';'

a = 2 ; b = 3 ; c = 5

# Indentation: Like C, C++, Java use braces {} to define block, python uses indentation
# 4 whitespace indentation usually preferred 

for i in range(1,18):
    print(i)
    if i == 3:
        break

# o/p: 1 
#      2 
#      3

if True:
    print('Hello')
    c = 9

##

if True: print('Hello'); c = 9     

# both above statements are equivalent
# Incorrect indentation will result in 'IndentationError'

# Comments: 
# Single line comment: use '#'
# multi-line comment example below
'''This can be regarded
as multi-line comments
we are using three single inverted commas
you may also use (""" """)   '''

# Docstrings: (Documentation string)
# String literals that appear right after function definition

def plus10(num):
    """Number plus ten"""
    return num+10

# to print docstring in console you can use following command
print(plus10.__doc__)

# o/p: Number plus ten