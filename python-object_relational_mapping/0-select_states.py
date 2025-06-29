#!/usr/bin/python3
"""
A script that lists all states from the database hbtn_0e_0_usa.
"""
from sys import argv
import MySQLdb

if __name__ == "__main__":
    dp = MySQLdb.connect(host="localhost",
                         port=3306,
                         user=argv[1],
                         passwd=argv[2],
                         db=argv[3]

                         )
    cur = dp.cursor()
    row = cur.execute("SELECT * FROM states ORDER BY states.id ASC;")

    for r in range(row):
        print(cur.fetchone())

    cur.close()
    dp.close()
