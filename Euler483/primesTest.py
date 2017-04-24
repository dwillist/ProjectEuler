#!/usr/bin/python3

import math

#here we try to get some sense of the scope of using GCD as the backbone of our indexing
def gcd(a,b):
    if(a < b):
        return gcd(b,a)
    else: # b > a
        while( a > 0):
            temp = a
            a = b % a
            b = temp
        return b

def lcm(a,b):
    if (min(a,b) == 0):
        return max(a,b)
    return (a * b) / gcd(a,b)

def isPrime(k):
    for i in range(2,int(math.sqrt(k)) + 1):
        if k % i == 0:
            return False
    return True


def workHorse(n,primePos,solutionDict,primeList):
    if n < 0:
        return 0

    elif n == 0:
        return 1
    else:
        if n in solutionDict:
            if primePos in solutionDict[n]:
                return solutionDict[n][primePos]
            else:
                summation = 0 # for all 1-cycles
                for i in range(primePos,-1,-1):
                    summation += workHorse(n - primeList[i],i,solutionDict,primeList)
                solutionDict[n][primePos] = summation
                return solutionDict[n][primePos]
        else:
            solutionDict[n] = {}
            return workHorse(n,primePos,solutionDict,primeList)


def countUniqueLengths(n):
    pList = [i for i in range(1,n+1) if isPrime(i)]
    #print(pList)
    solutionDict = {}
    toReturn = workHorse(n,len(pList)-1,solutionDict,pList)
    #print(solutionDict)
    return toReturn

#for i in range(3,100):
#    print(str(i) + " : " + str(countUniqueLengths(i)))

#def estimation(n):
#    return math.e ** (2*math.pi* (1/math.sqrt(6)) * (n/math.sqrt(math.log(n))))

for i in range(3,351):
    print("{} : {} ".format(i,countUniqueLengths(i)))
