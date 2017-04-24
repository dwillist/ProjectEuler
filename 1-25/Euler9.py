#usr/bin/python2.7

import math

def find_triple(total):
    for val1 in range(1,total):
        for val2 in range(1,total):
            current = (1000 - val1) - val2
            if ( current > 0 ) and (current**2 == val1**2 + val2**2):
                return [val1,val2,current]


user_input = int(raw_input("Enter a value to find a Pathagorean triple for: "))
val = find_triple(user_input)
print val[0] * val[1] * val[2]
