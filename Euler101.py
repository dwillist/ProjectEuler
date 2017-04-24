# this is the solution to Euler 101

#matrix operations
# below are some very useful matrix operations
###################################################

def getRow(matrix,n):
    # return the nth row in a matrix (Note 'first' row is at n = 0)
    if( n < len(matrix) ):
        return matrix[n]
    else:
        return False

def getColumn(matrix,n):
    # return the nth column in a matrix ( nothe the 'firts column is at n = 0)
    if n < len(matrix[0]):
        return [ row[n] for row in matrix]
    else:
        return False



def rowAddition(matrix,row_num1,row_num2,operation):
    for i in range(len(matrix[0])):
        matrix[row_num1][i] = operation(matrix[row_num1][i],matrix[row_num2][i])
        
def upperTriangulate(matrix):
    for i in range(len(matrix)):
        applyToRow(matrix,i,lambda(x): float(x)/matrix[i][i])
        for k in range( i+1 , len(matrix)):
            rowAddition(matrix,k,i,lambda x,y : x - y*(matrix[k][i]))

def solveMatrix(matrix):
    for i in range(len(matrix)):
        applyToRow(matrix,i,lambda(x): float(x)/matrix[i][i])
        for k in range(len(matrix)):
            if k!= i:
                applyToRow(matrix,k,lambda(x) : float(x)/matrix[k][i])
                rowAddition(matrix,k,i,lambda x,y: x - y)


                
def extractSol(solvedTrix):
    return [solvedTrix[i][-1]/solvedTrix[i][i] for i in range(len(solvedTrix))]

        


# add a vector and its solution togeather to make a single vector system
def addsolutionVector(eqTrix,solVec):
    if len(solVec) == len(eqTrix):
        # then this is possible
        for i in range(len(eqTrix)):
            eqTrix[i].append(solVec[i])

        return True
    return False
    
def applyToRow(matrix,row_num,function):
    # apply a function to all elements in a row
    matrix[row_num] = map(function,matrix[row_num])



def applyToColumn(matrix,col_num,function):
    #apply a function to all the elements in a column
    for row in matrix:
        row[col_num] = function(row[col_num])


#########################################################



def polynomial(coefficentList):
    def evaluate(x): # evaluate the polynomial at x
        value = 0
        for i in range(len(coefficentList)):
            value += pow(x,i)*coefficentList[i]
        return value
    return evaluate



# not particularly useful here 
def solutioncheck(equationVector):
    boolean = True
    for i in range(len(equationVector)):
        for j in range(i):
            if i != j:
                if equationVector[i][j] != 0:
                    boolean = False
            else:
                if equationVector[i][j] != 1:
                    boolean = False
    return boolean





def subMatrix(matrix,n):
    # extract a submatrix from a matrix of size n x n
    return [matrix[i][:n] for i in range(len(matrix)) if i < n ]

    
    
    
    
def optimumPolynomial(coefficentList,n):
    a = polynomial(coefficentList[:n])
    valueList = [a(i) for i in range(n)]

def solveEuler101():
    badfit = []
    lenpoly = 11
    f = polynomial([1,-1,1,-1,1,-1,1,-1,1,-1,1])
    #f = polynomial([0,0,0,1])
    basematrix = []
    solMatrix = []
    for i in range(lenpoly):
        basematrix.append([])
        for j in range(lenpoly):
            basematrix[i].append((i+1)**(j))

    for k in range(lenpoly):
        solMatrix.append(f(k+1))

    for i in range(lenpoly-1):
        print "----------------------------------------"
        sub = subMatrix(basematrix,i+1)
        print "polynomial Value:"
        print f(i+1)
        print "submatrix:"
        print sub
        addsolutionVector(sub,solMatrix[:i+1])
        solveMatrix(sub)
        print "solved subMatrix: "
        print sub
        polynew = polynomial(extractSol(sub))
        print " solution: "
        print extractSol(sub)
        badfit.append(polynew(i+2))
        print "BadFit: "
        print badfit

    print "badfit Sum"
    print sum(badfit)
        
        
                


#def FIT(coefficentList,n):
#    return optimumPolynomial(
