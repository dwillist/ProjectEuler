#!/usr/bin/python2.7

import math

def is_prime(integer):
    for val in range(2,int(math.sqrt(float(integer)))):
        if(integer % val == 0):
            return False
    return True


def factorize(integer,current = 2):
    lis = []
    for val in range(current,integer+1):
        if( integer % val == 0 and is_prime(val)):
            lis.append(val)
            lis.extend(factorize(integer/val,current))
            return lis
    return []

def myextend(lis1,lis2):
    for elem in lis2:
        if lis2.count(elem) > lis1.count(elem):
            for i in range(lis2.count(elem) - lis1.count(elem)):
                lis1.append(elem)


def main(integer):
    lis = []
    temp = []
    for val in range(2,integer+1):
        temp = factorize(val)
        myextend(lis,temp)
        temp = []

    prod = 1
    for elem in lis:
        prod = prod * elem

    return prod

user_input = int(raw_input("Enter the limiting value "))
print main(user_input)
