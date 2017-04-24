import GeneralProcs

def hept(n):
    return n*(2*n-1)

def solve():
    solutions = []
    i = 1
    while len(solutions) < 3:
        val = hept(i)
        if GeneralProcs.pentagonalTest(val) and GeneralProcs.triangularTest(val):
            solutions.append(val)
        i+=1
    return solutions

print(solve())
