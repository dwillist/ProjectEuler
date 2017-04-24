#!/usr/bin/python2.7

def pal(string):
    for i in range(len(string) / 2):
        if( not (string[i] == string[len(string)- 1 - i])):
            return False
    return True


def main(int1,int2):
    p = ""
    current_pal = 0
    for val1 in range (int1,int2):
        for val2 in range(int1,int2):
            p = str(val1 * val2)
            if int(p) > current_pal and pal(p):
                current_pal = int(p)
    return current_pal

input_int1 = int(raw_input("Enter the start value "))
input_int2 = int(raw_input("Enter the end value "))
print main(input_int1,input_int2)
