#!/usr/bin/python3
'''Write a script that lists all states from the database hbtn_0e_0_usa
   You must use the module MySQLdb (import MySQLdb)
'''

import MySQLdb
from sys import argv


if __name__ == "__main__":
    db = MySQLdb.connect(host="localhost", user=argv[1], passwd=argv[2],
                         db=argv[3], port=3306, charset="utf8")
    '''make a connection to the database that you wish to use'''
    cur = db.cursor()
    cur.execute("SELECT cities.id, cities.name, states.name FROM cities JOIN \
    states ON cities.state_id = states.id ORDER BY cities.id")
    rows = cur.fetchall()
    for row in rows:
        print(row)
    cur.close()
    db.close()
