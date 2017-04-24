#usr/bin/python3

def pentagonal(x,y):
    string = str(x) + str(y) + str(x*y)
    if len(string) == 9:
        for i in range(1,10):
            if not str(i) in string:
                return False
        return True
    return False

def solve():
    prodList = []
    for x in range(1,10001):
        for y in range(1,x+1):
            if len(str(x) + str(y) + str(x*y)) > 9:
                break
            elif pentagonal(x,y):
                print(x,y,x*y)
                prodList.append(x*y)
    return prodList

def main():
    a = solve()
    summation = sum(list(set(a)))
    print(summation)

main()
