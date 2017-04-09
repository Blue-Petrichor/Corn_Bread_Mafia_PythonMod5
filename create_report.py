#!/user/bin/env python3
import sys
import re
from datetime import datetime
import argparse

def convert_date():
    """
    Get dates and format for input arguments
    """
    begDateInput = sys.argv[1]
    endDateInput = sys.argv[2]

    bd = datetime.strptime(begDateInput, "%Y%m%d")
    Begin_Datetime =  bd.strftime("%Y-%m-%d HH:mm:ss")
    # Need to add exit code -1 when bad input of date occures

    
    ed = datetime.strptime(endDateInput, "%Y%m%d")
    End_Datetime = ed.strftime("%Y-%m-%d HH:mm:ss")
    # Need to add exit code -1 when bad input of date occures
        

    print ("Name of the script is", sys.argv[0])
    print ("Number of args is ", len(sys.argv))
    print ("The args are: ", str(sys.argv))

    #print ("This is the d string date:, ", d)
    print ("Beginning date conversion is: ", Begin_Datetime)
    print ("Ending date conversion is: ", End_Datetime)
    

def main():
    """
    Main function
    """
    convert_date()

    pass

if __name__ == "__main__":
    #call main fuction
    main()

    exit(0)

