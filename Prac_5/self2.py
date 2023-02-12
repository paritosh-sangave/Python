# loops
# - for
#   - is used only when you know when to stop
#   - can be written as traditional and foreach loop
#   - can also declare else block which gets called only when the for
#     loop does not break in between
# - while
#   - is used only when you do not know the terminating condition

# write a menu driven program for
# - checking if a number is prime
# - checking if a number is even
# - checking if a number is odd

# welcome to the program
# 1. check if the number is prime
# 2. check if the number is even
# 3. check if the number is odd
# 4. exit
# enter your choice:

# pass: no operation (noop)

def check_prime(num):
    is_prime = True
    for i in range(2,num//2+1):
        if num%i==0:
            print(f"{num} is divisible by {i}")
            is_prime=False
            break
    if is_prime:
        print("{num} is a prime number")
    else:
        print("{num} is a composite number")

def check_even(num):
    if num%2==0:
        print(f"{num} is even")
    else:
        print(f"{num} is not even")

def check_odd(num):
    if num%2==1:
        print(f"{num} is odd")
    else:
        print(f"{num} is not odd")


## One time run program
def check_program_menu(num):
    intro_string = f'''welcome to the program
number = {num}
1. check if the number is prime
2. check if the number is even
3. check if the number is odd
4. exit
'''
    print(intro_string)
    choice = int(input("enter your choice:"))

    if choice==1:
        check_prime(num)
    elif choice==2:
        check_even(num)
    elif choice==3:
        check_odd(num)
    elif choice==4:
        print("Exiting the menu driven program, Have a nice day")
    else:
        print("Invalid choice...exiting the program")

# check_program_menu(37)
# welcome to the program
# number = 37
# 1. check if the number is prime
# 2. check if the number is even
# 3. check if the number is odd
# 4. exit

# enter your choice:1
# {num} is a prime number


## using While loop 
def check_program_menu():
    intro_string = '''welcome to the program
1. check if the number is prime
2. check if the number is even
3. check if the number is odd
4. exit
'''

    while True:
        print(intro_string)
        num = int(input("Select a number : "))
        choice = int(input("enter your choice :"))

        if choice==1:
            check_prime(num)
        elif choice==2:
            check_even(num)
        elif choice==3:
            check_odd(num)
        elif choice==4:
            print("Exiting the menu driven program, Have a nice day")
            break
        else:
            print("Invalid choice...exiting the program")
            break
        print()

check_program_menu()
