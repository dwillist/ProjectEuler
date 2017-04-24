#!/usr/bin/python3

# this problem is pretty easily brute forceable
from itertools import permutations
import GeneralProcs

def solve():
    perms = permutations('1234567',7)
    lastVal = 0
    for perm in perms:
        value = int(''.join(perm))
        if GeneralProcs.isPrime(value):
            print(value)
            lastVal = value
    return lastVal

solve()
