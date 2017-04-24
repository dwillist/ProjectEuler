from math import factorial

def factorialSum(s,factArray):
    summation = 0
    for i in str(s):
        summation += factArray[int(i)]
    return summation == s


def solve():
    solutionArray = []
    factArray = [factorial(i) for i in range(10)]
    for i in range(10,factorial(9) * 7):
        if factorialSum(i,factArray):
            solutionArray.append(i)

    return solutionArray


def main():
    lis = solve()
    print(lis)
    print(sum(lis))

main()
