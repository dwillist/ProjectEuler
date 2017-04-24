
from itertools import product

def to_int(string):
    summation = 0
    string = string.lstrip('0')
    power = 1
    for val in string:
        summation += int(val) * (10 ** (len(string) - power))
        power += 1
    return summation

def apply_power(string,power):
    summation = 0
    for val in string:
        summation += int(val) ** power
    return summation


def solve():
    list_of_vals = range(2,1 + 5*(9**5))
    equal_list = []
    for integer in list_of_vals:
        string = str(integer)
        if integer == apply_power(string,5):
            print "integer value: " + str(integer)
            print "power value: " + str(apply_power(string,5))
            equal_list.append(integer)
    return equal_list

def main():
    a =  solve()
    print a
    print sum(a)
main()
