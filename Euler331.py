# Problem Euler 331
import math
import itertools


def solveat(x,y):
    for i in range(2,x):
        a = Lattice(i)
        a.printLat()
        b = a.solve()
        print b(y)

class Lattice:
    """ a class for Euler 331, 1 -> black, 0 -> white"""
    def __init__(self,n):
        self.vec = []
        self.size = n
        for i in range(n):
            self.vec.append([])
            tempString = ""
            for j in range(n):
                comp = math.sqrt(math.pow(i,2) + math.pow(j,2))
                if (n-1) <= comp and comp < (n):
                    self.vec[i].append(1)
                else:
                    self.vec[i].append(0)

    def flipBit(self,i,j):
        if self.vec[i][j] == 1:
            self.vec[i][j] = 0
        else:
            self.vec[i][j] = 1
            
    def flipOperation(self,i,j):
        for k in range(self.size):
            self.flipBit(i,k)
            if k != i:
                self.flipBit(k,j)

    def chainFlipOperation(self,vector):
        """preforms a flip operations for all tuples in vector"""
        for tup in vector:
            self.flipOperation(tup[0],tup[1])
            

                
    def printLat(self):
        for i in self.vec:
            print i

    def isSolved(self):
        solved = True
        for i in range(self.size):
            for j in range(self.size):
                if self.vec[i][j] != 0:
                    solved = False
        return solved

        
    #first lets see if we can determine weather or not a puzzle is solvable
    def solve(self,moves =[]):
        # to get positions
        def solve_for_bound(bound):
            possible_moves = []
            for i in range(bound):
                print "@ ", i
                combos = itertools.product(range(self.size),repeat = 2)
                iLengthMoves = itertools.combinations(combos,i)
                for moveSet in iLengthMoves:
                    self.chainFlipOperation(moveSet)
                    if self.isSolved():
                        return moveSet
                    self.chainFlipOperation(moveSet)
            return ()
        return solve_for_bound


                
                
    def solve_at_bound(self,i):
        """ i is the bound to solve at"""
        #TODO: add precentage done bar
        max_combos = math.factorial(self.size) 
        supress = False
        combo_count = 0
        combos = itertools.product(range(self.size),repeat = 2)
        iLengthMoves = itertools.combinations(combos,i)
        for moveSet in iLengthMoves:
            combo_count += 1.0
            p = int(combo_count / max_combos * 10)
            if (( p  % 10) == 0) and not supress:
                #print p, "% done"
                supress = True
            if p%10 != 0:
                supress = False
            self.chainFlipOperation(moveSet)
            if self.isSolved():
                return moveSet
            self.chainFlipOperation(moveSet)
        return ()
          
            
                
                
    def solveRange(self, k ):
        for i in range(1,k):
            print "at ", i , " out of " , k
            temp = self.solve_at_bound(i)
            if temp != ():
                return temp

    def _removable(self,lis,val=1):
        lis.count(val) == 1 and (lis[0] == val or lis[-1] == val) 

    
    def reduceLat():
        """ reduces current lattice and returns a new one of reduced size"""
        newVec = []
        start_slice = 0
        for i in range(self.size()):
            if self._removable(self.vec[i]):
                start_slice += 1
            else:
                # we need to add to the list
                newVec.append(self.vec[i][start_slice::])
        newLat = Lattice(self.size - start_slice)
        return newLat
                              
        
        
                           
                        
                    

            







        
