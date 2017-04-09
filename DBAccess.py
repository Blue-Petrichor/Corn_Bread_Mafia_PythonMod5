#!/usr/bin/env python3
"""
Database acess script. Contains functions for opening a connection
to a database and reading information from it. 
USAGE: python3 DBAcess.py <dbname>
"""

import sys
import sqlite3

def open_db(dbname):
    """
    Establishes a connection to the specified DB.
    Args:
        dbname -> string of the DB to connect to
    Returns:
        cursor to the DB
    """
    
    conn = sqlite3.connect(dbname)

    if conn:
        print("connected to DB")

    cur = conn.cursor()
    return cur

def main():
    """
    Main for testing module
    """

    
    try:
        cur = open_db(sys.argv[1])
    except IndexError:
        print("Invalid arguments")
        print("USAGE: python3 DBAcess.py <dbname>")
        exit(-1)

    type(cur)


if __name__ == "__main__":
    main()
    exit(0)

