#/usr/bin/python2.7

def main():
    file_handle = open(raw_input("Enter file path: "),'r')
    array = []
    for line in file_handle:
        array.append(int(line))
    # now we have an array filled with each number
    our_sum = sum(array)
    while(len(str(our_sum)) > 10):
        our_sum = int(our_sum/10)
    print our_sum


main()
