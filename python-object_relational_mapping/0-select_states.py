#!/usr/bin/python3
"""
0-select_states.py
A script that lists all states from the database hbtn_0e_0_usa.
"""
import sys
import MySQLdb

if __name__ == "__main__":
    dp = MySQLdb.connect(user=sys.argv[1],
                         passwd=sys.argv[2],
                         db=sys.argv[3],
                         port=3306,
                         host="localhost"
                         )
    cur = dp.cursor()
    row = cur.execute("SELECT * FROM states ORDER BY states.id;")

    for r in range(row):
        print(cur.fetchone())
