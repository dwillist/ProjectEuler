#!/usr/bin/python2.7
import math

def is_prime(num,p_list):
    for element in p_list:
        if num % element == 0:
            return False
        elif element >= math.sqrt(num):
            return True


def gen_primes(limit):
    p_list = [2]
    for val in range(3,limit):
        if is_prime(val,p_list):
            p_list.append(val)
    return sum(p_list)

user_value = int(raw_input("Enter a value: "))
print gen_primes(user_value)
