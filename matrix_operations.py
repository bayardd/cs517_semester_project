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

    """
    Take a lhs matrix and rhs vector and augment the lhs matrix with the rhs vector

    Args:
        lhs - (List) representing the matrix to append the vector to
        rhs - (List) representing the vector to append to the lhs matrix

    Yields:
        Augmented Matrix

    """

    n = len(lhs)

    for i in range(0, n):
        lhs[i].insert(n, rhs[i][0])

    return lhs


def solveMatrix(matrix):

    """
    Take an augmented matrix and solve the matrix using Guassian elimination

    Args:
        matrix - (List) representing the augmented matrix to solve

    Yields:
        Solution of linear equations
    """

    n = len(matrix)
    
    #As the matrix is augmented, number of colums will be greater by 1
    numColumns = len(matrix[0])

    for i in range(0, n):
        maxIndex = findLargestRowByColumn(matrix, i, n)

        #Swap row
        swap_row(matrix, i, maxIndex)

        #Need to scale
        scale(matrix, i, numColumns, matrix[i][i])

        #Eliminate rest of column
        eliminate(matrix, i, numColumns, n)

    return backSolve(matrix)

        # print("After Swap and scaling and eliminating")
        # print(matrix)


def createXMatrix(matrix):

    """
    
    """

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


def findLargestRowByColumn(matrix, startingCol, numRows):
    """

    Yields:
        index of largest element in matrix
    """
    maxIndex = startingCol
    startingMax = matrix[startingCol][startingCol]
   
    startingPoint = startingCol + 1


    for i in range(startingPoint, numRows):
        if(matrix[startingCol][i] > startingMax):
            maxIndex = i
    return maxIndex


def swap_row(matrix, currentRow, rowToSwap):
    
    #Switch currentRow with rowToSwap (both are indexes)
    temp = matrix[currentRow]
    matrix[currentRow] = matrix[rowToSwap]
    matrix[rowToSwap] = temp;


def scale(matrix, currentRow, numColumns, scalar):
    
    for j in range(0, numColumns):
        matrix[currentRow][j] = matrix[currentRow][j] / scalar

def eliminate(matrix, startRow, numColumns, numRows):

    # print("Should be sorted")
    # print(matrix)
    startingCol = startRow

    # print("starting row " + str(startRow))
    # print("Starting column " + str(startingCol))
    # print("Number of rows " + str(numRows))

    for i in range(startRow + 1, numRows):

        s = matrix[i][startingCol]
        for j in range(startingCol, numColumns):
            matrix[i][j] = matrix[i][j] - (s * matrix[startRow][j])

        matrix[i][startingCol] = 0
  

def backSolve(matrix):
    
    augColumnId = len(matrix)
    lastRow = len(matrix) - 1

    # print(matrix)
    # print("Last row " + str(lastRow))

    for i in range(lastRow, 0, -1):
        # print("i " + str(i))
        # print("Enter for loop")
        # print("i - 1 " + str(i - 1))
        for j in range(i - 1, -1, -1):
            # print("j is " + str(j))
            s = matrix[j][i]

            # print("s is " + str(s))
            # print("augmented id " + str(augColumnId))

            matrix[j][i] = matrix[j][i] - (s * matrix[i][i])
            matrix[j][augColumnId] = matrix[j][augColumnId] - (s * matrix[i][augColumnId])
    # print("Done")
    # print(matrix)

    return matrix
