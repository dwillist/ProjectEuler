#!/usr/bin/python2.7

import math

def sum_factors(n):
    fact_sum = -n
    for i in range(1,int(math.sqrt(float(n))) + 1):
        if n % i == 0:
            fact_sum += (i + n/i)
    return fact_sum


def main():
    summation = 0
    for val in range(2,10000):
            s1 = sum_factors(val)
            if(val == sum_factors(s1) and s1 != val):
                print val
                summation += val

    print summation

main()
#print sum_factors(284)
