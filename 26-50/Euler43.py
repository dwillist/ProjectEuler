from itertools import permutations

def prop(string,primes):
    for i in range(7):
        #print(string[i+1:i+4] + "divided by: " + str(primes[i]))
        if int(string[i+1:i+4]) % primes[i] != 0:
            return False
    return True


def solve():
    primes = [2,3,5,7,11,13,17]
    propCount = 0
    sumCount = 0
    for perm in permutations('0123456789',10):
        permString = ''.join(perm)
        if prop(permString,primes):
            propCount += 1
            sumCount += int(''.join(perm))
    return propCount,sumCount


print(solve())
#print(prop('1406357289',[2,3,5,7,11,13,17]))
