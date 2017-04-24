#!/usr/bin/python2.7


def main(user_integer):
    temp = 0
    fib1 = 0
    fib2 = 1
    summation = 0
    while(fib2 < user_integer):
        temp = fib1
        fib1 = fib2
        fib2 = fib2 + temp
        if(fib2 % 2 == 0):
            summation += fib2
    return summation


user_int = int(raw_input("Enter an Integer: "))
print main(user_int)
