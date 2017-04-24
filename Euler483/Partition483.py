#!/usr/bin/python2.7

partition_dict = {}

# just test this function to see if it will run effectively on 350
def partition_count(n,k):
    #print "New Call"
    #print str(n) + " : " + str(k)
    if n == 0:
        return 1
    else:
        current_sum = 0
        for i in xrange(1,min(k+1,n+1)):
            if i in partition_dict[n-i]:
                 current_sum += partition_dict[n-i][i]
            else:
                current_sum += partition_count(n-i,i)

        partition_dict[n][k] = current_sum
        return current_sum

def combinatorial_count(i,n,k):
    if n == 0:
        return 1
    else:
        current_sum = 0
        for i in xrange(1,min(k+1,n+1)):
            if i in partition_dict[n-i]:
                 current_sum += partition_dict[n-i][i]
            else:
                current_sum += partition_count(n-i,i)

        partition_dict[n][k] = current_sum
        return current_sum

def main():
    n = int(raw_input("enter n: "))
    partition_dict[0] = {0:1}
    for val in range(1,n+1):
        partition_dict[val] = {1:1}
    partition_count(n,n)
    #for key in partition_dict:
        #print str(key) + " : " + str(partition_dict[key])
    print partition_dict[n][n]
main()
