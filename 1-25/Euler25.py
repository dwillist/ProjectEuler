#usr/bin/python2.7

def first_fibo(length):
    a = 1
    b = 1
    index = 2
    while(len(str(b)) < 1000):
        temp = b
        b += a
        a = temp
        index += 1
    return index

def main():
    print first_fibo(1000)

main()
