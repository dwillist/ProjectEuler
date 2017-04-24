#!/usr/bin/python2.7

alpha_dict = {'A':1,'B':2,'C':3,'D':4,'E':5,'F':6,'G':7,'H':8,'I':9,'J':10,'K':11,'L':12,'M':13,'N':14,'O':15,
'P':16,'Q':17,'R':18,'S':19,'T':20,'U':21,'V':22,'W':23,'X':24,'Y':25,'Z':26}

def value_calc(string):
    s = 0
    for char in string:
        s += alpha_dict[char]
    return s

def main():
    summation = 0
    handle = open("/Users/danielthornton/Dropbox/CompProg/projectEuler/22.in",'r')
    file_line = handle.readline()
    current_string = ""
    array = []
    for char in file_line:
        if(char.isalpha()):
            current_string += char
        else:
            if current_string != "":
                array.append(current_string)
                current_string = ""
    array = sorted(array)
    for pos in range(len(array)):
        if(array[pos] == "COLIN"):
            print "COLIN"
            print str(value_calc(array[pos])) + " " + str(pos+1)

        summation += value_calc(array[pos]) * (pos+1)
    print summation


main()
