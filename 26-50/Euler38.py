#!/usr/bin/python3

def solve():
    rng = range(1000,10000)
    for i in rng:
        lis = list(map(int,list(str(i*1) + str(i*2))))
        if len(list(set(lis))) == 9 and 0 not in lis:
            print(i)


solve()
