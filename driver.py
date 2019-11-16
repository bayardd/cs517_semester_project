"""
Main driver for this program. Responsible for taking command line arguments and initiating the program.
If the file provided as an command line argument is invalid this function will quit with an exception.
*** needs more details *** 
 """

import sys
import os
import matrix_operations as matrix_op
import parse_temps as parsing

def main():
    """
    Entry point into the program. 
    Currently the file must be in the same path as this program, an update is necessary to find a file given the full path.
    """

    if(len(sys.argv) < 2):
        print("Usage: file must be provided")
        exit()
    
    fileName = sys.argv[1]
    includes_units = sys.argv[2] == "yes"

    if(len(sys.argv) == 4):
        try:
            num_cores = int(sys.argv[3])
        
        # Probably should add better error handling..
        except Exception as inst:
            print(inst)
            exit()
    else:
        num_cores = 4
    
    filePath = generateFilePath(fileName)
    isValidPath = checkValidFile(filePath)
    
    #Build to adapt to number of cores?
    #Start with 1 for now...
    # Need matrix with 2 rows and n columns (2 dimensional list)
    matrices = {}
    numRows = parsing.file_len(fileName)
    numColumns = 2

    for i in range(0, num_cores):
        matrices["matrix{0}".format(i)] = [[0 for x in range(numColumns)] for x in range(numRows)]

    # matrices is a dict containing String keys which match 2d lists, corresponding to the matrices for each core.
    if(isValidPath):
        with open(filePath, 'r') as temps_file:
            for temps_as_floats in parsing.parse_raw_temps(temps_file, units=includes_units):
                
                currentRow = int(temps_as_floats[0] / 30)

                for i in range(0, num_cores):  
                    matrices["matrix{0}".format(i)][currentRow][0] = temps_as_floats[0]
                    matrices["matrix{0}".format(i)][currentRow][1] = temps_as_floats[1][i]
                
    # Matrices are being read from file. Need to finish matrix solver and calculate least squares approximation based on that.
    # Then need to repeat the same for interpolation module.
    # Also need to implement matrix solver.. 
    # xTranspose = matrix_op.transposeMatrix(x)
    # result = matrix_op.multiply(xTranspose, x)


def checkValidFile(filePath):
    """
    Takes file path provided through CLI and confirms that it exists and is a file.

    args:
        filePath - (String) File path

    yields: 
        isValidFile - (Bool) Whether provided file path is a file or not
    """
    return os.path.isfile(filePath)



def generateFilePath(fileName):
    """
    Take file name and modify it to reflect the correct path for the current OS.
    If an extension is provided it will be removed to ensure that the file is a .txt file.

    args:
        fileName - (String) File name

    yields:
        filePath - (String) The path to the file 

    """
    pathWithoutExtenson = os.path.splitext(fileName)[0]

    suffix = ".txt"
    currentDir = os.getcwd()
    return os.path.join(currentDir, pathWithoutExtenson + suffix)



if(__name__ == "__main__"):
    main()
