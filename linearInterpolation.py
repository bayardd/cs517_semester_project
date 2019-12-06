"""
Module containing the functions necessary to perform piece wise linear interpolation
"""
NEWLINE = '\n'
TAB = '\t'


def calculateSlope(y1,y2):
    
    """
    Take 2 points y1 and y2 and calculate the slope between them
    (Note that the 30 seconds is hardcoded because the distance between all x values is 30)

    Args:
        y1 - (int) representing the current y coordinate
        y2 - (int) representing the y coordinate 30 seconds ahead.

    Yields: 
        slope
    """

    return (y2-y1) / 30


def calculateYIntercept(x, y,slope):
    
    """
    Take the x and y positions, and using the slope calculate the y intercept.

    Args:
        x - (int) representing the current x coordinate
        y - (int) representing the y coordinate 30 seconds ahead.

    Yields: 
        slope
    """

    return y - (slope*x)
    

def pieceWiseLinearInterp(matrix):
    
    """
    Take a matrix and perform piece wise linear interpolation for each row

    Args:
       matrix - (list) representing the x,y points

    Yields: 
        list of linear equations.
    """

    linearEquations = []

    slope = 0

    for i in range(0, len(matrix) - 1):
        
        x = matrix[i][0]
        y0 = matrix[i][1]
        y1 = matrix[i + 1][1]

        slope = calculateSlope(y0, y1)
        yIntercept = calculateYIntercept(x, y0, slope)

        yInterceptSlopePair = (x, yIntercept, slope)
        linearEquations.append(yInterceptSlopePair)
    
    return linearEquations


def writeToFile(linearEquations, fileStream):

    """
    Write linear equations to file

    Args:
        linearEquations (List of tuples) representing the system of equations

    Yields:
        file containing the system of linear equations
    """
    
    for line in linearEquations:
        fileStream.write(f'{line[0]} <= x < {line[0] + 30};{TAB}{TAB} y = {round(line[1],3)} + {round(line[2],3)}x{TAB}{TAB}interpolation {NEWLINE}')

    



