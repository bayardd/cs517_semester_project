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

    print(sys.argv)
    
    fileName = sys.argv[1]
    includes_units = sys.argv[2] == "yes"

    filePath = generateFilePath(fileName)
    isValidPath = checkValidFile(filePath)

    if(isValidPath):
        with open(filePath, 'r') as temps_file:
            for temps_as_floats in parsing.parse_raw_temps(temps_file, units=includes_units):
                print(temps_as_floats)
    

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
