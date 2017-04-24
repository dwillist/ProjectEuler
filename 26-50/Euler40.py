#!usr/bin/python3

def solve():
    # here we are just going to creat a super long string...
    i = 0
    length = 0
    string = ''
    while length <= 30 + 10**6:
        string += str(i)
        i += 1
        length += len(str(i))

    prod = 1
    print(len(string))
    for i in range(7):
        print(string[10**i])
        prod *= int(string[10**i])
    return prod

print(solve())
