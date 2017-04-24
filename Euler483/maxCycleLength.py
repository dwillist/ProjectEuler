# here we whish to count the max cycle length as well as number of cycles of this length
import math

def isPrime(k):
    for i in range(2,int(math.sqrt(k)) + 1):
        if k % i == 0:
            return False
    return True

def calculate_max():
    pSet = []
    for i in range(2,350 + 1):
        if isPrime(i):
            pSet.append(i)
    # now we have a prime set
    index = 0
    summation = 0
    length = 1
    count = 1
    print(pSet)
    while summation + pSet[index] + pSet[index+1] < 350:
        summation += pSet[index]
        length *= pSet[index]
        index += 1
        count *= math.factorial(pSet[index] -1)
    #
    prevIndex = index
    while(summation + pSet[prevIndex+1] < 350):
        prevIndex += 1
    summation += pSet[prevIndex]
    length *= pSet[prevIndex]
    count *= math.factorial(pSet[prevIndex] - 1)
    index = prevIndex
    cycleCount = math.factorial(350)//count
    print(cycleCount,summation,length,pSet[index])
    print(length**2 * cycleCount)

calculate_max()
