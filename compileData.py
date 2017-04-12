#!/usr/bin/env python3
"""
Queries the database with a given date range and compiles all records
into a fixed length format
"""

import DBAccess as db


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

        sqlProdInfo = 'SELECT trans_line.qty, trans_line.amt, products.prod_desc \
            FROM trans_line \
            JOIN products \
            WHERE trans_line.prod_num = products.prod_num \
            AND trans_id = {};'.format(tranID[0])

        prod_recs = db.query_db(sqlProdInfo, cur)
        for row in prod_recs:
            fixed.append(row[0])
            fixed.append(row[1])
            fixed.append(row[2])
        fixed.append(tranID[3])
        print(fixed)

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
