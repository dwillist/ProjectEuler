#usr/bin/python3

def countPairs(p):
    count = 0
    for i in range(1,int(p/2)):
        for j in range(1,i+1):
            k = p-i-j
            if k > i and i**2 + j**2 == k**2:
                #print([i,j,k])
                count += 1
    return count


def solve():
    maxp = 0
    maxcount = 0
    for i in range(3,1000):
        c = countPairs(i)
        if countPairs(i) > maxcount:
            maxcount = c
            maxp = i
    print(maxp)
    print(maxcount)

print(solve())
