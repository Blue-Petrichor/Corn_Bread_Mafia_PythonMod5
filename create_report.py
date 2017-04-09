#!/user/bin/env python3
import sys
import re
from datetime import datetime
import argparse

def Email_customer():
    """
    Email the customer if the date range Beg_date and End_date do not have
    has no transaction availiable
    """

    # Add email header: "The create_report program exit with code -2"
    # add the code for email confirmation, need to pass email in as an argument for email as Argv[3]
    email_cust = sys.argv[3]
    # call the email txt file for the header
    mail -s "The Create_report program exit with code -2" email_cust


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
    

    # If statment for invalid date range for search
    # Call the Email_customer function

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

