import math

def factorsum(n):
    current_sum = 1
    for val in range(2,int(math.sqrt(float(n))) + 1):
        if n % val == 0 and val**2 != n:
            current_sum += (val + n/val)
        elif n % val == 0:
            current_sum += val
    return current_sum

def genAbundent(n):
    abundent_list = []
    for val in range(1,n+1):
        if factorsum(val) > val:
            abundent_list.append(val)
    return abundent_list

def get_all_sums(abundent_list,n):
    sum_dict = {}
    for index_A in range(len(abundent_list)):
        for index_B in range(index_A+1):
            if abundent_list[index_A] + abundent_list[index_B] > n:
                break
            else:
                sum_dict[(abundent_list[index_A] + abundent_list[index_B])] = 1
    return sum_dict

def calc_non_abundent(sum_dict,n):
    summation = ((n+1)* n)/2
    for key in sum_dict:
        summation -= key
    return summation


def main():
    #print get_all_sums(genAbundent(100))
    n = 20161
    lis = genAbundent(n)
    dic = get_all_sums(lis,n)
    to_print = calc_non_abundent(dic,n)
    print to_print


main()
