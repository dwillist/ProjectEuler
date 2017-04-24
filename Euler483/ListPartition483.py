import copy

# here we also have an issue with double counting...
# consider

#here we assume that the list_dict is of the form:
#[ {cycle-dcomp},{cycle-decomp2},{...},... ]
set_dict = {}

def add_partition(part,n):
    # here we are given a partition, which is a dictionary
    part_set = {}
    for cycle in part:
        c = copy.deepcopy(part)
        part_list.append(c)
        if cycle+1 in c:
            part_set[-1][cycle+1] += 1
            part_set[-1][cycle] -= 1
            # need to add in a provision for deleting cycles of length 0
        else:
            part_set[-1][cycle+1] = 1
            part_set[-1][cycle] -= 1
        if part_set[-1][cycle] == 0:
            del part_set[-1][cycle]
    return part_set


def list_partions(n):
    global set_dict
    new_set = {{1:n}}
    for partition in set_dict:
        new_set = new_set.union( add_partition(partition,n) )
    set_dict = new_set
    return


def main():
    global list_dict
    n = int(raw_input("enter n: "))
    list_dict = [{1:1}]
    for val in range(2,n+1):
        list_partions(val)
        #partition_dict[val] = {1:1}
    print list_dict
    #partition_count(n,n)
    #for key in partition_dict:
        #print str(key) + " : " + str(partition_dict[key])
main()
