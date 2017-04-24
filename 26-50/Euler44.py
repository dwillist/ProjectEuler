#!usr/bin/python3

import GeneralProcs,math

def pentagonalTest(integer):
    return GeneralProcs.isSquare(1 + 24*integer) and (1 + math.sqrt(1 + 24*integer)) % 6 == 0

def finishTest(i,currentDiff):
    return 3*i + 1 > currentDiff

def minDiff(i,j):
    k = i - j
    return (3*k**2 + 6*i*k - k)//2

# actually does this problem correctly
def solve2():
    solutions = []
    d = 1
    i = 1
    while(len(solutions) < 3):
        Pd = GeneralProcs.pentagonal(d)
        Pi = GeneralProcs.pentagonal(i)
        n,rem = divmod(Pd-Pi,3*i)
        #print("Pi: {i},Pd: {d}".format(i=Pi,d=Pd))
        if Pi >= Pd:
            d += 1
            i = 0
        elif rem == 0 and pentagonalTest(GeneralProcs.pentagonal(n) + GeneralProcs.pentagonal(n+i)):
            #print(str([i,d]))
            #print(divmod((Pd - Pi),3*i))
            solutions.append(Pd)
            print(solutions)
        # update
        i += 1
    return solutions



def solve():
    i = 2
    j = 1
    minj = 1
    currentPi = 0
    currentPj = 0
    currentDiff = float('inf')
    while(not finishTest(i-1,currentDiff)):
        #print("i: " + str(i) + " j: " + str(j))
        if(j >= i): # or minDiff(i,j) > currentDiff):
            i += 1
            minj = int(max(GeneralProcs.quadraticFormula(-3,1,i*(3*i-1) - 2*currentDiff)))
            print("minj: {m} and i: {i}".format(m=minj,i=i))
            j = max(minj,1)
            j = 1
        Pi = GeneralProcs.pentagonal(i)
        Pj = GeneralProcs.pentagonal(j)
        if (Pi - Pj < currentDiff) and pentagonalTest(Pi - Pj) and pentagonalTest(Pi + Pj):
            currentPi = Pi
            currentPj = Pj
            currentDiff = Pi - Pj
            print("newDiff " + str(currentDiff))
            print("new Pi: " + str(Pi) + " new Pj: "+ str(Pj))
            print("i: " + str(i) + " j: " + str(j))
        # increment
        j += 1
    return currentPi,currentPj,currentDiff

print(solve2())
print("post solve")
