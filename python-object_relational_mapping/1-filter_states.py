#!/usr/bin/python3
"""Lists all states starting with 'N' (case-sensitive) from the database"""

import MySQLdb
import sys

if __name__ == "__main__":
    # Connect to MySQL server
    db = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=sys.argv[1],
        passwd=sys.argv[2],
        db=sys.argv[3]
    )

    # Create cursor object
    cur = db.cursor()

    # Execute SQL query using BINARY for case-sensitive match
    query = (
        "SELECT * FROM states "
        "WHERE BINARY name LIKE 'N%' "
        "ORDER BY id ASC"
    )
    cur.execute(query)

    # Fetch all rows and display results
    for row in cur.fetchall():
        print(row)

    # Close cursor and connection
    cur.close()
    db.close()
