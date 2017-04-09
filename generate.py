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




    #SELECT trans.trans_id, trans_line.qty, products.prod_desc FROM trans JOIN trans_line, products WHERE trans.trans_id = trans_line.trans_id AND trans_line.prod_num = products.prod_num;


    sqlString = 'SELECT trans.trans_id, trans.trans_date, trans.card_num, trans_line.qty, trans_line.amt, products.prod_desc, trans.total \
    FROM trans JOIN trans_line, products \
    WHERE trans.trans_id = trans_line.trans_id \
    AND trans_line.prod_num = products.prod_num \
    AND trans.trans_date >= DATETIME({0}) \
    AND trans.trans_date <= DATETIME({1});'.format(begDate, endDate)


    conn, cur = db.open_db('hw8SQLite.db')
    recs = db.query_db(sqlString, cur)

    for row in recs:
        print(row)

    db.close_db(conn, cur)

def main():
    """
    testing
    """

    #have to have quotes for query to work properly
    query_db('\'2017-03-23\'', '\'2017-05-21\'')


if __name__ == "__main__":
    main()
    exit(0)

