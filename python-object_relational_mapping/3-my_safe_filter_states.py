#!/usr/bin/python3
"""
do you remember the previous task? Did you test "Arizona'; TRUNCATE
TABLE states ; SELECT * FROM states WHERE name = '" as an input?
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
    query = "SELECT * FROM states WHERE name = '{}' ORDER BY id ASC"
    cur.execute(query.format(state_name))
    rows = cur.fetchall()

    for row in rows:
        if row[1] == state_name:
            print(row)
    else:
        print("No result found")

    cur.close()
    db.close()
