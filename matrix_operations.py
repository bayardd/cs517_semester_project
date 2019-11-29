"""
This module is a collection of functions which assist in matrix operations. 
These operations include multiplying, transposing, and ... matrices
 """

def multiply(lhs, rhs):

    """
    Take two matrices and multiply them

    Args:
        lhs - (List) representing the left matrix to multiply 
        rhs - (List) representing the right matrix to multiply

        Yields:
            Result of multiplying the right matrix by the left matrix
 
    """

    sum = 0
    result = []
    lhsRows = len(lhs)
    rhsColumns = len(rhs[0])

    n = len(lhs[0])
    print("X TRANSPOSE ")
    print(lhs)

    for i in range(0, lhsRows):
        result.append([]);
        for j in range(0, rhsColumns):
            # result[i].append([])
            for k in range(0, n):
                sum += lhs[i][k] * rhs[k][j]
            result[i].append(sum)
            sum = 0

    return result

def transposeMatrix(matrix):

    """ 
    Take a matrix and transpose it
    
    Args: 
        matrix - (List) representing the matrix to transpose
    
    Yields:
        Transposed matrix

    """

    result = [[matrix[j][i] for j in range(len(matrix))] for i in range(len(matrix[0]))] 

    return result


def augmentMatrix(lhs, rhs):
    pass

def matrixSolver(matrix):
    pass

def createXMatrix(matrix):

    xMatrix = []

    for i in range(0, len(matrix)):  
        new = []

        new.append(1)
        new.append(matrix[i][0])
        xMatrix.append(new)

    return xMatrix

def createYMatrix(matrix):
    yMatrix = []

    for i in range(0, len(matrix)):
        new = []
        new.append(matrix[i][1])
        yMatrix.append(new)

    return yMatrix

