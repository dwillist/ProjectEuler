#!/usr/bin/python2.7

#global

array = [0,0]
for i in range(1200000):
    array.append(-1)



def seq_step(n):
    if n > 100000000:
        print n
    if( n % 2 == 0):
        next_val = n/2
    else:
        next_val = 3*n + 1
    ######################
    if array[n] == -1:
        array[n] = seq_step(next_val) + 1
    return array[n]

def run_seq_steps():
    for k in range(1,1000):
        seq_step(k)
    return


def getlargest():
    max_val = 0
    for val in array:
        if max_val < val:
            max_val = val
    return max_val


run_seq_steps()
print array
print getlargest()
