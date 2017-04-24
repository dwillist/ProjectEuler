#!/usr/bin/python2.7

# here we are actually going to use a dictionary to make our memoization more efficient
# our previousl model used a list and it was highly inefficent! due to the sparseness of values we used
# in high numbers

kollatz_dict = {1:0} # this is just the starting value

def kollatz(k):
    if( k in kollatz_dict):
        return kollatz_dict[k]
    else:
        if(k % 2 == 0):
            kollatz_dict[k] = kollatz(k/2) + 1
        else:
            kollatz_dict[k] = kollatz(3*k + 1) + 1
        return kollatz_dict[k]

def pair_max(dictionary):
    max_pair = (0,0)
    for pair in dictionary.items():
        if pair[1] > max_pair[1]:
            max_pair = pair
    return max_pair



def populate_dict(int_range):
    for val in range(1,int_range+1):
        kollatz(val)
    return pair_max(kollatz_dict)


print populate_dict(1000000)
