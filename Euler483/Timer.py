import sys
import os
import time
sys.path.append(os.path.abspath("/Users/danielthornton/Dropbox/CompProg/projectEuler/Euler483/"))
import New


def time_main(n):
    start_time = time.time()
    # need to reset all of our globals
    New.factorial = []
    New.perm_dict={}
    New.divisor_array = []
    New.main(n)
    runtime = time.time() - start_time
    return '{:.6f}'.format(runtime)

def main2():
    user_input = int(raw_input("enter n: "))
    x_list = [str(i) for i in xrange(1,user_input+1)]
    y_list = [time_main(int(x)) for x in x_list]
    x_csv = open("/Users/danielthornton/Dropbox/CompProg/projectEuler/Euler483/x.csv",'w')
    y_csv = open("/Users/danielthornton/Dropbox/CompProg/projectEuler/Euler483/y.csv",'w')
    x_csv.write(",".join(x_list))
    y_csv.write(",".join(y_list))
    print "Done"
    #print ", ".join(x_list)
    #print ", ".join(y_list)

#main2()
user_input = int(raw_input("get n: "))
print time_main(user_input)
