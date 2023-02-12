# Write a program to identify if number is prime or not
import math as mt

def primeCheck(num1):
    if type(num1) == int:
        is_prime = True
        for i in range(2, int(mt.sqrt(num1)+1)+1):
            if num1 % i == 0:
                print(f"Number {num1} completely divisible by {i}")
                is_prime = False
                break
        if is_prime:
            print(f"{num1} is a Prime")
        else:
            print(f"{num1} is composite")        
    else:
        print("Number entered is not an integer")

# primeCheck(37)
# 37 is a Prime


def function3():
    def is_prime(number):
        for temp_number in range(2, number):
            if number % temp_number == 0:
                return False

        return True

    # generate a list of prime numbers from 3 to user input
    upper_bound = int(input("enter number till which you want to generate prime numbers: "))

    prime_numbers = []
    for value in range(3, upper_bound + 1):
        if is_prime(value):
            prime_numbers.append(value)

    print(prime_numbers)

# function3()
# enter number till which you want to generate prime numbers: 40
# [3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37]


def func4():
    number = 31

    for temp_number in range(2, number):
        if number % temp_number == 0:
            print(f"{number} is NOT prime")
            break
    else:
        # this block gets called only when the input is not divisible by
        # any of the numbers between 2 to the number
        print(f"{number} is prime")


func4()


def func5():
    for number in range(10):
        print(f"number = {number}")
        if number > 15:
            break
    else:
        # this block gets called only if the for loop completes from
        # the first till the last value of range

        # this block will never get called if the for loop
        # breaks in between
        print("this is else block of for loop")


# func5()