#!/usr/bin/python3
"""
a script that takes in an argument and displays all values
 in the states table of hbtn_0e_0_usa where name matches the argument.
 """
import MySQLdb
import sys
if __name__ == "__main__":
    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]
    state_name = sys.argv[4]

    db = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=username,
        passwd=password,
        db=database
    )
    cur = db.cursor()
    query = "SELECT * FROM states WHERE BINARY name = '{}' ORDER BY id ASC"
    cur.execute(query.format(state_name))
    rows = cur.fetchall()

    for row in rows:
        print(row)

    cur.close()
    db.close()
