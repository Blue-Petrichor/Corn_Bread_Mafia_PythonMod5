#!/usr/bin/env python3
"""
Performs FTP actions
"""
from ftplib import FTP
from ftplib import error_perm

def upload_to_ftp(upFile, user='anonymous', password='anonymous@'):
    """
    Transfer files
    Args:

    Returns:
    """
    ftp = FTP('137.190.19.90')
    ftp.login(user, password)

    if user == 'anonymous':
        ftp.cwd("MockData")
    else:
        ftp.cwd("/srv/ftp/MockData/")


    try:
        ftp.storlines("STOR {}".format(upFile), open(upFile, "rb"))
        ftp.retrlines('LIST')
    except error_perm:
        print('That file already exists or you dont have permission to write that file.')
    ftp.quit()


def main():
    """
    Main function
    """
    upload_to_ftp('test.txt')


if __name__ == "__main__":
    # Call main function
    main()
    exit(0)
