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
    cur = conn.cursor()
    cur.execute("SELECT * FROM states WHERE name LIKE 'N%' ORDER BY id ASC")
    query_rows = cur.fetchall()
    for row in query_rows:
        if row[1][0] == 'N':
            print(row)
    cur.close()
    db.close()
