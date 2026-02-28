#!/usr/bin/python3
"""Safely lists all states from the database hbtn_0e_0_usa
where name matches the argument (protected from SQL injection)."""

import MySQLdb
import sys

if __name__ == "__main__":
    # Get arguments
    user = sys.argv[1]
    passwd = sys.argv[2]
    db_name = sys.argv[3]
    state_name = sys.argv[4]

    # Connect to MySQL server
    db = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=user,
        passwd=passwd,
        db=db_name
    )

    # Create cursor
    cur = db.cursor()

    # Safe parameterized query (prevents SQL injection)
    query = "SELECT * FROM states WHERE name = %s ORDER BY id ASC"
    cur.execute(query, (state_name,))

    # Fetch and print results
    for row in cur.fetchall():
        print(row)

    # Close cursor and connection
    cur.close()
    db.close()
