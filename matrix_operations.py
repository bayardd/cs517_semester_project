"""
This module is a collection of functions which assist in matrix operations. 
These operations include multiplying, transposing, and ... matrices
 """

def multiply(lhs, rhs):
    sum = 0
    result = []
    lhsRows = len(lhs)
    rhsColumns = len(rhs[0])

    n = len(lhs[0])
    print("iter")
    print(n)

    for i in range(0, lhsRows):
        result.append([]);
        for j in range(0, rhsColumns):
            result[i].append([])
            for k in range(0, n):
                sum += lhs[i][k] * rhs[k][j]

            result[i][j].append(sum)
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


# multiply(0,0)
