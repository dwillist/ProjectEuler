# our first objective is just to brute force generate the solutions for
# cycles of length 4


def perm_gen(n):
    if(n > 1):
        gen_list = []
        for item in perm_gen(n-1):
            for position in range(len(item)+1):
                gen_list.append(item[:position] + [n] + item[position:])
        return gen_list
    else:
        return [[1]]

def cycle_len(cycle_list):
    cycle = 0
    current_list = [i for i in range(1,len(cycle_list) + 1)]
    new_list = []
    while cycle == 0 or not all(current_list[j] <= current_list[j+1] for j in xrange(len(cycle_list)-1)):
        for pos in  cycle_list:
            new_list.append(current_list[pos-1])
        current_list = new_list
        new_list = []
        cycle += 1
    return cycle


def main():
    user_input = int(raw_input("enter the number you want to gen: "))
    perm_list = perm_gen(user_input)
    perm_dict = {}
    for perm in perm_list:
        size = cycle_len(perm)
        if(size in perm_dict):
            perm_dict[size] += 1
        else:
            perm_dict[size] = 1
    for key in perm_dict:
        print "Cycle Size - " + str(key) + " Count - " + str(perm_dict[key])

main()
