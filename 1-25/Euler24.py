#/usr/bin/python2.7

from math import factorial

# list_left is a list of the form [k1,k2,...,kn]
# where ki < k(i+1), so it is linearly ordered.
#
def lexographicFactorial(list_left,k,current_permutation = []):
    if len(list_left) == 0:
        return current_permutation
    else:
        permuations_per_fixed_element = factorial(len(list_left) - 1)
        index = (k-1) / permuations_per_fixed_element
        current_permutation.append(list_left[index])
        new_k = k - ((index + 1) * permuations_per_fixed_element)
        list_left.pop(index)
        return lexographicFactorial(list_left,new_k,current_permutation)

def main():
    l = range(10)
    num = 10**6
    result = lexographicFactorial(l,num)
    print "".join([str(i) for i in result])

main()
