#!/usr/bin/python3
'''Write a script that lists all states from the database hbtn_0e_0_usa
   You must use the module MySQLdb (import MySQLdb)
'''

import MySQLdb
from sys import argv


if __name__ == "__main__":
    conn = MySQLdb.connect(host="localhost", user=argv[1], passwd=argv[2],
                           db=argv[3], port=3306, charset="utf8")
    '''make a connection to the database that you wish to use'''
    with conn.cursor() as cur:
        cur.execute("""SELECT * FROM states WHERE name LIKE BINARY %(name)s \
                     ORDER BY states.id ASC""", {'name': argv[4]})
        query_rows = cur.fetchall()
    if query_rows is not None:
        for row in query_rows:
            print(row)
