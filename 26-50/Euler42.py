import GeneralProcs,math


def wordToInt(word):
    summation = 0
    for letter in word.strip('"'):
        summation += ord(letter) - 64
    return summation

def isTriangle(integer):
    return int(math.sqrt(1 + 8*integer))**2 == (8*integer +1)

def solve():
    fileObject = open("p042_words.txt")
    triangleCount = 0
    for line in fileObject:
        lis = line.split(',')
        for word in lis:
            if isTriangle(wordToInt(word)):
                triangleCount += 1

    return triangleCount

print(solve())
