#!/usr/bin/python2.7

def square_diff(integer):
    sum1 = 0
    sum2 = 0
    for val in range(integer+1):
        sum1 += val
        sum2 += val**2
    return sum1**2 - sum2


user_input = int(raw_input("Enter the max value: "))
print square_diff(user_input)
