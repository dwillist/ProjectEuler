#!/usr/bin/python3

import GeneralProcs

def isPrimeLookup(integer,primeDict):
    if integer in primeDict:
        return primeDict[integer]
    else:
        primeDict[integer] = GeneralProcs.isPrime(integer)
    return primeDict[integer]

def trunkLeft(integer):
    trunkArray = []
    string = str(integer)
    for i in range(1,len(string)+1):
        trunkArray.append(int(string[:i]))
    return trunkArray

def trunkRight(integer):
    trunkArray = []
    string = str(integer)
    for i in range(len(string)-1,-1,-1):
        trunkArray.append(int(string[i:]))
    return trunkArray

def solve():
    primeDict = {1:False}
    trunPrimes = []
    i = 10
    while len(trunPrimes) < 11:
        toAppend = True
        left = trunkLeft(i)
        right = trunkRight(i)
        for k in range(len(left)):
            if not (isPrimeLookup(left[k],primeDict) and isPrimeLookup(right[k],primeDict)):
                toAppend = False
                break
        if toAppend:
            trunPrimes.append(i)
            print(trunPrimes)
        i+=1
    return trunPrimes

print(sum(solve()))
