#usr/bin/python2.7

def square_sum(n):
    return 4*n**2 - 6*(n-1)

def solve(n):
    summation = 1
    for i in range(3,n+1,2):
        summation += square_sum(i)
    return summation

def main():
    user_input = int(raw_input("enter the max dimension: "))
    print solve(user_input)

main()
