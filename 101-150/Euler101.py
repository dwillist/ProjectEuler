#usr/bin/python2.7

# here we need to preform some gaussian elemination on a matrix to get our solution

class Matrix:
    # here coefficent lists is a list of lists
    def __init__(self,coefficent_list):
        self.coefficent_list = coefficent_list

    def gaussian(self):
        # this will attempt to normalize the entire vector as much as possible
        
