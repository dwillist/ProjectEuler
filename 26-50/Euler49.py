#!/usr/bin/python

import itertools,GeneralProcs

def prop(threeSet):
    threeSet = [int(''.join(i)) for i in threeSet]
    diffList = [threeSet[i] - threeSet[i-1] for i in range(1,len(threeSet))]
    if len(set(diffList)) == 1 and len(set(threeSet)) == 3:
        for i in threeSet:
            if not GeneralProcs.isPrime(i):
                return False
        return True
    return False

def solve():
    myset = map(''.join,itertools.combinations_with_replacement('123456789',4))
    for aset in myset:
        for threeSet in itertools.combinations(sorted(itertools.permutations(aset)),3):
            if prop(threeSet):
                print(threeSet)


solve()
print("post Solve")
