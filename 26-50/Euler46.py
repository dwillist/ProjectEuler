#!/usr/bin/python3

import GeneralProcs

def updatePrimes(p,primeSet,compositeSet):
    if p in primeSet:
        return True
    elif p in compositeSet:
        return False
    elif GeneralProcs.isPrime(p):
        primeSet.add(p)
        return True
    else:
        compositeSet.add(p)
        return False


def goldbach(i,primeSet,compositeSet):
    odd = 2*i+1
    if updatePrimes(odd,primeSet,compositeSet):
        return True
    j = 1
    while 2*j**2 < odd:
        diff = odd - 2*j**2
        if updatePrimes(diff,primeSet,compositeSet):
            return True
        j += 1
    return False


def solve():
    i = 1
    primeSet = {2,3}
    compositeSet = {4}
    while goldbach(i,primeSet,compositeSet):
        i+=1
    return 2*i+1

print(solve())
print(GeneralProcs.isPrime(5777))
