"""

Module which deals with piece wise linear interpolation

"""

def calculateSlope(y1,y2):

    # Because difference between xn and xn + 1 will always be 30, we can hardcode it and save the calculation time.
    return (y2-y1) / 30

def calculateYIntercept(x, y,slope):
    return y - (slope*x)
    
def piece_wise_linear_interp(matrix):

    slope = 0

    for i in range(0, 3):
        
        x = matrix[i][0]
        y0 = matrix[i][1]
        y1 = matrix[i + 1][1]

        slope = calculateSlope(y0, y1)

        yIntercept = calculateYIntercept(x, y0, slope)
        
        print("Y = " + str(yIntercept) + " + " + str(slope) + "x")
