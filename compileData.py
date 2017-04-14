#!/usr/bin/env python3
"""
Queries the database with a given date range and compiles all records
into a fixed length format
"""

import DBAccess as db
from datetime import datetime


def build_fixed_string(s):
    """
    Takes two lists as input and builds fixed string out of them
    Args:
        s -> input list to build string out of
    Returns:
        string
    """
    pass


def build_tran_string(tranls):
    """
    Sets up the transinfo for fixed length format
    Args:
        s -> list of products
    Returns:
        string
    """

    if len(tranls) < 3:
        return

    tranStr = ''

    tranStr += str(tranls[0]).rjust(5, '0')
    tempDate = datetime.strptime(str(tranls[1]), '%Y-%m-%d %H:%M:%S')
    tranStr += datetime.strftime(tempDate, '%Y%m%d%H%M')
    tranStr += tranls[2][(len(tranls[2]) - 6):]
    return tranStr


def build_prod_string(prodls):
    """
    Sets up the products for fixed length format
    Args:
        s -> list of products
    Returns:
        string
    """

    prodStr = ''

    if len(prodls) < 3:
        return

    # Create right justified string with 0's as padding
    prodStr += str(int(prodls[0])).rjust(2, '0')
    prodStr += str(int(prodls[1] * 100)).rjust(6, '0')
    prodStr += str(prodls[2]).ljust(10, ' ')
    return prodStr


def query_by_id(id, cur):
    """
    Query the database by id
    Args:
        id -> the id of the transaction
    Returns:
        string of returned rows
    """

    sqlProdInfo = 'SELECT trans_line.qty, trans_line.amt, products.prod_desc \
        FROM trans_line \
        JOIN products \
        WHERE trans_line.prod_num = products.prod_num \
        AND trans_id = {};'.format(id)

    prod_info = []

    prod_recs = db.query_db(sqlProdInfo, cur)
    for row in prod_recs:
        prod_info.append(build_prod_string(row))
    return prod_info


def query_db(begDate, endDate):

    """
    Opens a connection to the DB and queries based on the given date string
    Args:
        dateString -> the date range to find records in
    Returns:
        no idea yet
    """

    sqlTransID = 'SELECT trans_id, trans_date, card_num, total FROM trans \
    WHERE trans_date >= DATETIME({0}) \
    AND trans_date <= DATETIME({1});'.format(begDate, endDate)

    conn, cur = db.open_db('hw8SQLite.db')
    recs = db.query_db(sqlTransID, cur)

    for tranID in recs:
        # Create empty list for fixed string info
        fixed = []
        fixed.append(tranID[0])
        fixed.append(tranID[1])
        fixed.append(tranID[2])

        tranls = build_tran_string(fixed)
        prodls = query_by_id(tranID[0], cur)
        print(tranls)
        print(prodls)

    db.close_db(conn, cur)


def main():
    """
    testing
    """
    # have to have quotes for query to work properly
    query_db('\'2017-03-23 00:00 \'', '\'2017-05-21 23:59\'')

if __name__ == "__main__":
    main()
    exit(0)
