# CS517 Semester Project - CPU Temps
This program takes a file containing CPI temperatures as input and calculates a global least squares approximation as well as a system of equations resulting from a piece 
wise linear interpolation.

## Running the Program
The driver.py file acts as the started for this application and is build using python3.7, it must be executed in order to run the application. A filename is expected as a parameter, without this
provided file, the program will exit. Additionally, the file is expected to exist within the same directory as the driver.py file. Optional two parameters include 
whether the file contains units, and the number of cores which the file contains. 

Parameters:   
Required:   
        &nbsp;&nbsp;&nbsp;&nbsp; filename - The file to be parsed. (This file is expected to be in the same directory as the driver.py file)   
    Optional:   
        &nbsp;&nbsp;&nbsp;&nbsp; units - Whether the file contains units, if so, the input should be "yes", otherwise it may be left empty and will default to false.  
        &nbsp;&nbsp;&nbsp;&nbsp; number_cores - The number of cores in the text file, this will default to 4 cores.

### Usage Examples 
./driver.py sensors-2018.12.26.txt yes    
./driver.py sensors-2018.12.26-no-label.txt

## Output
The program will output 4 text files by default, representing each individual core. These files will include the global least squares approximation as well as
the system of linear equations. These files are overridden each time the program is run, removing the previous results.