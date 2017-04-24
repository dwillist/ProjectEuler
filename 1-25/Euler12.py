#!/usr/bin/python2.7

import math

def divisor_count(integer):
    div_count = 0
    for i in range(1,int(math.sqrt(float(integer)))):
        if integer % i == 0 and i != math.sqrt(float(integer)):
            div_count += 2
        elif i == math.sqrt(float(integer)) and integer % i == 0:
            div_count += 1
    return div_count

def t_num(i):
    return (i * (i+1))/2

def main(value):
    i = 1
    while(divisor_count(t_num(i)) < value):
        i+=1
    return t_num(i)


user_input = int(raw_input("Enter the min number of divisiors"))
print main(user_input)
