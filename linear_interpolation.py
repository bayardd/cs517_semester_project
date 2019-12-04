"""

Module which deals with piece wise linear interpolation

"""

def calculateSlope(y1,y2):

    # Because difference between xn and xn + 1 will always be 30, we can hardcode it and save the calculation time.
    return (y2-y1) / 30
    
def piece_wise_linear_interp(matrix):

    slope = 0

    for i in range(0, len(matrix) - 1):
        slope = calculateSlope(matrix[i][1], matrix[i + 1][1])


        # we have slope, y value, b, and x value, just display equation.


    

