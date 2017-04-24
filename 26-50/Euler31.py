# here we just need to do a bit of memoization

coinArray = [1,2,5,10,20,50,100,200]

memoArray = [[None for i in coinArray] for j in range(201)]

# coinIndex should start at 7
def countCoins(value,coinArray,coinIndex,memoArray):
    if value > 0 and coinIndex >= 0:
        if memoArray[value][coinIndex]:
            return memoArray[value][coinIndex]
        else:
            memoArray[value][coinIndex] = (countCoins(value - coinArray[coinIndex],coinArray,coinIndex,memoArray) +
                        countCoins(value,coinArray,coinIndex-1,memoArray))
            return memoArray[value][coinIndex]
    elif value == 0:
        return 1
    return 0

def main():
    print("number of ways to make 200 quid")
    print(countCoins(200,coinArray,7,memoArray))
    print(memoArray[200][7])


main()
