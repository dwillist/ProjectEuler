import time,math
#Globals#
factorial = []
# perm dict is a muti layered dictionary perm_dict[permutation_length]
# while give you a dictionary of the cycle breakdown for permutation of given length
perm_dict={}
divisor_array = []

# order O(n**2)
# notice that we can easily make this O(n**(3/2)) but that this is NOT
# going to be a rate limiting step during these computations
def populate_divisor(n):
    for val in xrange(n+1):
        divisor_array.append([div for div in xrange(1,val+1) if val % div == 0])


def populateFactorial(n):
    for val in xrange(n+1):
        if(val == 0):
            factorial.append(1)
        else:
             factorial.append( factorial[val-1] * val)

def perm_initialize(n):
    perm_dict[0] = {0:{0:1}}

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
# NOTE it is NOT the case that i*k = n
# but n >= i * k
# and that factorial has been populated
def identical_cycles(n,k,i):
    if n < i*k:
        print "ERROR"
    return (factorial[n]*factorial[k-1]**i)/((factorial[k]**i) * factorial[i] * factorial[n-(i*k)])

def combine(n):
    global perm_dict
    perm_dict[n] = {}
    for new_cycle_len in xrange(1,n+1): # new cycle length to add
        for div in divisor_array[new_cycle_len]: # div = all divisors of |new_cycle_len|
        # it is important to note that new_cycle_len/div is the number of cycles we are making
        # div is the size of the new cycles
            for max_cycle_len in perm_dict[n-new_cycle_len]:
                 # max_cycle_len is the max cycle length of the cycles that we have ALREADY constructed
                if div > max_cycle_len:
                    for total_cycle_len in perm_dict[n-new_cycle_len][max_cycle_len]:
                        # total_cycle_len are the actual lengths of permutations that have a max
                        # cycle length of < div
                        leastCM = lcm(div,total_cycle_len)
                        new_perm_count = identical_cycles(n,div,new_cycle_len/div) * perm_dict[n-new_cycle_len][max_cycle_len][total_cycle_len]
                        #if leastCM == 2 and n == 4:
                            #print n
                            #print "new_cycle_len : " + str(new_cycle_len)
                            #print "leastCM : " + str(leastCM)
                            #print "new_perm_count : " + str(new_perm_count)
                            #print "identical_cycles : " +str(identical_cycles(n,div,new_cycle_len/div))
                            #print "div: : " + str(div)
                            #print "max_cycle_len : " + str(max_cycle_len)
                            #print "total_cycle_len : " + str(total_cycle_len)
                        if div not in perm_dict[n]:
                            perm_dict[n][div] = {}
                        if leastCM in perm_dict[n][div]:
                            perm_dict[n][div][leastCM] += new_perm_count
                        else:
                            perm_dict[n][div][leastCM] = new_perm_count
    #            else:
    #                break
    #if n in perm_dict[n]:
    #    perm_dict[n][n][n] = factorial[n-1]
    #else:
    #    perm_dict[n][n] = {}
    #    perm_dict[n][n][n] = factorial[n-1]

def myFormat(perm_dict,p_length):
    new_dict = {}
    for dictionary in perm_dict[p_length].values():
        #here dictionary is of the form {len:count}
        for cycle_len in dictionary:
            if cycle_len in new_dict:
                new_dict[cycle_len] += dictionary[cycle_len]
            else:
                new_dict[cycle_len] = dictionary[cycle_len]
    return new_dict

def pprint(formatted_dict):
    for key in formatted_dict:
        print "Cycle Size : " + str(key) + " Count : " + str(formatted_dict[key])

def op_lengths(formatted_dict,func):
    summation = 0
    for key in formatted_dict:
        summation += func(key) **2 *formatted_dict[key]
    return summation

def correctTokDigits(val1,val2,k):
    return len(str(val1)) == len(str(val2)) and str(val1)[:k] == str(val2)[:k]


def modified_lengths(formatted_dict,func,totalSum):
    currentSum = 0
    keys = sorted(list(formatted_dict.keys()),key=lambda x : -x)
    for key in keys:
        if not correctTokDigits(currentSum,totalSum,10):

            currentSum += func(key) **2 * formatted_dict[key]
        else:
            print "used keys:"
            for i in keys[:key]:
                print "key: " + str(i) + " count: " + str(formatted_dict[i])
            print "CurrentSum: " +str(currentSum)
            return keys.index(key),len(keys)



def approximationOp(formatted_dict,func,maxLen,permLength,factorialProd):
    summation = 0
    remainingLen = maxLen - permLength
    #key is the cycle length
    print formatted_dict
    for key in formatted_dict:
        print str(permLength) + "|" + str(key) + ":" + str(formatted_dict[key])
        toAdd = lcm(func(key),maxLen-permLength) ** 2 * formatted_dict[key] * factorialProd
        summation += lcm(func(key),maxLen-permLength) ** 2 * formatted_dict[key] * factorialProd
    return summation

def mainApproximation(k):
    # first we should try and predict a value we know the answer to m = 100
    #Total Sum
    #502255597001070293433447827865056690699895513118781873968548138624380986043
    #496352442946642396814779582835467528835712265038971629716699453535522375170
    #8883254956452220901
    # divided solution
    #53817203945.5
    m = 100
    #m = 20
    global perm_dict
    populate_divisor(k)
    populateFactorial(351)
    perm_initialize(k)
    total = 0
    #print divisor_array
    for i in xrange(1,k+1):
        combine(i)
    #print "done combining"
    for j in range(0,k+1):
        f_dict = myFormat(perm_dict,j)
        total += approximationOp(f_dict,lambda x : x,m,j,factorial[m-j-1])
    #print op_lengths(f_dict,lambda(x): x)
    print(total)
    print ansify(total/factorial[m])

def ansify(integer):
    stringInt = str(integer)
    return stringInt[:10] + 'e' + str(len(stringInt) -1)

def main(user_input):
    start_time = time.time()
    #user_input = int(raw_input("enter n: "))
    populate_divisor(user_input)
    populateFactorial(user_input)
    perm_initialize(user_input)
    #print divisor_array
    for i in xrange(1,user_input+1):
        combine(i)
    #print "done combining"
    f_dict = myFormat(perm_dict,user_input)
    #pprint(f_dict)
    toPrint = op_lengths(f_dict,lambda(x): x)
    lastkey,totalKeys = modified_lengths(f_dict,lambda(x) : x,toPrint)
    print toPrint
    print float(toPrint)/math.factorial(user_input)
    print "Key info:"
    print "total keys:" + str(totalKeys) + "| Last key:"  + str(lastkey)
    #print perm_dict
    #print("--- %s seconds ---" % (time.time() - start_time))

#for i in range(2,20):
#    main(i)
main(int(raw_input("enter n: ")))
#mainApproximation(50)
