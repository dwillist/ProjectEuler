
def fact(n):
    if n == 0:
        return 1
    else:
        return n * fact(n-1)

def main():
    string = str(fact(100))
    s = 0
    for element in string:
        s += int(element)
    print s

main()
