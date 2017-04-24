#usr/bin/python3

import math

def toBase2(integer):
    base2string = ''
    while integer > 0:
        base2string = str(integer % 2) + base2string
        integer = int(integer/2)
    return base2string

def palindrom(string):
    return string == string[::-1]


def solve():
    summation = 0
    for i in range(1000001):
        if palindrom(str(i)) and palindrom(toBase2(i)):
            summation += i
    return summation


print(solve())
