#include/bin/python3

def gcd(a,b):
    while b>0:
        temp = a % b
        a = b
        b = temp
    return a

def simplify(num,denom):
    div = gcd(denom,num)
    return num/div , denom/div

def incorrectSimp(num,denom):
    newDenom = str(denom)
    newNum = str(num)
    for i in newDenom:
        if i in newNum:
            newDenom = newDenom.replace(i,'',1)
            newNum = newNum.replace(i,'',1)
    if newNum == '' or newDenom == '':
        return 1,1
    else:
        return int(newNum),int(newDenom)

def solve():
    for denom in range(10,100):
        for num in range(10,denom):
            wrongDenom,wrongNum = incorrectSimp(denom,num)
            if simplify(denom,num) == simplify(wrongDenom,wrongNum):
                print(str([wrongDenom,wrongNum]) + ":" + str([denom,num]))


def main():
    for denom in range(10,100):
        for num in range(10,denom):
            wrongN,wrongD = incorrectSimp(num,denom)
            simpN,simpD = simplify(wrongN,wrongD)
            n,d = simplify(num,denom)
            if (denom != wrongD and num != wrongN)  and (n == simpN and d == simpD) and ((num%10 != 0) or (denom%10 != 0)):
                print(str(num)+'/'+str(denom)+'='+str(n)+'/'+str(d))

main()
