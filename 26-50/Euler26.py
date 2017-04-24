#usr/bin/python2.7

from math import log

# here we have
def decimal_length(denom):
    num = 10
    num_list = []
    decimal = ""
    while num not in num_list:
        num_list.append(num)
        decimal += str(num/denom)
        num = num % denom * 10
    return decimal[num_list.index(num)::]



def main():
    user_input = int(raw_input("Enter a value to calculate: "))
    dec_list = [decimal_length(i) for i in xrange(2,user_input+1)]
    #for index in range(len(dec_list)):
        #print str(index+2) + " : " + dec_list[index]
    len_list = [len(i) for i in dec_list]
    #print len_list
    m = max(len_list)
    print_index = len_list.index(m) + 2
    print str(m) + " at " + str(print_index)
main()
