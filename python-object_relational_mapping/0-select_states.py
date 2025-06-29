#!/usr/bin/python3
"""
A script that lists all states from the database hbtn_0e_0_usa.
It takes 3 arguments: mysql username, mysql password, and database name.
"""

import MySQLdb
import sys

if __name__ == "__main__":
    """
    The main execution block that connects to the database
    and retrieves the states.
    """
    # Check if the correct number of arguments are provided
    if len(sys.argv) != 4:
        print("Usage: {} <username> <password> <database>".format(sys.argv[0]))
        sys.exit(1)

    # Database connection parameters from command-line arguments
    mysql_user = sys.argv[1]
    mysql_password = sys.argv[2]
    db_name = sys.argv[3]

    try:
        # Connect to the MySQL server
        db = MySQLdb.connect(
            host="localhost",
            port=3306,
            user=mysql_user,
            passwd=mysql_password,
            db=db_name
        )

        # Create a cursor object using the cursor() method
        cur = db.cursor()

        # SQL query to select all states, sorted by id in ascending order
        query = "SELECT * FROM states ORDER BY id ASC"

        # Execute the SQL command
        cur.execute(query)

        # Fetch all the rows in a list of lists.
        results = cur.fetchall()

        # Print each row from the results
        for row in results:
            print(row)

    except MySQLdb.Error as e:
        # Print an error message if something goes wrong with MySQL
        print("MySQL Error {}: {}".format(e.args[0], e.args[1]))
        sys.exit(1)

    finally:
        # Disconnect from the server by closing the cursor and connection
        if 'cur' in locals() and cur:
            cur.close()
        if 'db' in locals() and db:
            db.close()
