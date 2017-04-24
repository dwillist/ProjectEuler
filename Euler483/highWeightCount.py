#!/usr/bin/python3

import math

def isPrime(n):
    for div in range(2,int(math.sqrt(n)+1)):
        if n % div == 0:
            return False
    return True

def main():
    primes = [i for i in range(2,351) if isPrime(i)]
    summation = 0
    product = 1
    count = 0
    index = 0
    primesInProd = []
    while summation + primes[index] <= 350:
        summation += primes[index]
        product *= primes[index]
        count += 1
        primesInProd.append(primes[index])
        index +=1
    print(summation)
    print(product)
    print(count)
    print(index)
    print(math.factorial(350) // sum(map( lambda x : math.factorial(x),primesInProd)))

main()
