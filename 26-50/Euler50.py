


import GeneralProcs

def solve():
    compositeSet,primeSet = GeneralProcs.makeSieve(1000000)
    primeList = sorted(list(primeSet))
    maxSum = 0
    maxLength = 0
    for startPos in range(len(primeList)):
        for endPos in range(max(startPos+1,maxLength+startPos),len(primeList)+1):
            #print([startPos,endPos])
            summation = sum(primeList[startPos:endPos])
            if summation in primeSet and endPos - startPos > maxLength:
                    maxSum = summation
                    maxLength = endPos - startPos
            if summation > 10**6:
                break
            #if (endPos - startPos) < maxLength:
                #break

    print(maxLength,maxSum)


solve()
