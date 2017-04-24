# so first lets try to make a function that can approximate
import math

def isPrime(x):
    for i in range(2,int(math.sqrt(x))+1):
        if x % i ==0:
            return False
    return True

def genPrimeSet(k):
    toReturn = []
    for i in range(2,k+1):
        if isPrime(i):
            toReturn.append(i)
    return toReturn

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


def factorize(integer,pSet):
    workingValue = integer
    workingFactorization = []
    while workingValue not in pSet:
        for prime in pSet:
            if workingValue % prime == 0:
                workingFactorization.append(prime)
                workingValue /= prime
                break
    return workingFactorization

def myOpp(maxIndex,lis,function = lambda x,y : x + y,startVal = 0):
    value = startVal
    for i in range(0,min(maxIndex,len(lis))):
        summation = function(summation,lis[i])
    return

def integerPartitonApprox(n):
    return 1/(math.sqrt(3) * 4*n) * math.e**(math.pi * (math.sqrt(2*n/3)))


main()
