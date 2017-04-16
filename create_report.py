#!/user/bin/env python3
import sys
from datetime import datetime
import compileData
import sendemail


def make_report(recs, begDate, endDate):
    """
    Takes a list as input and makes a .dat file
    Args:
        recs -> list of things
    """
    fp = open("company_trans_{0}_{1}.dat".format(begDate, endDate), 'w')
    for item in recs:
        fp.write(item)
        fp.write('\n')
    fp.close()


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
        exit(1)

    # add ' to date strings for query to work
    begDate = '\'' + begDate + '\''
    endDate = '\'' + endDate + '\''

    strs = compileData.query_db(begDate, endDate)

    if len(strs) == 0:
        print("No records found. Exiting...")
        exit(2)

    for x in strs:
        print(x)
        # print(len(x))

    make_report(strs, sys.argv[1], sys.argv[2])
    sendemail.send_email(sys.argv[3], 'email_templates/Success.txt', begDate,
                         endDate)

if __name__ == "__main__":
    # call main fuction
    main()
    exit(0)
