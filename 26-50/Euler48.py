#!/usr/bin/python3



def solve():
    summation = 0
    for i in range(1,1001):
        summation += i**i % 10**10
    str(summation)
    return int(str(summation)[-10:])

print(solve())
