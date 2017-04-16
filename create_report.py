#!/user/bin/env python3
import sys
from datetime import datetime
import compileData
import sendemail
import ftpaccess


def make_report(recs, begDate, endDate):
    """
    Takes a list as input and makes a .dat file
    Args:
        recs -> list of things
    """
    fileName = "company_trans_{0}_{1}.dat".format(begDate, endDate)
    fp = open(fileName, 'w')
    for item in recs:
        fp.write(item)
        fp.write('\n')
    fp.close()
    return fileName


def convert_date(begDate, endDate):
    """
    Get dates and format for input arguments
    Args:
        begDate -> begining date for date range
        endDate -> end date for date range
    Returns:
        tuple of two datetime objects
    """
    bd = datetime.strptime(begDate, "%Y%m%d")
    begin_datetime = bd.strftime("%Y-%m-%d 00:00:00")
    # Need to add exit code -1 when bad input of date occures

    ed = datetime.strptime(endDate, "%Y%m%d")
    end_datetime = ed.strftime("%Y-%m-%d 23:59:59")
    # Need to add exit code -1 when bad input of date occures

    # If statment for invalid date range for search
    # Call the Email_customer function

    # print ("This is the d string date:, ", d)
    print("Beginning date conversion is: ", begin_datetime)
    print("Ending date conversion is: ", end_datetime)
    return begin_datetime, end_datetime


def main():
    """
    Main function
    """
    try:
        begDate, endDate = convert_date(sys.argv[1], sys.argv[2])
    except ValueError:
        print("Bad date format")
        subStr = 'The create_report program exit with code 1'
        sendemail.send_email(sys.argv[3],
                             'email_templates/BadParam.txt',
                             subStr,
                             sys.argv[1],
                             sys.argv[2])
        exit(1)

    # add ' to date strings for query to work
    begDate = '\'' + begDate + '\''
    endDate = '\'' + endDate + '\''

    strs = compileData.query_db(begDate, endDate)

    if len(strs) == 0:
        print("No records found. Exiting...")
        subStr = 'The create_report program exit with code -2'
        sendemail.send_email(sys.argv[3],
                             'email_templates/NoTrans.txt',
                             subStr,
                             sys.argv[1],
                             sys.argv[2])
        exit(2)

    for x in strs:
        print(x)
        # print(len(x))

    fileName = make_report(strs, sys.argv[1], sys.argv[2])
    ftpaccess.upload_to_ftp(fileName, sys.argv[4], sys.argv[5])
    subStr = 'Successfully transfer file (FTP Address)'
    sendemail.send_email(sys.argv[3],
                         'email_templates/Success.txt',
                         subStr,
                         begDate,
                         endDate)

if __name__ == "__main__":
    # call main fuction
    main()
    exit(0)
