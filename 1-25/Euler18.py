#!/usr/bin/python2.7


def open_file(path):
    return open(path,'r')

def valid(row,col,array):
    if(row >= 0 and row < len(array)):
        if(col >= 0 and col < len(array[row])):
            return True
    return False

#here we need to use dynamic programming once again except now it is going to be 2D
def solve(row,col,array,memo):
    if valid(row,col,array):
        if((row,col) in memo):
            return memo[(row,col)]
        else:
            memo[(row,col)] = array[row][col] + max(solve(row+1,col,array,memo), solve(row+1,col-1,array,memo))
            return memo[(row,col)]
    return 0




def main():
    handle = open_file("/Users/danielthornton/Dropbox/CompProg/projectEuler/67.in")
    array = []
    for line in handle:
        current_list = map(int,line.rstrip('\n').split(" "))
        array.append(current_list)
    array.reverse()
    # now we have a reversed array
    max_row = len(array) -1
    max_col = len(array[max_row]) -1
    memoization_dict = {(max_row,max_col) : array[max_row][max_col]}
    #print array
    for index in range(len(array[0])):
        solve(0,index,array,memoization_dict)
    #print memoization_dict
    print max(memoization_dict.values())

main()
