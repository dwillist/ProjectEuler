#!/usr/bin/python3

import math

def isPrime(integer):
    for div in range(2,int(math.sqrt(integer)+1)):
        if integer % div == 0:
            return False
    return True

def makeSieve(maxInt):
    compositeSet = set()
    primeSet = set()
    for integer in range(2,maxInt):
        if integer in compositeSet:
            pass
        else:
            primeSet.add(integer)
            for composite in range(integer*2,maxInt,integer):
                compositeSet.add(composite)
    return compositeSet,primeSet


def pentagonal(n):
    # we can guarentee this will always be an integer
    return (n*(3*n -1)) // 2

def pentagonalTest(integer):
    return isSquare(1 + 24*integer) and (1 + math.sqrt(1 + 24*integer)) % 6 == 0

def triangular(n):
    return n*(n+1)//2

def triangularTest(integer):
    return isSquare(1 + 4*2*integer)

def quadraticFormula(A,B,C):
    try:
        base = -B/(2*A)
        switch = math.sqrt(B**2 - 4*A*C)/2*A
        return base+switch,base-switch
    except ValueError:
        return [0,0]

def toBase2(integer):
    base2string = ''
    while integer > 0:
        base2string = str(integer % 2) + base2string
        integer = int(integer/2)
    return base2string

def isSquare(integer):
    return int(math.sqrt(integer))**2 == integer

def factorize(n):
    if n > 1:
        for i in range(2,int(math.sqrt(n)) + 1):
            div,mod = divmod(n,i)
            if mod == 0:
                return [i] + factorize(div)
        return [n]
    else:
        return []


def gcd(a,b):
    while b>0:
        temp = a % b
        a = b
        b = temp
    return a
