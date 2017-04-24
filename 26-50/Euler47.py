#!/usr/bin/python3

from GeneralProcs import factorize

def f(lis):
    prod = 1
    for i in lis:
        prod *= i
    return prod

def solve():
    currentFactors = []
    i = 600
    while len(currentFactors) < 4:
        f = factorize(i)
        if len(set(f)) == 4:
            currentFactors.append(f)
        else:
            currentFactors = []
        i+=1

    return currentFactors

sol = solve()
print(sol)
print(list(map(f,sol)))
