#!/usr/bin/env python3
from ftplib import FTP


def call_ftp():
    ftp = FTP('137.190.19.90')
    ftp.login()
    ftp.cwd("MockData")
    ftp.storlines("STOR test.txt", open("test.txt", "rb"))
    ftp.retrlines('LIST')
    ftp.quit()


def main():
    """
    Main function
    """
    call_ftp()


if __name__ == "__main__":
    # Call main function
    main()
    exit(0)
