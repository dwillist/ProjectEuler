#!usr/bin/python2.7


def sum(integer):
    string = str(integer)
    summation = 0
    for element in string:
        summation += int(element)
    return summation

print sum(2**1000)
