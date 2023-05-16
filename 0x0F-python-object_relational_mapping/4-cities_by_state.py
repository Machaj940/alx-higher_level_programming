#!/usr/bin/python3
'''Write a script that lists all states from the database hbtn_0e_0_usa
   You must use the module MySQLdb (import MySQLdb)
'''

import MySQLdb
from sys import argv


if __name__ == "__main__":
    conn = MySQLdb.connect(host="localhost", port=3306, user=argv[1], passwd=argv[2], db=argv[3], charset="utf8")
    cur = conn.cursor()
    cur.execute("SELECT cities.id, cities.name, states.name  FROM states \
                 INNER JOIN cities WHERE states.id = cities.state_id \
                 ORDER BY cities.id ASC")
    query_rows = cur.fetchall()
    for row in query_rows:
        print(row)
    cur.close()
    conn.close()
