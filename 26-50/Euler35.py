#usr/bin/python3

#Circular Primes

import math

def cycleList(integer):
    string = str(integer)
    stringList = [string]
    for i in range(len(string)-1):
        stringList.append(stringList[-1][-1] + stringList[-1][:-1])
    return list(map(int,stringList))

def isPrime(integer):
    for i in range(2,int(math.sqrt(integer)+1)):
        if integer % i == 0:
            return False
    return True

def update(primesDict,lis):
    if lis[0] in primesDict:
        return 0
    else:
        for element in lis:
            if element in primesDict and not primesDict[element]:
                return 0
            elif not isPrime(element):
                for el in lis:
                    primesDict[el] = False
                    return 0
            else:
                primesDict[element] = True
        print(lis)
        return len(list(set(lis)))

def solve():
    count = 0
    primesDict = {}
    for i in range(2,1000001):
        lis = sorted(cycleList(i))
        count += update(primesDict,lis)
    print(count)
    #print(primesDict)

solve()
