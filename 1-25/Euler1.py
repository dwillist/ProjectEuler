#!/usr/bin/python2.7
def main(input_integer):
    count = 0
    for val in range(1,input_integer):
        if (val % 3 == 0) or (val % 5 == 0):
            count += val
    return count



user_value = int(raw_input("Enter an integer "))
print(main(user_value))
