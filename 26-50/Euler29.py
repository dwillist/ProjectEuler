#!/usr/bin/python2

def solve(n,m):
    hashing = {}
    for a in xrange(2,n+1):
        for b in xrange(2,m+1):
            hashing[a**b] = 1
    return len(hashing)

def main():
    print solve(100,100)

main()
