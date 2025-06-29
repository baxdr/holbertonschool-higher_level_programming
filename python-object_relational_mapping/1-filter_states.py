#!/usr/bin/python3
"""
a script that lists all states with a name starting with N
from the database hbtn_0e_0_usa
"""
import MySQLdb
import sys

if __name__ == "__main__":

    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]

    dp = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=username,
        passwd=password,
        db=database
    )
    cur = dp.cursor()
    cur.execute(
        "SELECT * FROM states WHERE name LIKE BINARY 'N%' ORDER BY id ASC")
    row = cur.fetchall()

    for i in row:
        print(i)

    cur.close()
    dp.close()
