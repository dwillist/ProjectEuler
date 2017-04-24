#!usr/bin/python2.7

import math
#the below finds the largest prime factor of a number
def is_prime(integer):
    for val in range(2, int(math.sqrt(float(integer)) + 1)):
        if(integer % val == 0):
            return False
    return True

def main(user_int):
    current_prime = 0
    for val in range(int(math.sqrt(float(user_int)) + 1),1,-1):
        if user_int % val == 0:
            d1 = val
            d2 = user_int / val
            if d2 > current_prime and is_prime(d2):
                current_prime = d2
            if d1 > current_prime and is_prime(d1):
                current_prime = d1

    return current_prime

user_input = int(raw_input("Enter an integer to find the greates prime factor of it: "))
print main(user_input)
