#!usr/bin/python2.7

#Globals#
factorial = []

# perm dict is a muti layered dictionary perm_dict[permutation_length]
# while give you a dictionary of the cycle breakdown for permutation of given length
perm_dict={}
divisor_dict = {}

def populate_divisor(n):
    for val in range(1,n+1):
        divisor_dict[val] = {}
        for div in xrange(1,val+1):
            if(val % div == 0):
                divisor_dict[val][div] = val/div


def populateFactorial(n):
    for val in range(n+1):
        if(val == 0):
            factorial.append(1)
        else:
             factorial.append( factorial[val-1] * val)


def nCk(n,k):
    return factorial[n] / (factorial[k] * factorial[n-k])

def gcd(a,b):
    if(a < b):
        return gcd(b,a)
    else: # b > a
        while( a > 0):
            temp = a
            a = b % a
            b = temp
        return b

def lcm(a,b):
    if (min(a,b) == 0):
        return max(a,b)
    return (a * b) / gcd(a,b)

# counts the number of structures (k)(k)...cycle_count...(k) [ rest ]
def cycle_struct(k,cycle_count,n):
    current_perm = n-(cycle_count*k)
    lcm_sum = 0
    if(current_perm >= 0):
        for cycle_length in perm_dict[current_perm]: # this should iterate through cycle lengths
            if cycle_length > k:
                break
            else:
                if(lcm(cycle_length,k) == k):
                    lcm_sum += perm_dict[current_perm][cycle_length] # adds # of cycles of length cycle_length
        #print "LCM sum: " + str(lcm_sum)
        #print "for current_perm: " + str(current_perm)
        return (factorial[n] * factorial[k-1]**cycle_count * lcm_sum)/( (factorial[k]**cycle_count) * factorial[cycle_count] * factorial[current_perm])
    return 0


# TEST this
def IE_cycles(k,n):
    sign = -1
    k_count = 2
    to_return = 0
    while(n >= k_count*k):
        to_return += (cycle_struct(k,k_count,n)*sign)
        sign *= -1
        k_count += 1
    return to_return

def cycle_count(n):
    perm_dict[n] = {1:1}
    for val in range(2,n+1): # these are the sizes of the cycles we are adding
        for cycle_len in perm_dict[n-val]:
            # these are the cycle lengths of a permutation of n-val size
            if( cycle_len <= val): # explicitly prevent double counting due to large cycles
                                   # occuring in the permutation portion.
                new_cycle_len = lcm(cycle_len,val)

                new_cycle_count = nCk(n,val) * factorial[val-1] * perm_dict[n-val][cycle_len]
                if new_cycle_len == 6 and n == 8:
                    print "val : " + str(val)
                    print "cycle_len : " + str(cycle_len)
                    print "cycle_count : " + str(new_cycle_count)
                if new_cycle_len in perm_dict[n]:
                    perm_dict[n][new_cycle_len] += new_cycle_count
                else:
                    perm_dict[n][new_cycle_len] = new_cycle_count
        if n >= 2*val: # need to make sure remove double counting!
            #print "IE_cycles being called for " + str(val) + " in " + str(n)
            ie_val = IE_cycles(val,n)
            #print ie_val
            perm_dict[n][val] += ie_val



################################################################################
# New code:

# here we assume that we can access elements in our permutaioin dict as follows:
# perm_dict[n'][l][c] this will give us
# permutations of length n'
# the largest loop l
# the cycle length c
# the above dictionary access will return the count of all such permutations matching
# this criteria

def initialize_perm_dict(n):
    perm_dict[1] = {1:{1:1}}
    #for i in xrange(1,n+1)
    #perm_dict[i] = {1:{1:1}}

# number of ways of constructing i cycles of length k from n elements
# here we require that i*k = n
# and that factorial has been populated
def identical_cycles(n,k):
    i = n/k
    return (factorial[n]*factorial[k-1]**i)/((factorial[k]**i) * factorial[i])

def combine(n):
    perm_dict[n] = {}
    for new_cycle_len in xrange(1,n): # new cycle length to add
        for div in divisor_dict[new_cycle_len]: # div = all divisors of |new_cycle_len|
            for max_cycle_len in perm_dict[n-new_cycle_len]: # max_cycle_len is the max cycle length of the cycle
                if div > max_cycle_len:
                    for total_cycle_len in perm_dict[n-new_cycle_len][max_cycle_len]:
                        leastCM = lcm(div,total_cycle_len)
                        new_perm_count = identical_cycles(new_cycle_len,div) * perm_dict[n-new_cycle_len][max_cycle_len][total_cycle_len]
                        if div not in perm_dict[n]:
                            perm_dict[n][div] = {}
                        if leastCM in perm_dict[n][div]:
                            perm_dict[n][div][leastCM] += new_perm_count
                        else:
                            perm_dict[n][div][leastCM] = new_perm_count
    if n in perm_dict[n]:
        perm_dict[n][n][n] = factorial[n-1]
    else:
        perm_dict[n][n] = {}
        perm_dict[n][n][n] = factorial[n-1]

def pprint(perm_dict,p_length):
    for cycle_len in perm_dict[p_length]:
        print "     " + str(cycle_len) + ": " + str(sum(perm_dict[p_length][cycle_len].values()))



def main():
    user_input = int(raw_input("enter n: "))
    populate_divisor(user_input)
    print divisor_dict
    populateFactorial(user_input)
    for i in range(1,user_input+1):
        combine(i)
        pprint(perm_dict,i)
    for row in perm_dict:
        print str(row) + str(perm_dict[row])


main()
