# First attempt at implementation was very wrong... went throught a LOT of repeated numbers

# here we come up with a better way to do this.

def generateAllKeys(starCount,barCount):
    if starCount == 0:
        return ['-' * barCount]
    elif barCount == 0:
        return ['*' * starCount]
    else:
        totalLen = starCount + barCount
        toReturn = []
        for i in generateAllKeys(starCount-1,barCount):
            toReturn.append(i + '*')
        for j in generateAllKeys(starCount,barCount-1):
            toReturn.append(j + '-')
        return toReturn

def primeSieve(n,primeSet = set(),compositeSet = set()):
    # prime sieve method
    for i in range(2,n+1):
        if not (i in compositeSet):
            primeSet.add(i)
            for j in range(2*i,n+1,i):
                compositeSet.add(j)
    return primeSet,compositeSet

def combine(key,value):
    strValue = str(value)
    if len(strValue) < key.count('-'):
        strValue = '0' * (key.count('-') - len(strValue)) + strValue
    newVal = ''
    strPos = 0
    for i in key:
        if i != '*':
            newVal += strValue[strPos]
            strPos += 1
        else:
            newVal += '*'
    return newVal

def genGroup(protoString):
    returnSet = set()
    startPos = int(protoString[0] == '*')
    for i in range(startPos,10):
        newStr = ''
        for value in protoString:
            if value == '*':
                newStr += str(i)
            else:
                newStr += value
        returnSet.add(int(newStr))
    return returnSet

def generateAllNumbers(key):
    #here we have to watch a few different cases
    # case 1
    starCount = key.count('*')
    barCount = len(key) - starCount
    if key[0] == '*':
        # then we don't to worry about generating numbers
        return [combine(key,i) for i in range(10**barCount - 1)]
    else:
        # then we do as our key is of the form -... so we can't let the first number be a zero
        return [combine(key,i) for i in range(10**(barCount-1),10**barCount)]

def solve():
    pS,cS = primeSieve(10**6)
    for numLength in range(1,7):
        for stars in range(1,numLength):
            keys = generateAllKeys(stars,numLength-stars)
            #print("keys")
            #print(keys)
            for key in keys:
                nums = generateAllNumbers(key)
                for num in nums:
                    #print("num")
                    #print(num)
                    groupSet = genGroup(num)
                    #print("groupSet")
                    #print(groupSet)
                    intersect = groupSet.intersection(pS)
                    if(len(intersect) == 8):
                        print(intersect)

solve()
