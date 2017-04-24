#usr/bin/python2.7

from math import sqrt

# So here we make the distinction that we only have to produce prime numbers for
# consecutive values of n, this does NOT mean that we have to produce consecutive primes


class polynomial():
    def __init__(self,coefficent_list= []):
        self.coefficent_list = coefficent_list
        self.degree = len(coefficent_list)

    def __str__(self):
        return ",".join([str(i) for i in self.coefficent_list])

    def evaluate(self,x):
        to_return = 0
        power = 0
        for coefficent in self.coefficent_list:
            to_return += coefficent * (x**power)
            power += 1
        return abs(to_return)


def prime_check(n):
    for i in range(2,int(sqrt(n))+1):
        if n % i == 0:
            return False
    return True

def main():
    # this will be a dictionary where if a key is present then a prime is presnet as well.
    user_input = int(raw_input("Enter a range |n| : "))
    prime_dictionary = {}
    polynomial_list = [polynomial([a,b,1]) for a in range(-user_input,user_input+1) for b in range(-user_input,user_input+1)]
    max_n = 0
    max_poly = None
    for poly in polynomial_list:
        n = 0
        p = poly.evaluate(n)
        #print poly
        while(p in prime_dictionary or prime_check(p)):
            if p not in prime_dictionary:
                prime_dictionary[p] = 1
            if n > max_n:
                max_n = n
                max_poly = poly
            # update new variables
            n += 1
            p = poly.evaluate(n)
    print max_n
    print max_poly
    print "playing with our maximum polynomial"
    #for i in range(2,max_n):
        #val = max_poly.evaluate(i)
        #print str(i) + " : " + str(val) + "  :  " +str(prime_check(val))

    return max_n

main()
